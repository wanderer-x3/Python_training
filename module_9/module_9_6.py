def all_variants(text):
    i, j = 0, 1
    while j <= len(text):
        res = text[i:j+i]
        yield res
        i += 1
        if j + i > len(text):
            j += 1
            i = 0


a = all_variants("abc")
for i in a:
    print(i)