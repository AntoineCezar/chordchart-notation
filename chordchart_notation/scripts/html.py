import argparse
import sys
import os

from ..grammar import chordchart
from ..parser import parse
from ..render.director import ChordchartDirector
from ..render.html import HtmlBuilder


def parse_args(argv=sys.argv):
    parser = argparse.ArgumentParser(description='''
        Render chordchart notation to html.
        ''')

    parser.add_argument('input', metavar='FILE', type=str, help='''
        A file to render.
        If no files provided, it reads from stdin.
        ''')

    return parser.parse_args(argv[1:])


def render(text):
    tree = parse(chordchart, text)
    builder = HtmlBuilder()
    director = ChordchartDirector(builder)
    director.visit(tree)
    return builder.get_result()


def main():
    args = parse_args()

    if not args.input:
        text = sys.stdin.read()
        out = sys.stdout
    else:
        with open(args.input, 'r') as fd:
            text = fd.read()

        output = os.path.splitext(args.input)[0] + '.html'
        out = open(output, 'w')

    result = render(text)
    out.write(result)
