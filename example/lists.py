#lists can contain items of different types, but usually all have the same type
squares = [1, 4, 9, 16, 25]

#Lists can be indexed and sliced
print(squares[0] , squares[-1]) #first and last indexes
print(squares[2:]) #return a new list containing the requested elements

#Concatenation
squares = squares + [36, 49, 81, 100]

#Lists are mutable
cubes = [1, 8, 27, 65, 125]
print(cubes) #first version of cubes
cubes[3] = 64
print(cubes) #second version of cubes

#Nested list
nest = [[1,2,3], [2,4,6], [3,6,9]]
print(nest[0][0]) #index call