#!/usr/bin/ python
'''
python3 script
python script code for generate grid pathfinding with tar pit problem instance.
where a tar pit cell would have higher cost to leave once the agent step in

Author: Tianyi Gu
Date: 04/20/2021
'''

__author__ = 'TianyiGu'

import argparse
from random import seed
from random import randrange
import random
import heapq

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

    parser.add_argument(
        '-pd',
        action='store',
        dest='tarPitDesity',
        help='tar pit field density: 0.25(default)',
        default='0.25')

    parser.add_argument(
        '-pc',
        action='store',
        dest='tarPitCost',
        help='cost of stepping out a tar pit cell : 10(default)',
        default='10')

    return parser


def generateCheckerBoardAndObs(args, curSeed):
    r, c = int(args.row), int(args.col)
    seed(curSeed)

    outMap = [['_'] * c for _ in range(r)]

    start = (randrange(r), 0)
    goal = (randrange(r), c-1)

    outMap[start[0]][start[1]] = '@'
    outMap[goal[0]][goal[1]] = '*'

    obsColStart = int((1 - float(args.obstacleField)) * c)
    obsColEnd = c-1
    obsColRange = range(obsColStart, obsColEnd)

    pitColEnd = int(float(args.obstacleField) * c + 5)
    pitColStart = 5
    pitColRange = range(pitColStart, pitColEnd)

    for i in range(r):
        for j in obsColRange:
            if outMap[i][j] == '@' or outMap[i][j] == '*':
                continue
            if random.uniform(0, 1) <= float(args.desity):
                outMap[i][j] = '#'

    for i in range(r):
        for j in pitColRange:
            if outMap[i][j] == '@' or outMap[i][j] == '*':
                continue

            if i == 0 and j != pitColStart and (j - pitColStart)% 2 == 0:
                outMap[i][j] = '$'
            elif i%2 == 0 and j == pitColStart:
                outMap[i][j] = '$'

    step = 0
    for j in pitColRange:
        if outMap[0][j] != '$':
            continue
        step += 1
        curRow, curCol = 0, j
        curStep = step
        while curRow < r and curCol < pitColEnd:
            if curStep % 2 == 0:
                outMap[curRow][curCol] = '$'
            curRow += 1
            curCol += 1
            curStep += 1

    step = 0
    for i in range(2, r):
        if outMap[i][pitColStart] != '$':
            continue
        step += 1
        curStep = step
        curRow, curCol = i, pitColStart
        while curRow < r and curCol < pitColEnd:
            if curStep%2 ==0:
                outMap[curRow][curCol] = '$'
            curRow += 1
            curCol += 1
            curStep += 1
    return outMap, start, goal

def printMap(outMap, args, solutionLength):
    r, c = int(args.row), int(args.col)
    print(c)
    print(r)
    for i in range(r):
        print("".join(outMap[i]))
    print(solutionLength)
    print(args.tarPitCost)

def bfs(outMap, start, goal, tarPitCost):
    openList = [(0, start)]
    closed = {start: 0}

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while openList:
        cur = heapq.heappop(openList)

        if cur[1] == goal:
            return cur[0]

        for i in range(4):
            newX = cur[1][0] + dx[i]
            newY = cur[1][1] + dy[i]

            if not isValid(newX, newY, outMap):
                continue

            cost = cur[0] + getCost(cur[1][0], cur[1][1], outMap, tarPitCost)

            if (newX, newY) in closed and closed[(newX, newY)] <= cost:
                continue

            heapq.heappush(openList, (cost, (newX, newY)))
            closed[(newX, newY)] = cost

    return -1

def isValid(x, y, outMap):
    return 0 <= x < len(outMap) and\
           0 <= y < len(outMap[0]) and\
           outMap[x][y] != '#'

def getCost(x, y, outMap, tarPitCost):
    if outMap[x][y] == '$':
        return tarPitCost
    return 1

def main():
    parser = parseArugments()
    args = parser.parse_args()
    # print(args)

    curSeed = int(args.seed)
    outMap, start, goal = generateCheckerBoardAndObs(args, curSeed)
    solutionLength = bfs(outMap, start, goal, int(args.tarPitCost))


    i = 0
    while solutionLength == -1:
        curSeed = int(args.seed) * 100 + i
        outMap, start, goal = generateCheckerBoardAndObs(args, curSeed)
        solutionLength = bfs(outMap, start, goal, int(args.tarPitCost))
        i += 1

    printMap(outMap, args, solutionLength)

if __name__ == '__main__':
    main()
