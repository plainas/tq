#!/usr/bin/python3


"""
Test non unicode input with:
curl https://www.flashback.org/| ./tq.py -Jt ".td_forum"

Test unicode input
curl https://news.ycombinator.com/news| ./tq.py -Jt ".title a"

curl https://www.flashback.org/t2494391| ./tq.py -j ".post_message"

"""

import sys
from bs4 import BeautifulSoup
import argparse
import json
import codecs
import io

parser = argparse.ArgumentParser()
parser.add_argument("selector", help="A css selector")
parser.add_argument("-t", "--text",			action="store_true", help="Outputs only the inner text of the selected elements.")
parser.add_argument("-q", "--squash",		action="store_true", help="Squash lines.")
parser.add_argument("-s", "--squash-space",	action="store_true", help="Squash spaces.")
parser.add_argument("-j", "--json-lines",	action="store_true", help="JSON encode each match.")
parser.add_argument("-J", "--json",			action="store_true", help="Output as json array of strings.")

args = parser.parse_args()

print

if not args.selector:
    system.exit("ERROR! No selector")

if args.json and args.json_lines:
    sys.exit("ERROR! --json and --json-lines options cannot be used simultaniously")


def get_els(css_selector):
    #input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='ignore')
    input_stream = io.TextIOWrapper(sys.stdin.buffer, errors='ignore')
    soup = BeautifulSoup(input_stream)
    return soup.select(css_selector)


selected_els = get_els(args.selector)

if args.text:
    selected_els = [el.get_text() for el in selected_els]

if args.squash:
    selected_els = [el.replace('\n', ' ').el('\r', '') for el in selected_els]
	
if args.squash_space:
    selected_els = [' '.join( el.split(' ') ) for el in selected_els]

if args.json or args.json_lines:
    selected_els = [json.dumps(str(el_text)) for el_text in selected_els]


if args.json:
    sys.stdout.write(json.dumps(selected_els, indent=1))
    sys.stdout.write("\n")
else:
    for el_text in selected_els:
        sys.stdout.write(str(el_text) + "\n")
