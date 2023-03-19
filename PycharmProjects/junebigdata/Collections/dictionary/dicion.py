#first recursive character
word='ABCDFGBCDFGBCGF'
d={}
for i in word:
    if i not in d:
        d[i]=1
    else:
        print(i)
        break