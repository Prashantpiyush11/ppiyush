#Strings
name = "abcde"
namesq = 'xyz'
print(type(name))
print(type(namesq))

#access string content
print(name[0])
print(name[2:5])

#modify string content
name[0] = 'A' #Check this

name + 'xyz'
name = name + 'xyz'
print(name)
name = name.upper()
name = "mr"
name = name.capitalize()
print(name)

name = name.replace('AB','pq')
print(name)

isinstance(name, str) #True
isinstance(name, int) #False