import sys


def get_max_score_diff(cards):
    score_a = 0
    score_b = 0
    cards.sort(reverse=True)
    for i, c in enumerate(cards):
        if i % 2 == 0:
            score_a += c
        else:
            score_b += c
    return score_a - score_b


def main():
    N = int(sys.stdin.readline().rstrip())
    cards = [int(x) for x in sys.stdin.readline().rstrip().split()]
    ans = get_max_score_diff(cards)
    print(ans)


if __name__ == '__main__':
    main()
    
