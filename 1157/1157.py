import sys
from string import ascii_uppercase
input = sys.stdin.readline()[:-1].upper()

input = list(input)
alphabet_list = list(ascii_uppercase)

count = []

for _, alpha in enumerate(alphabet_list) :
    count.append(input.count(alpha))

max_count = max(count)

idx_max_count = [i for i, cnt in enumerate(count) if cnt == max_count]
if len(idx_max_count) > 1 :
    print("?")
else : 
    print(alphabet_list[idx_max_count[0]])