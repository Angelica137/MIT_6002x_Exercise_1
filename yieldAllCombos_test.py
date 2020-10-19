def buildItems():
    return [Item(n, v, w) for n, v, w in (('clock', 175, 10),
                                          ('painting', 90, 9),
                                          ('radio', 20, 4),
                                          ('vase', 50, 2),
                                          ('book', 10, 1),
                                          ('computer', 200, 20))]


def buildRandomItems(n):
    return [Item(str(i), 10*random.randint(1, 10), random.randint(1, 10))
            for i in range(n)]
