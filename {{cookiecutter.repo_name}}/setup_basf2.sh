#!/bin/bash

RELEASE={{cookiecutter.release}}
TOOLS=/cvmfs/belle.cern.ch/tools

unset PYTHONPATH
source $TOOLS/b2setup
b2setup $RELEASE
export PATH=$PATH:~/.local/bin
