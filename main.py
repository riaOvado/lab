
import operator


def f(n):
    if n == 0:
        return 1
    return f(n-1) * n

dictionary = {'k':(11), 'o':(15), 'r':(18), 't':(20), 'i':(9), 'v':(22), 'a':(1)}
# number 1
print("1...................................................................................")
fib1 = 1
fib2 = 1

k = dictionary['k']
k = int(k)

i = 0
while i < k - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("Значение элемента k:", fib2)
fib1 = 1
fib2 = 1
o = dictionary['o']
o = int(o)

i = 0
while i < o - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("Значение элемента o  :", fib2)
fib1 = 1
fib2 = 1
r = dictionary['r']
r = int(r)

i = 0
while i < r - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("Значение элемента r :", fib2)
fib1 = 1
fib2 = 1
t = dictionary['t']
t = int(t)

i = 0
while i < t - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("Значение элемента t :", fib2)
fib1 = 1
fib2 = 1
I = dictionary['i']
I = int(I)

i = 0
while i < I - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("Значение элемента i :", fib2)
fib1 = 1
fib2 = 1
v = dictionary['v']
v = int(v)

i = 0
while i < v - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("Значение элемента v :", fib2)
fib1 = 1
fib2 = 1
a = dictionary['a']
a = int(a)

i = 0
while i < a - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("Значение элемента a :", fib2)

#number 2
print("2..................................................................")

sorted_by_value = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_by_value)

file_to_save = open('f2.txt', 'w+')
file_to_save.write(str(sorted_by_value))
file_to_save.close()
# number 3
print("3.............................................................................")
num = [89, 610, 2584, 6765, 34, 17711, 1]

num.sort()
print(f'Возрастание {num}')


#number 4
print("4..............................................................................")

dictionary_4 = {'k':(11), 'o':(15), 'r':(18), 't':(20), 'i':(9), 'v':(22), 'a':(1)}

g = dictionary_4.values()

fg= (sum(g) / len(g))

dictionary_4_1 = [i for i in g if i < fg]
dictionary_4_2 = [i for i in g if i > fg]

print(dictionary_4_1)
print(dictionary_4_2)


# number 5
print("5............................................................")
sr = sum(num) / len(num)
print(sr)
up = []
for i in num:
    if i > sr:
        up.append(i)
print(up)

down = []
for i in num:
    if i < sr:
        down.append(i)
print(down)
