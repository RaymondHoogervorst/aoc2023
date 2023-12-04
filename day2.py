import fileinput

MAX_CUBES = {
    "red" : 12,
    "green" : 13,
    "blue" : 14,
}

COLOURS = MAX_CUBES.keys()

p1 = 0
p2 = 0

for line in fileinput.input():
    game, hands = line.split(':')
    game_id = int(game.split()[1])

    min_set = {}

    for hand in hands.split(';'):
        for set in hand.split(','):
            cnt, colour = set.split()
            min_set[colour] = max(min_set.get(colour, 0), int(cnt))
    
    # Part 1: Add game_id if the min_set fits in MAX_CUBES
    if all(min_set.get(colour, 0) <= MAX_CUBES[colour] for colour in COLOURS):
        p1 += game_id

    # Part 2: Add the power of the game
    pow = 1
    for colour in COLOURS:
        pow *= min_set.get(colour, 0)
    p2 += pow

print(p1, p2)