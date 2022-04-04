#!/bin/bash

poetry version $1
sed -i -e "s/__version__ = \".*\"/__version__ = \"${1}\"/" ./codesys_code_gen/__init__.py
sed -i -e "s/assert __version__ == \".*\"/assert __version__ == \"${1}\"/" ./tests/test_codesys_code_gen.py
