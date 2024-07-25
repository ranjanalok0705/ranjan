from collections import Counter
ref = input().strip("[]").split(",")
ch = input().lstrip("[]").rstrip(']').split(",")
temp = [i for i in ref]
ch_counter = Counter(ch)
for word in ref:
    ref_char = Counter(word)
    for i in ref_char.keys():
        if i not in ch_counter:
            temp.remove(word)
            break
        continue

if temp:
    print(",".join(temp))
else:
    print("No")
