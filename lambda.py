var = lambda a: a + 10
print(var(5))
x = lambda b,c: b*c
print(x(10,10))
t=lambda q,w,e:q+w+e
print(t(11,22,33))
def my():
    return lambda i:i*100
print(my())
y=my()
print(y(4))
def fun(n):
    return lambda u:u-n
s=fun(10)
print(s(22))