#!/usr/bin/python3


"""
Test non unicode input with:
curl https://www.flashback.org/| ./tq.py -Jt ".td_forum"

Test unicode input
curl https://news.ycombinator.com/news| ./tq.py -Jt ".title a"

"""

import sys
from bs4 import BeautifulSoup
import argparse
import json
import codecs

parser = argparse.ArgumentParser()
parser.add_argument("selector", help="A css selector")
parser.add_argument("-t", "--text", action="store_true", help="Outputs only inner text of the selected elements.")
parser.add_argument("-j", "--json", action="store_true", help="JSON encode each match. Because tq only outputs strings, this can be used to force one match per output line")
parser.add_argument("-J", "--json_trimmed", action="store_true", help="same as -j but without opening anc closing quotes")

args = parser.parse_args()

def get_els(css_selector):
    #char_stream = codecs.getreader("utf-8")(sys.stdin)
    #TODO:try this instead: unicode(value, "utf-8", errors="ignore")
    char_stream = sys.stdin
    input_text = char_stream.read()
    soup = BeautifulSoup(input_text)
    return soup.select(css_selector)

selected_els = get_els(args.selector)

if args.text:
	selected_els = [el.get_text() for el in selected_els]

if args.json or args.json_trimmed:
	selected_els = [json.dumps(str(el_text)) for el_text in selected_els]

##TODO:trip first and last quote if --json_trimmed

for el_text in selected_els:
	sys.stdout.write(str(el_text) + "\n")
