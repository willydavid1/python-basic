name = 'willy'

print(name.upper())
print(name.capitalize())
print(name.strip())
print(name.lower())
print(name.replace('y', 'i'))
print(name[0])
print(len(name))

print(name[0:3]) # 'wil'
print(name[:3]) # 'wil'
print(name[3:]) # 'ly'
print(name[1:4]) # 'ill'
print(name[1:4:2]) # 'il' / access the letters two by two
print(name[::]) # 'willy'
print(name[::2]) # 'wly'
print(name[::-1]) # 'ylliw'

