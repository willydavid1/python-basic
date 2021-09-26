list = [1,2,3,4,5]
list.append(6)
print(list) # [1, 2, 3, 4, 5, 6]


list = [1,2,3,4,5]
list.clear() 
print(list) # []


l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1) # [1, 2, 3, 4, 5, 6]


["Hola", "mundo", "mundo"].count("Hola") # 1


["Hola", "mundo", "mundo"].index("Hola") # 0

l = [1,2,3]
l.insert(0,0)


l = [10,20,30,40,50]
print(l.pop()) # 50
print(l) # [10, 20, 30, 40]


print(l.pop(0)) #10
print(l) # [20, 30, 40]


l = [20,30,30,30,40]
l.remove(30)
print(l) # [20, 30, 30, 40]


l = [20, 30, 30, 40]
l.reverse()
print(l) # [40, 30, 30, 20]


list = [5,-10,35,0,-65,100]
list.sort()
print(list) # [-65, -10, 0, 5, 35, 100]

list.sort(reverse=True)
print(list) # [100, 35, 5, 0, -10, -65]

l = [20, 30, 30, 40, 90]
print(l[1:3]) # [30, 30]

l = [20, 30, 30, 40, 90]
print(l[::-1]) # [90, 40, 30, 30, 20]
