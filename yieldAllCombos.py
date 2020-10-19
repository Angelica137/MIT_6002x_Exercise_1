def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    if (items == []):
        yield ([], [])
    else:
        item = items[0]
        for result in yieldAllCombos(items[1:]):
            yield (result[0], result[1])
            yield ([item] + result[0], result[1])
            yield (result[0], [item] + result[1])


items = ['a', 'b']
gen = yieldAllCombos(items)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
