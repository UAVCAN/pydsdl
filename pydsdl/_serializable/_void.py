#
# Copyright (C) 2018-2019  UAVCAN Development Team  <uavcan.org>
# This software is distributed under the terms of the MIT License.
#

from .._bit_length_set import BitLengthSet
from ._root import SerializableType
from ._primitive import InvalidBitLengthError


class VoidType(SerializableType):
    MAX_BIT_LENGTH = 64

    def __init__(self, bit_length: int):
        super(VoidType, self).__init__()
        self._bit_length = int(bit_length)

        if self._bit_length < 1:
            raise InvalidBitLengthError('Bit length must be positive')

        if self._bit_length > self.MAX_BIT_LENGTH:
            raise InvalidBitLengthError('Bit length cannot exceed %r' % self.MAX_BIT_LENGTH)

    @property
    def bit_length(self) -> int:
        return self._bit_length

    def _compute_bit_length_set(self) -> BitLengthSet:
        return BitLengthSet(self.bit_length)

    def __str__(self) -> str:
        return 'void%d' % self.bit_length

    def __repr__(self) -> str:
        return 'VoidType(bit_length=%d)' % self.bit_length


def _unittest_void() -> None:
    from pytest import raises

    assert VoidType(1).bit_length_set == 1
    assert str(VoidType(13)) == 'void13'
    assert repr(VoidType(64)) == 'VoidType(bit_length=64)'
    assert VoidType(22).bit_length_set == {22}

    with raises(InvalidBitLengthError):
        VoidType(1)
        VoidType(0)

    with raises(InvalidBitLengthError):
        VoidType(64)
        VoidType(65)