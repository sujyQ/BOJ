
word = input()

alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
num_alpha = 0
len_croatia = 0

for _, x in enumerate(alpha) :
    cnt = word.count(x)
    print(word.split(x))

    if word.split(x) != word :
        

    if cnt >= 1 :
        print(cnt, x)
        len_croatia += len(x) * cnt
        num_alpha += cnt


print(num_alpha + len(word)-len_croatia)