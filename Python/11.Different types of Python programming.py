#Traditional functional programming
age = [1,2,3,4,]
i = 0
for e in age:
    age[i] = e + 10
    i = i + 1
print(age)

#Convert above traditional functional programming to better in python
age = [1,2,3,4,]
#i = 0
for i,e in enumerate(age):
    age[i] = e + 10
print(age)

#Convert above traditional functional programming to MOST EFFICIENT in python by using
#map is more effective, scalable and parallel process mechanism
#Use map object instead of for loop
age = [1,2,3,4,]
weight = [5,10,15,20]
def incr(e, f):
    return e+f+10
#age = map(incr, age)
#print(age) #This returns an object.

total = list(map(incr, age, weight)) #Let's convert this object to list for display purpose
print(total)

#Let us write even shorter code Using lambda
#Lambda is anonymous function/in-line funtion
#Note that lambda is used only when you don't want to re-use the function and just at one place.
age = [1,2,3,4,]
i = 0
age = list(map(lambda e:e+10, age)) #labda is replacing incr function here.
print(age)