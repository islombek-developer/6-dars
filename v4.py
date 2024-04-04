def f(t,d):
    s=''
    if len(t) > len(d):
        s+=t[len(d):]
    elif len(t) < len(d):
        s+=d[len(t):]
    return s
print(f('abcde' ,'abcd'))