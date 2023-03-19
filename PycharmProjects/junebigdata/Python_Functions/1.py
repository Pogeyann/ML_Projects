def string_common():
    s1 = input('enter number')
    s2 = input('enter number')
    m = set(s1)
    n = set(s2)
    l = m & n
    print(l)

string_common()
