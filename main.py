from decimal import Decimal
from http.cookiejar import user_domain_match

from attr.setters import frozen

#a = 0.5

#print(a)

#a = 0.1 + 0.2
#print(a)
# assert a == 0.3

#import math

#print(math.pi)

#import random

#random.seed("some word")

#print("----------------------")

#print(random.randint(0, 100))
#print(random.randint(0, 100))
#print(random.randint(0, 100))

#print("----------------------")

#print(round(1.3333333, 2))

#print("----------------------")

#s = "Hello, \nworld!"
#print(s)
#s1 = 'Hello, world!'
#print(s1)
#s2 = """Hello,
#world!"""
#print(s2)
#s3 = '''He
#llo,
#world!'''
#print(s3)

#s = "Hello, \\nworld!"
#print(s)

#s = r"Hello, \\nworld!"
#print(s)

#email= "user@domain.com"

#print(email[1])
#print(email[-1])
#print(email[:5])
#print(email[0:10:2])
#print(email[::-1])

#assert email.endswith("domain.com")
#email.islower()
#email.split("@")

#a = "Hello"
#b = "World"
#print(a + ", " + b + "!")
#print("{a}, {b}!".format(a=a, b=b))
#print(f"{a=}, {b=}!")
#print(f"{a=}, {b.upper()}!")
#print("%s, %s!" % (a, b))

#url_template = "https://yourservice.com/v1/api/{}"
#users_url = url_template.format("users")
#groups_url = url_template.format("groups")

#s = "1234"
#n = 1234

#assert s == str(n)
#assert int(s) == n

# Списки

#l = [1, 2, 3, "a", "b", "c", [4, 5, 6]]

#print(l[0])
#print(l[-1])
#print(l[-1][0])
#print(l[::-1])

#l.append("new element")
#l.extend(["elem", "another elem"])
#len(l)
#l.reverse()

#l[0] = 200
#print(l)

# Множества

#s = {1, 2, 3, 4, 5, 5, 5, 5}
#s1 = {1, 2, 5, 5}
#print(s)
#(s1)

#print(s.intersection(s1))
#print(s - s1)

#print(list(set([1, 2, 3, 4, 5, 5, 5])))

# Словари

#d = {
#     "key": "value",
#     "another": "another value"
#     }

user1 = {
     "name": "Vasya",
     "age": 18,
}

user2 = {
    "name": "Petya",
     "age": 20,
}

users = {
     25: user1,
     42: user2
}

#print(users[42])
#print(user1["name"])
#print(user2["name"])

#from pprint import pprint
#pprint(list(users.items()))
#print(users.values())
#print(users.keys())

#print(users.get(50, {"name": "default user"}))
#print(users[42])

#users[55] = {"name": "Oleg", "age": 25}

# Списки, словари и множества - изменяемые!

#from copy import deepcopy

#l1 = [1, 2, 3, [5, 6, 7]]
#l2 = l1.copy()
#l2 = deepcopy(l1)
#l2[-1].append(8)
#l2.append(4)

#print(l1)
#print(l2)

# Кортежи, frozen - нет

#t = (1, 2, 3)
#print(t.index(2))

#frozenset({1, 2, 3, 4, 5, 5, 5})