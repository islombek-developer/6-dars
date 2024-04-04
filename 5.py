def f(a):
    d=[]
    for i in set(a[0]):
        if all(i in j for j in a):
            d.append(i)
    return d
x=['bella','label','roller']       
print(f(x))