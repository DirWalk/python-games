import sys
import random
import argparse


def roll(sides, rolls=1):
    for _ in range(rolls):
        rand_number = random.choice(range(1, sides))
        print("Your roll is: {}".format(rand_number))


def run(args):
    sides = args.sides
    if args.multi_mode:
        rolls = args.multi_mode
    else:
        rolls = 0
    roll(sides, rolls)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to roll dice!')
    parser.add_argument('-s', '--sides', metavar='', type=int, help='The amount of sides for your di(c)e.', required=True, dest='sides')
    parser.add_argument('-r', '--rolls', metavar='', type=int, help="The amount of rolls for your di(c)e.", dest='multi_mode')
    args = parser.parse_args()
    run(args)
