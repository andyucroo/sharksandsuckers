TRUE, FALSE = C, D = 1, 0

class Critter:
    critterCount = 0

    def strategy(self):
        raise ValueError

    def addMemory(self, newMemory):
        self.memory.append(newMemory)

    def copy(self):
        return self.__class__(symbol=self.symbol)

    def __init__(self, symbol=' x '):
        self.memory = []
        self.score = 0
        Critter.critterCount += 1
        self.idnum = Critter.critterCount
        self.symbol = symbol
        self.colour = (0, 0, 0)

    def __str__(self):
        result = "%s [%s]" % (str(self.__class__.__name__), str(self.idnum))
        return result

    def __copy__(self):
        return self.copy()


class Sucker(Critter):
    def strategy(self):
        return C

    def __init__(self, symbol=' + '):
        Critter.__init__(self, symbol)
        self.colour = (192, 0, 0)


class Shark(Critter):
    def strategy(self, symbol=' - '):
        return D

    def __init__(self, symbol=' + '):
        Critter.__init__(self, symbol)
        self.colour = (0, 192, 0)


class Madman(Critter):
    def strategy(self):
        return random.choice((C, D))

    def __init__(self, symbol=' ! '):
        Critter.__init__(self, symbol)
        self.colour = (63, 0, 255)


class Neutral(Critter):
    def strategy(self):
        if len(self.memory) > 0:
            return self.memory[-1]
        return C

    def __init__(self, symbol=' @ '):
        Critter.__init__(self, symbol)
        self.colour = (0, 0, 192)


class Conservative(Critter):
    def strategy(self):
        if len(self.memory) > 2:
            return self.memory[-1] and self.memory[-2]
        if len(self.memory) == 1:
            return self.memory[-1]
        return C

    def __init__(self, symbol=' # '):
        Critter.__init__(self, symbol)
        self.colour = (192, 0, 192)


class Liberal(Critter):
    def strategy(self):
        if len(self.memory) > 2:
            return self.memory[-1] or self.memory[-2]
        if len(self.memory) == 1:
            return self.memory[-1]
        return C

    def __init__(self, symbol=' # '):
        Critter.__init__(self, symbol)
        self.colour = (255, 255, 0)


class Bee(Critter):
    def __init__(self, symbol=' b ', signal=[C, D, D, D, C]):
        beeSymbol = symbol
        Critter.__init__(self, symbol=beeSymbol)
        self.signal = signal
        self.friendFlag = TRUE
        self.colour = (0, 0, 0)


class BeeShark(Bee):
    def strategy(self):
        turn = len(self.memory)
        if turn == 0:
            self.friendFlag = TRUE
        if self.friendFlag and turn < len(self.signal):
            if turn > 0:
                for oldTurn in range(0, turn):
                    if self.memory[oldTurn] != self.signal[oldTurn]:
                        self.friendFlag = FALSE
                        break
            if self.friendFlag:
                return self.signal[turn]
            return D
        return self.friendFlag

    def __init__(self, symbol='-b-', signal=[C, D, D, D, C]):
        Bee.__init__(self, symbol)
        self.colour = (31, 31, 31)


class BeeNeutral(Bee):
    def strategy(self):
        def neutralStrategy(self):
            if len(self.memory) > 0:
                return self.memory[-1]
            return C

        turn = len(self.memory)
        if turn == 0:
            self.friendFlag = TRUE
        if self.friendFlag and turn < len(self.signal):
            if turn > 0:
                for oldTurn in range(0, turn):
                    if self.memory[oldTurn] != self.signal[oldTurn]:
                        self.friendFlag = FALSE
                        break
            if self.friendFlag:
                return self.signal[turn]
            return neutralStrategy(self)
        if self.friendFlag:
            return C
        return neutralStrategy(self)

    def __init__(self, symbol='-n-', signal=[C, D, D, D, C]):
        Bee.__init__(self, symbol)
        self.colour = (64, 128, 0)


class BeeConservative(Bee):
    def strategy(self):
        def conservativeStrategy(self):
            if len(self.memory) > 2:
                return self.memory[-1] and self.memory[-2]
            if len(self.memory) == 1:
                return self.memory[-1]
            return C

        turn = len(self.memory)
        if turn == 0:
            self.friendFlag = TRUE
        if self.friendFlag and turn < len(self.signal):
            if turn > 0:
                for oldTurn in range(0, turn):
                    if self.memory[oldTurn] != self.signal[oldTurn]:
                        self.friendFlag = FALSE
                        break
            if self.friendFlag:
                return self.signal[turn]
            return conservativeStrategy(self)
        if self.friendFlag:
            return C
        return conservativeStrategy(self)

    def __init__(self, symbol='-c-', signal=[C, D, D, D, C]):
        Bee.__init__(self, symbol)
        self.colour = (63, 63, 255)


class BeeLiberal(Bee):
    def strategy(self):
        def liberalStrategy(self):
            if len(self.memory) > 2:
                return self.memory[-1] or self.memory[-2]
            if len(self.memory) == 1:
                return self.memory[-1]
            return C

        turn = len(self.memory)
        if turn == 0:
            self.friendFlag = TRUE
        if self.friendFlag and turn < len(self.signal):
            if turn > 0:
                for oldTurn in range(0, turn):
                    if self.memory[oldTurn] != self.signal[oldTurn]:
                        self.friendFlag = FALSE
                        break
            if self.friendFlag:
                return self.signal[turn]
            return liberalStrategy(self)
        if self.friendFlag:
            return C
        return liberalStrategy(self)

    def __init__(self, symbol='-l-', signal=[C, D, D, D, C]):
        Bee.__init__(self, symbol)
        self.colour = (64, 0, 128)


