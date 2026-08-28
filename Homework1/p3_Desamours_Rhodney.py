def find_dup_str(s, n):
    subs = []

    for i in range(len(s) - n + 1):
        subs.append(s[i:i + n])

    for i in range(len(subs)):
        for j in range(i + 1, len(subs)):
            if subs[i] == subs[j]:
                return subs[i]

    return ""

def find_max_dup(s):
    dups = []

    for i in range(2, len(s)):
        dup = find_dup_str(s, i)
        if dup == "":
            break
        dups.append(dup)

    if dups:
        return dups[-1]
    else:
        return ""

text = input("Enter string: ")
num = 0

while text != "":
    # num = int(input("Enter substring length: "))

    # print(find_dup_str(text, num))
    print(find_max_dup(text))

    text = input("Enter string: ")