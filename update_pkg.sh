#!/usr/bin/env bash

python setup.py sdist
pip install --upgrade $(ls -l1 dist/*.tar.gz | tail -n1)
