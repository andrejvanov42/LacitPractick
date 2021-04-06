 #1
a = [1, 2 , 6, 1.2, 'a']
b = [x for x in a if type(x) == int and x%2 == 0 ]
print(b)

#2
d = [-1, 2 , 6, 1.2]
c = d[::2] 
print(c)

 #3
d = [-1, 2 , 6, 1.2]
e = [x for x in d if x>0]
print(e)

 #4
m = 3
l = [1, 3, 4, 7, 9]
D1 = {k:k%m for k in l}
print(D1.keys())


#5
dictionary = {'b':2, 3:4, 'a':9, 4:1}
res = [x+y for x, y in dictionary.items() if type(x) in [int, float] and type(y) in [int, float] ] 
print(res)

#6
L = [3, 2, 4, 5, -1]
L.sort()
L1 = [(L[i],L[j]) for i in range(len(L)-1) for j in range(i+1, len(L)) if L[i] < L[j]]
print(L1)


#7
l = ['a', 1, -2, 1.2]
value = [i for i in l if l.index(i)%2!=0]
keys = [i for i in l if l.index(i)%2==0]
d = {k: v for k, v in zip(keys, value)}
print(d)



