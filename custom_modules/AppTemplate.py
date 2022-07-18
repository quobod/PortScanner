#! /usr/bin/python3

import argparse

answer = None

parser = argparse.ArgumentParser(
    description="A template program that squares a given number"
)
group = parser.add_mutually_exclusive_group()

# group arguments
group.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="count", default=0
)
group.add_argument("-q", "--quiet", help="silently run program", action="store_true")


# positional argumens
parser.add_argument("square", help="display a square of given number", type=int)

# optional arguments

args = parser.parse_args()
answer = args.square**2

if args.quiet:
    print(answer)
elif args.verbose >= 2:
    print("The square of {} equals {}".format(args.square, answer))
elif args.verbose >= 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
