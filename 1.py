def first_funct(a):
    n = a
    def second(b):
        nonlocal n
        n=n*b
        return f"{a*b} {n}"
    return second

number = first_funct(5)
print(number(5))
print(number(5))
print(number(5))
print(number(5))