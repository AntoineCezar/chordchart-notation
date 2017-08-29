import argparse
import pprint
import sys

from ..grammar import chordchart
from ..parser import parse


def parse_args(argv=sys.argv):
    parser = argparse.ArgumentParser(description='''
        Render chordchart notation to sexpression like tree.
        ''')

    parser.add_argument('input', metavar='FILE', type=str, help='''
        A file to render.
        If no files provided, it reads from stdin.
        ''')

    return parser.parse_args(argv[1:])


def main():
    args = parse_args()

    if not args.input:
        tree = parse(chordchart, sys.stdin.read())
        pprint.pprint(tree.sexpression())
    else:
        with open(args.input, 'r') as fd:
            tree = parse(chordchart, fd.read())
            pprint.pprint(tree.sexpression())
