def max(a,b):
    if a>b:
        return a
    else:
        return b

name = "Ryuhana"
print(f"Hello, {name}!")

a = 10
b = 20
print(f"The sum of {a} and {b} is {a + b}")

ls=[1,2,3,4,5]
print(f"{ls[1]}+{ls[2]}={ls[1]+ls[2]}")

print(f"The bigger num between {a} and {b} is {max(a,b)}")

r = 2
pi = 3.1415926
print(f"The area of the circle is: {pi*r*r:.2f}")

print(f"{'Left':<10} | {'Center':^10} | {'Right':>10}")

def func(x):
    return 3*x
print(list(map(func,[1,2,3,4,5])))

print(list(map(lambda x,y: x*y, [1, 2, 3, 4, 5],[1, 2, 3, 4, 5])))

s = "Hello world"
print(s.title())
print(s.upper())
print(s.lower())

s = " Hello world "
print(f"_{s.strip()}_")
print(f"_{s.lstrip()}_")
print(f"_{s.rstrip()}_")

a = {1,2,3}
b = {2,4,3}

print(a|b) # 并集
print(a&b) # 交集
print(a-b) # 差集
print(a^b) # 环合

s = "Hello world"
print(set(s))