class Nazi(Bee):
    def strategy(self):
        turn = len(self.memory)
        if turn == 0:
            self.friendFlag = TRUE
        if self.friendFlag and turn < len(self.signal):
            if turn > 0:
                for oldTurn in range(0, turn):
                    if self.memory[oldTurn] != self.signal[oldTurn]:
                        self.friendFlag = FALSE
                        break
            if self.friendFlag:
                return self.signal[turn]
            return D
        return D

    def __init__(self, symbol='-l-', signal=[C, D, D, D, C]):
        Bee.__init__(self, symbol)
        self.colour = (192, 192, 192)


class Wasp(BeeShark):
    def __init__(self, symbol='-w-', signal=[C, D, D, D, C, D, D]):
        Bee.__init__(self, symbol, signal=[C, D, D, D, C, D, D])
        self.colour = (140, 60, 200)


class Grifter(Critter):
    def strategy(self):
        if len(self.memory) % 3 == 1:
            return D
        if len(self.memory) > 2:
            return self.memory[-1] or self.memory[-2]
        if len(self.memory) == 1:
            return self.memory[-1]
        return C

    def __init__(self, symbol=' g '):
        Critter.__init__(self, symbol)
        self.colour = (63, 255, 63)


class Bludger(Critter):
    """ Grifter variant; by Avi Waksberg """

    def strategy(self):
        if len(self.memory) % 3 == 1:
            return D
        if len(self.memory) > 2:
            return self.memory[-1] and self.memory[-2]
        if len(self.memory) == 1:
            return self.memory[-1]
        return C

    def __init__(self, symbol=' $ '):
        Critter.__init__(self, symbol)
        self.colour = (255, 63, 63)


class Metamorph(Critter):
    def strategy(self):
        if self.score < 6:
            return D
        return C

    def __init__(self, symbol=' % '):
        Critter.__init__(self, symbol)
        self.colour = (191, 191, 191)


class Ffrenchman(Critter):
    """ Suggested by Rohan Ffrench """

    def strategy(self):
        opponentType = self.opponent.__class__.__name__
        if opponentType in self.strategyTable.keys():
            return self.strategyTable[opponentType]()
        return self.liberal()

    def __init__(self, symbol=' F '):
        self.shark = Shark().strategy
        self.neutral = Neutral().strategy
        self.liberal = Liberal().strategy
        self.conservative = Conservative().strategy
        self.grifter = Grifter().strategy
        self.nazi = Nazi().strategy
        self.strategyTable = {'Sucker': self.shark,
                              'Shark': self.shark,
                              'Neutral': self.neutral,
                              'Conservative': self.conservative,
                              'Liberal': self.grifter,
                              'BeeShark': self.nazi,
                              'BeeNeutral': self.nazi,
                              'BeeLiberal': self.nazi,
                              'BeeConservative': self.nazi,
                              'Nazi': self.nazi,
                              'Wasp': self.nazi,
                              'Grifter': self.conservative,
                              'Bludger': self.liberal,
                              'Metamorph': self.grifter}
        Critter.__init__(self, symbol)
        self.colour = (255, 127, 31)


class Parisian(Ffrenchman):
    def __init__(self, symbol=' P '):
        Ffrenchman.__init__(self, symbol)
        self.strategyTable = {'Sucker': self.shark,
                              'Shark': self.shark,
                              'Neutral': self.shark,
                              'Conservative': self.shark,
                              'Liberal': self.grifter,
                              'BeeShark': self.nazi,
                              'BeeNeutral': self.nazi,
                              'BeeLiberal': self.nazi,
                              'BeeConservative': self.nazi,
                              'Nazi': self.shark,
                              'Wasp': self.nazi,
                              'Grifter': self.shark,
                              'Bludger': self.shark,
                              'Metamorph': self.grifter}
        self.colour = (191, 31, 255)


class Teenager(Critter):
    """ By Colin Jacobs """

    def strategy(self):
        c_count = 0
        d_count = 0
        for x in self.memory:
            if (x == C):
                c_count += 1
            else:
                d_count += 1
        if (c_count > d_count):
            return C
        return D

    def __init__(self, symbol=' T '):
        Critter.__init__(self, symbol)
        self.colour = (0, 120, 120)


class Nonconformist(Critter):
    """ Teenager variant """

    def strategy(self):
        c_count = 0
        d_count = 0
        for x in self.memory:
            if (x == C):
                c_count += 1
            else:
                d_count += 1
        if (c_count > d_count):
            return D
        return C

    def __init__(self, symbol=' N '):
        Critter.__init__(self, symbol)
        self.colour = (80, 0, 80)


class Feudalist(Critter):
    def __init__(self, symbol=' > '):
        Critter.__init__(self, symbol)
        self.prince = FALSE
        self.colour = (196, 196, 255)

    def strategy(self):
        opponentType = self.opponent.__class__.__name__
        if self.prince:
            if opponentType == 'Feudalist':
                if self.opponent.prince:
                    return C
            return D
        else:
            if opponentType == 'Feudalist':
                return C
            else:
                self.prince = TRUE
                return D


class Bolshevik(Critter):
    def strategy(self):
        opponentType = self.opponent.__class__.__name__
        if opponentType == 'Bolshevik':
            return C
        return D
        self.colour = (0, 0, 0)