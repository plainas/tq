#!/usr/bin/python3

import sys
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("selector", help="A css selector")
args = parser.parse_args()

def get_els(css_selector):
    input_text = sys.stdin.read()
    soup = BeautifulSoup(input_text)
    return soup.select(css_selector)

selected_els = get_els(args.selector)

selected_els_text = [el.get_text() for el in selected_els]

for el_text in selected_els_text:
	sys.stdout.write(el_text + "\n")
