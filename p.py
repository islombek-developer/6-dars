# def f(x):
#     return sum(i in "a,i,o,u,e" for i in x)
# a="salom,qale,bolyapi"
# print(f(a))

# def f(x):
#     vowels = 'aeiou'
#     result = ''
#     for i in x:
#         if i in vowels:
#             result += '1'
#         else:
#             result += '0'
#     return result

# d = "salom"
# print(f(d)) 

# import string
# def gimme_the_letters(sp):
#     a = ''
#     for i in range(ord(sp[0]), ord(sp[-1])+1):
#         if ord('a') <= i <= ord('z'):
#             a += chr(i)
#         elif ord('A') <= i <= ord('Z'):
#             a += chr(i)
#     return a
# def gimme_the_letters(sp):
#     return "".join(chr(x) for x in range(ord(sp[0]),ord(sp[-1])+1))
# d = "h-o"
# print(gimme_the_letters(d))

# b = 90061
# def f(soniya):
#     kun = soniya // (24 * 60 * 60)
#     soat = (soniya % (24 * 60 * 60)) // (60 * 60)
#     daqiqa = ((soniya % (24 * 60 * 60)) % (60 * 60)) // 60
#     soniya_qolgan = ((soniya % (24 * 60 * 60)) % (60 * 60)) % 60
#     return kun*1000+soat*100+daqiqa*10+soniya_qolgan
# print(f(b))



