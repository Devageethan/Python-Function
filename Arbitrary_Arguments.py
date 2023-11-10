def myfun(*name):
    print(name)
myfun()
myfun('deva','nobi','moni')
#keyword
def key(c1,c2,c3):
    print(c1,c2,c3)
key(c1=100,c3=300,c2=200)
#arbitarykeywords
def fun(**name):
    print(name)
fun(name1='dk',name2='blody',name3='hendry')