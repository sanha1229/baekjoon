from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

input()
cards = sorted(list(map(int, input().split())))
input()
for s in input().split():
    t = int(s)
    print(bisect_right(cards, t) - bisect_left(cards, t))
