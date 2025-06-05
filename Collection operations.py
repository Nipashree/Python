collect=set()
collect.add(9)
collect.add(9)
collect.add(1)
collect.add("Me")
collect.add((1,2,3))


print(collect)

collect.remove(9)
print(collect)

collect.clear()
print(collect)
print(len(collect))

col={"hello","World","me","mine"}
print(col)
print(col.pop())
print(col.pop())
