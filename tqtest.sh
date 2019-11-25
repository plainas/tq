#!/bin/bash

# This script executes all tests f the tests/ directory.

# For every .html file in it, it is passed as input to the `tq` command,
# the options in the corresponding .args file are provided as arguments,
# and the resulting output is compared to the matching .expected-output file.

set -o pipefail -o errexit -o nounset

for input_file in tests/*.html; do
    echo $input_file...
    basename=${input_file%.*}
    tq $(cat $basename.args) <${input_file} >$basename.actual-output 2>&1 || true
    diff $basename.expected-output $basename.actual-output
    echo OK
done