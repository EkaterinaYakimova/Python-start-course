mydict = {}
with open("tekst 6.txt", encoding="utf-8") as f:
    for line in f:
        name, stats = line.split(':')
        elems = [i for i in stats if i == i == ' ' or (i >= '0' and i <= '9')]
        print(elems)
        subject_sum = sum(map(int, "".join(elems).split()))
        mydict[name] = subject_sum
print(f"{mydict}")

