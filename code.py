def counter(s,e):
    i=s
    while i<=e:
        yield i
        i+=1
        print("sds",i)
for i in counter(0,10):
    print(i)
print("hello")
gen = [x for x in range(5)]
print(gen)
for num in gen:
    print(num)