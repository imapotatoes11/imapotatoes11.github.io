def has_syncpation(line):
    for i,c in enumerate(line):
        if i%2==1 and c=="#":
            return True
    return False

print(has_syncpation("#######......"))
print(has_syncpation("#.#.#"))