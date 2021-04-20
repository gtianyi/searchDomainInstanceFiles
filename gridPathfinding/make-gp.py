#!/usr/bin/ python
'''
python3 script
python script code for generate grid pathfinding problem instance.

Author: Tianyi Gu
Date: 04/20/2021
'''

__author__ = 'TianyiGu'

import argparse
from random import seed
from random import randrange
import random

researchHome = "/home/aifs1/gu/phd/research/workingPaper"
# researchHome = "/home/aifs1/gu/Downloads"


def parseArugments():

    parser = argparse.ArgumentParser(description='make-gp')

    parser.add_argument(
        '-r',
        action='store',
        dest='row',
        help='row nums: 10(default)',
        default=10)

    parser.add_argument(
        '-c',
        action='store',
        dest='col',
        help='col nums: 100(default)',
        default=100)

    parser.add_argument(
        '-s',
        action='store',
        dest='seed',
        help='random seed: 31(default)',
        default=31)

    parser.add_argument(
        '-t',
        action='store',
        dest='mapType',
        help='map type: goalObstacle, startObstacle(default), uniform',
        default='goalObstacle')

    parser.add_argument(
        '-o',
        action='store',
        dest='obstacleField',
        help='obstacle field range: 0.1(default)',
        default=0.1)

    parser.add_argument(
        '-d',
        action='store',
        dest='desity',
        help='obstacle field density: 0.25(default)',
        default=0.25)

    return parser


def main():

    parser = parseArugments()
    args = parser.parse_args()
    print(args)

    r, c = args.row, args.col
    seed(args.seed)

    outMap = [['_']*c for _ in range(r)]

    start = (0, randrange(r))
    goal = (randrange(r), c-1)

    outMap[start[0]][start[1]] = '@'
    outMap[goal[0]][goal[1]] = '*'

    colRange = range(c)

    if args.mapType == 'goalObstacle':
        obsColStart = (1 - args.obstacleField) * c
        colRange = range(obsColStart, c)

    if args.mapType == 'startObstacle':
        obsColEnd = args.obstacleField * c
        colRange = range(obsColEnd)

    for i in range(r):
        for j in colRange:
            if outMap[i][j] == '@' or outMap[i][j] == '*':
                continue
            if random.uniform(0, 1) <= args.desity:
                outMap[i][j] = '#'

    print(c)
    print(r)
    for i in range(r):
        print("".join(outMap[r]))
