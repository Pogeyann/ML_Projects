dic={'bigdata':1500,'python':1000,'testing':750,'webdevelop':1750,'machinelearning':2000}
#Max salry prof collect
v=list(dic.values()) #values
k=list(dic.keys())#key
print(k[v.index(max(v))])
print(k[v.index(min(v))])
v=list(dic.values())