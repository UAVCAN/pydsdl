#!/bin/bash

status=0

# Static type checking
if ! mypy --strict --config-file=setup.cfg pydsdl
then
    status=1
fi

# Code style checking
if ! pycodestyle --show-source pydsdl
then
    status=1
fi

# Unit tests
if coverage run --source pydsdl -m pytest --capture=no -vv pydsdl
then
    coverage report
else
    status=1
fi

exit $status
