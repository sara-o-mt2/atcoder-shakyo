import sys
from sys import stdin
input = stdin.readline


def solve(cards):
    score_a = 0
    score_b = 0
    cards.sort(reverse=True)
    for i, c in enumerate(cards):
        if i % 2 == 0:
            score_a += c
        else:
            score_b += c
    return score_a - score_b


def main(args):
    N = int(input())
    cards = [int(x) for x in input().split()]
    ans = solve(cards)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
    
