# tq

tq is command line utility  that performs performs an HTML element selection on HTML content passed to the stdin. Using css selectors that everybody knows.

Since input comes from stdin and output is sent to stout. It can easily be be used inside traditional UNIX pipelines to extract content from webpages and html files.

tq provides extra formating options such as json-encoding or newlines squashing, so it can pley nicely with everyones favourite command line tooling.


## Instalation

	sudo pip install https://github.com/plainas/tq/zipball/stable


## Example usage

Get headlines from hacker news

	curl https://news.ycombinator.com/news | tq -tj ".title a"

Get the title of an html document stored in a file

	cat mydocument.html | tq -t title

Get all the images from a webpage

	TODO: add this example


Notice that tq doesn't provide a way to make http requests or read files. You can use your favorite HTTP client, or provide the html source from any source you want.

For a modern, user friendly http client, check httpie. Or you can just use curl, wget, netcat, etc.

## Command options

  * `SELECTOR`
    A css selector

  * `-a ATTRIBUTE --attr=ATTRIBUTE`
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
