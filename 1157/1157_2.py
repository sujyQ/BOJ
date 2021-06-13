
string = input().upper()

count_list = list(map(string.count, [chr(x) for x in range(65, 91)]))

if count_list.count(max(count_list)) > 1 :
    print("?")
else :
    print(chr(count_list.index(max(count_list))+65))