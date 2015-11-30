#!/bin/sh

# ronn is used to turn the markdown into a manpage.
# Get ronn at https://github.com/rtomayko/ronn
# Alternately, since ronn is a Ruby gem, you can just
# `gem install ronn`

ronn --roff tq.1.md
