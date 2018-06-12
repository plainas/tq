"""
Test non unicode input with:
curl https://www.flashback.org/| ./tq.py -Jt ".td_forum"

Test unicode input
curl https://news.ycombinator.com/news | ./tq.py -Jt ".title a"

curl https://www.flashback.org/t2494391 | ./tq.py -j ".post_message"

"""

#TODO: use add_mutually_exclusive_group()

import sys
from bs4 import BeautifulSoup
import argparse
import json
import codecs
import io

version = "0.2.0"


parser = argparse.ArgumentParser(description="Performs a css selection on an HTML document.", prog= "tq")
parser.add_argument("selector", help="A css selector")
parser.add_argument("-t", "--text",			action="store_true", help="Outputs only the inner text of the selected elements.")
parser.add_argument("-q", "--squash",		action="store_true", help="Squash lines.")
parser.add_argument("-s", "--squash-space",	action="store_true", help="Squash spaces.")
parser.add_argument("-j", "--json-lines",	action="store_true", help="JSON encode each match.")
parser.add_argument("-J", "--json",			action="store_true", help="Output as json array of strings.")
parser.add_argument("-v", "--version",		action="store_true", help="Ouputs tq version")
parser.add_argument("-a", "--attr",                              help="Ouputs only te contents of given HTML attribute of selected elements")
parser.add_argument("-p", "--parent",       action="store_true", help="Select the parents of the elements matching the selector")

args = parser.parse_args()

def main():

    if args.version:
        print(version)
        sys.exit(0)

    if not args.selector:
        system.exit("ERROR! No selector")

    if args.json and args.json_lines:
        sys.exit("ERROR! --json and --json-lines options cannot be used simultaniously")


    def get_els(css_selector):
        #input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='ignore')
        input_stream = io.TextIOWrapper(sys.stdin.buffer, errors='ignore')
        soup = BeautifulSoup(input_stream, "html.parser")
        return soup.select(css_selector)

    selected_els = get_els(args.selector)


    if args.parent:
        selected_els = [el.parent for el in selected_els]

    if args.attr:
        selected_els = [el.get(args.attr) for el in selected_els if args.attr in el.attrs]

    if args.text:
        selected_els = [el.get_text() for el in selected_els]

    if args.squash:
        selected_els = [el.replace('\n', ' ').replace('\r', '') for el in selected_els]

    if args.squash_space:
        selected_els = [el.replace('\t', ' ') for el in selected_els]
        selected_els = [' '.join( el.split(' ')) for el in selected_els]


    if args.json or args.json_lines:
        selected_els = [json.dumps(str(el_text)) for el_text in selected_els]


    if args.json:
        sys.stdout.write(json.dumps(selected_els, indent=1))
        sys.stdout.write("\n")
    else:
        for el_text in selected_els:
            sys.stdout.write(str(el_text) + "\n")
