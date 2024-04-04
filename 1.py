def f(s):
    a = 'aeiouAEIOU'
    b = [i for i in s if i in a]
    c = ''.join(b[::-1])
    result = ''
    d = 0
    for i in s:
        if i in a:
            result += c[d]
            d += 1
        else:
            result += i
    return result,d
print(f("leetcode"))  
