#!/bin/sh
set -ex

# unpack and install the tools
cd aoc-tools
tar -xvf aoc-tools-*-x86_64-unknown-linux-musl.tar.gz
mv aoc-tools /usr/local/bin/
cd ../

# unpack and install the lanjian solution
cd repo
tar -xvf lanjian-aoc-*-x86_64-unknown-linux-gnu.tar.gz
mv aoc /usr/local/bin/lanjian-aoc

# this is now above us
INPUTS_DIR="../aoc-inputs-write/${YEAR}"

# use the tools to check the inputs
aoc-tools ci check-solutions lanjian "$INPUTS_DIR"
