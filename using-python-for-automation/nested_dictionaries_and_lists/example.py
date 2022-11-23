allGuests = {'Or': {'apples': 6, 'pretzels': 12}, 'Dor': {'sandwiches': 3, 'apples': 1},
             'Gil': {'cups': 3, 'apples': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought')
print(' - Apples   ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups   ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes   ' + str(totalBrought(allGuests, 'cakes')))
print(' - Sandwiches   ' + str(totalBrought(allGuests, 'sandwiches')))
