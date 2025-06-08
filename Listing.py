num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
hero=["ironman","ant man","superman"]
print(len(num))
idx = 0
while idx < len(num):
    print(num[idx])
    print("Found at index",idx)
    num[idx] += 1
    idx += 1
 
id=0
while id <= len(hero):
    print(hero[id])
    print("Found at index",id)
    id+=1
 
