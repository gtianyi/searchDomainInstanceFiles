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
import collections

def parseArugments():

    parser = argparse.ArgumentParser(description='make-gp')

    parser.add_argument(
        '-r',
        action='store',
        dest='row',
        help='row nums: 10(default)',
        default='10')

    parser.add_argument(
        '-c',
        action='store',
        dest='col',
        help='col nums: 100(default)',
        default='100')

    parser.add_argument(
        '-s',
        action='store',
        dest='seed',
        help='random seed: 31(default)',
        default='31')

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
        default='0.1')

    parser.add_argument(
        '-d',
        action='store',
        dest='desity',
        help='obstacle field density: 0.25(default)',
        default='0.25')

    return parser


def generateRandomMap(args, curSeed):
    r, c = int(args.row), int(args.col)
    seed(curSeed)

    outMap = [['_'] * c for _ in range(r)]

    start = (randrange(r), 0)
    goal = (randrange(r), c-1)

    outMap[start[0]][start[1]] = '@'
    outMap[goal[0]][goal[1]] = '*'

    colRange = range(c)

    if args.mapType == 'goalObstacle':
        obsColStart = int((1 - float(args.obstacleField)) * c)
        colRange = range(obsColStart, c)

    if args.mapType == 'startObstacle':
        obsColEnd = int(float(args.obstacleField) * c)
        colRange = range(obsColEnd)

    for i in range(r):
        for j in colRange:
            if outMap[i][j] == '@' or outMap[i][j] == '*':
                continue
            if random.uniform(0, 1) <= float(args.desity):
                outMap[i][j] = '#'

    return outMap, start, goal

def printMap(outMap, args, solutionLength):
    r, c = int(args.row), int(args.col)
    print(c)
    print(r)
    for i in range(r):
        print("".join(outMap[i]))
    print(solutionLength)

def bfs(outMap, start, goal):
    queue = collections.deque([start])
    dist = {start : 0}

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        cur = queue.popleft()

        if cur == goal:
            return dist[cur]

        for i in range(4):
            newX = cur[0] + dx[i]
            newY = cur[1] + dy[i]

            if not isValid(newX, newY, outMap):
                continue
            if (newX, newY) in dist:
                continue
            queue.append((newX, newY))
            dist[(newX, newY)] = dist[cur] + 1

    return -1

def isValid(x, y, outMap):
    return 0 <= x < len(outMap) and\
           0 <= y < len(outMap[0]) and\
           outMap[x][y] != '#'

def main():
    parser = parseArugments()
    args = parser.parse_args()
    # print(args)

    curSeed = int(args.seed)
    outMap, start, goal = generateRandomMap(args, curSeed)
    solutionLength = bfs(outMap, start, goal)

    i = 0
    while solutionLength == -1:
        curSeed = int(args.seed) * 100 + i
        outMap, start, goal = generateRandomMap(args, curSeed)
        solutionLength = bfs(outMap, start, goal)
        i += 1

    printMap(outMap, args, solutionLength)

if __name__ == '__main__':
    main()
