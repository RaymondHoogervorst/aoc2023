from collections import Counter

import fileinput

PART1_ORDER = "0123456789TJQKA"
PART2_ORDER = "J0123456789TQKA"

def score(hand, part=1):
    ORDER = PART1_ORDER if part == 1 else PART2_ORDER

    hand = hand.split(' ')[0]
    freqs = Counter(hand)

    if part == 2 and freqs['J'] != 5:
        max_char, _ = max(((key, freq) for key, freq in freqs.items() if key != 'J'), key = lambda x : x[1])
        freqs[max_char] += freqs['J']
        freqs['J'] = 0

    freqs = list(freqs.values())

    # Five of a kind
    if 5 in freqs:
        rank = 7
    # Four of a kind
    elif 4 in freqs:
        rank = 6
    # Full house
    elif 3 in freqs and 2 in freqs:
        rank = 5
    #Three of a kind
    elif 3 in freqs:
        rank = 4
    # Two pair
    elif freqs.count(2) == 2:
        rank = 3
    # One pair
    elif 2 in freqs:
        rank = 2
    # High card
    else:
        rank = 1

    # Cards are first ordered by rank, then by suits in lexicographic order
    return (rank, ) + tuple(map(ORDER.index, hand))

def score2(hand):
    return score(hand, part=2)

lines = [line.strip() for line in fileinput.input()]
for score_function in (score, score2):
    lines.sort(key=score_function)
    total_winnings = 0
    for i, line in enumerate(lines):
        bid = line.split(' ')[1]
        total_winnings += (i + 1) * int(bid)

    print(total_winnings)