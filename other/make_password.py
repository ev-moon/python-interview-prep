# p. 486
# https://www.acmicpc.net/problem/1759

from itertools import combinations, product

len_password, _ = map(int, input().split())
chars = list(input().split())
vowels = set(chars) & {"a", "e", "i", "o", "u"}
consonants = set(chars) - vowels

answer = []
for i in range(1, len(vowels) + 1):
    j = len_password - i
    if j < 2:
        break
    vowel_combos = list(combinations(vowels, i))
    consonant_combos = list(combinations(consonants, j))
    for key_product in product(vowel_combos, consonant_combos):
        result = []
        for k in key_product:
            result.extend(list(k))
        answer.append("".join(sorted(result)))
answer.sort()
print(*answer, sep="\n")