def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
# for i in range(5):
#     print(next(g))  
#     print("*"*20)

print(next(g))
print(g.send(7))