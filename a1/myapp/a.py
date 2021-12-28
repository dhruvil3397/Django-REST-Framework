def outer(fun):
    def inner():
        a = fun()
        b =a.upper()
        return b
    return inner



# @outer
def eb():
    return "dhruvil"

c = outer(eb)
print(c())

# print(eb())