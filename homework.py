a = [1, 2 , 6, 1.2, 'a']
b = [x for x in a if type(x) == int and x%2 == 0 ] #1
print(b)
d = [-1, 2 , 6, 1.2]
c = d[::2] #2
print(c)

e = [x for x in d if x>0] #3
print(e)

m = 3
l = [1, 3, 4, 7, 9]
l1 = [x for x in l if x%m == 0] #4
print(l1)

dictionary = {'b':2, 3:4, 'a':9, 4:1}
res = [x+y for x, y in dictionary.items() if type(x) in [int, float] and type(y) in [int, float] ]
print(res)

l = ['a', 1, -2, 1.2]

non_even = [i for i in l if l.index(i)%2!=0]
even = [i for i in l if l.index(i)%2==0]
d = {
    even[i]: non_even[i] for i in range(even) 
}
print(d)
