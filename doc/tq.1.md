tq(1) -- Terminal based HTML query tool
=============================================

## SYNOPSIS

cat file.html | `tq` [<options>] SELECTOR

## DESCRIPTION

Perform a css query with SELECTOR on an html document passed to the standard input.

## OPTIONS

  * _SELECTOR_
    A css selector

  * `-a `_ATTRIBUTE_` --attr=`_ATTRIBUTE_
  	  Outputs only the contents of the html ATTRIBUTE.

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


## EXAMPLES


### Get headlines from hacker news

curl https://news.ycombinator.com/news | tq -tj ".title a"

### Download a gallery of nice forest pictures from flickr

curl -s 'https://www.flickr.com/photos/tgerus/galleries/72157622468645106/' | tq  ".gallery-photos img"


## AUTHORS

`tq` was written by Pedro <pedro@example.com>.

## DISTRIBUTION
The latest version of tq may be downloaded from https://github.com/plainas/tq

## SEE ALSO

curl(1), wget(1), jq(1)
