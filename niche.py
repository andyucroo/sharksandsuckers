import random

import pygame

from players import Critter

TRUE, FALSE = C, D = 1, 0

MAP_WIDTH = 20
MAP_HEIGHT = 20


class Niche:
    def addOccupant(self, occupant, x, y):
        self.occupants[x][y] = occupant

    def fill(self, species=None, widthRange=None, heightRange=None):
        if widthRange is None:
            widthRange = range(0, self.width)
        if heightRange is None:
            heightRange = range(0, self.height)
        for x in widthRange:
            for y in heightRange:
                if species:
                    self.addOccupant(random.choice(species).copy(), x, y)
                else:
                    speciesCount = {}
                    north = [x, y + 1]
                    east = [x + 1, y]
                    south = [x, y - 1]
                    west = [x - 1, y]
                    for neighbour in (north, east, south, west):
                        for ind in (0, 1):
                            if neighbour[ind] < 0 or neighbour[ind] >= (self.width, self.height)[ind]:
                                neighbour = None
                                break
                        if neighbour:
                            occupier = self.occupants[neighbour[0]][neighbour[1]]
                            kind = occupier.__class__.__name__
                            if kind in speciesCount.keys():
                                if occupier.score > speciesCount[kind][0]:
                                    speciesCount[kind][0] = occupier.score
                            else:
                                speciesCount[kind] = [occupier.score, occupier.copy()]
                    bestValue = -1000000
                    for key, (value, example) in speciesCount.items():
                        if value > bestValue:
                            bestKey, bestValue, bestExample = key, value, example
                        elif value == bestValue:
                            if key == self.occupants[x][y].__class__.__name__:
                                bestKey, bestValue, bestExample = key, value, example
                    self.nextNiche.addOccupant(bestExample.copy(), x, y)
        return self.nextNiche

    def flatList(self):
        result = []
        heightRange = range(0, self.height)
        for x in range(0, self.width):
            for y in heightRange:
                resident = self.occupants[x][y]
                if resident:
                    result.append(resident)
        return result

    def play(self, payoffs, numTurns):
        heightRange = range(0, self.height)
        turnRange = range(0, numTurns)
        for x in range(0, self.width):
            for y in heightRange:
                if isinstance(self.occupants[x][y], Critter):
                    p1 = self.occupants[x][y]
                    p1.score = 0
                    p1.memory = []
                    north = [x, y + 1]
                    east = [x + 1, y]
                    south = [x, y - 1]
                    west = [x - 1, y]
                    for neighbour in (north, east, south, west):
                        for ind in (0, 1):
                            if neighbour[ind] < 0 or neighbour[ind] >= (self.width, self.height)[ind]:
                                neighbour = None
                                break
                        if neighbour:
                            p2 = self.occupants[neighbour[0]][neighbour[1]]
                            if isinstance(p2, Critter):
                                for _ in turnRange:
                                    p1.opponent = p2
                                    p2.opponent = p1
                                    strat1 = p1.strategy()
                                    strat2 = p2.strategy()
                                    p1.addMemory(strat2)
                                    p2.addMemory(strat1)
                                    outcome = payoffs[(strat1, strat2)]
                                    p1.score += outcome[0]
                                p2.memory = []
        return self.fill()

    def textDiagram(self, topRunner="+" + "---+" * MAP_WIDTH, leftRunnerHigh="|", leftRunnerLow="+",
                    cell=['   ', '|', '---', '+'], absenceMarker='   '):
        result = topRunner + '\n'
        for y in range(0, MAP_HEIGHT):
            result += leftRunnerHigh
            for x in range(0, MAP_WIDTH):
                if self.occupants[x][y]:
                    result += self.occupants[x][y].symbol
                else:
                    result += absenceMarker
                result += cell[1]
            result += '\n' + leftRunnerLow
            cellString = ''.join([cell[2], cell[3]])
            result += cellString * MAP_WIDTH + '\n'
        return result.strip()

    def rectangleDiagram(self, viewSurface):
        for x in range(0, self.width):
            for y in range(0, self.height):
                littleRect = (x * 48 + 2, y * 36 + 2, 44, 32)
                occupier = self.occupants[x][y]
                if isinstance(occupier, Critter):
                    pygame.draw.rect(viewSurface, occupier.colour, littleRect)
        pygame.display.flip()

    def __init__(self, width=MAP_WIDTH, height=MAP_HEIGHT, projection=TRUE):
        self.width = width
        self.height = height
        if projection:
            self.nextNiche = Niche(width=self.width, height=self.height, projection=FALSE)
        self.occupants = []
        for x in range(0, width):
            newList = []
            for y in range(0, height):
                newList.append(None)
            self.occupants.append(newList)

    def __str__(self):
        return self.textDiagram()

    def __add__(self, other):
        self.addOccupant(other[2], other[0], other[1])