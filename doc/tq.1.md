tq(1) -- Terminal based HTML query tool
=============================================

## SYNOPSIS

cat file.html | `tq` [<options>] SELECTOR

## DESCRIPTION

Perform a css query with SELECTOR on an html document passed to the standard input.

## OPTIONS

  * `selector`
    A css selector

  * `-t, --text`
    Outputs only the inner text of the selected elements.
  
  * `-q, --squash`
    Squash lines.
  
  * `-s, --squash-space`
    Squash spaces.
  
  * `-j, --json-lines`
    JSON encode each match.
  
  * `-J, --json`
    Output as json array of strings.
  
  * `-v, --version`
    Prints tq version


## AUTHORS

`tq` was written by Pedro <pedro@example.com>.

## DISTRIBUTION
The latest version of tq may be downloaded from https://github.com/plainas/tq

## SEE ALSO

curl(1), wget(1), jq(1)