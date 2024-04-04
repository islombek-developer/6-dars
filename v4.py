def f(x,y):
    s=''
    if len(x) > len(y):
        s+=x[len(y):]
    elif len(x) < len(y):
        s+=y[len(x):]
    return s
print(f('aaa' ,'aa'))