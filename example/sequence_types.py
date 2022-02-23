ex_list = [1, 2, 5, 4, 1]
print(type(ex_list), '=', ex_list)
ex_tuple = (2, 1, 3, 1, 2)
print(type(ex_tuple), '=', ex_tuple)
ex_range = range(2, 12, 2)
print(type(ex_range), '=', ex_range)

'Common Operations'

n = 5
x, y, z = 1, 2, 3
s = [1, 2, 5, 4, 1]
t = ex_list

#in
x in s #True if an item of s is equal to x, else False

#not in
x not in s #False if an item of s is equal to x, else True

#list concatination
s + t #concatenation of s and t

#list multiplication
s * n #equivalent to adding s to itself n times

#indexing
s[z] #zth item of s, origin 0

#slicing
s[x:y] #slice of s from x to y
s[x:y:z] #slice of s from x to y with step z

#length
len(s) #length of s

#min and max
min(s) #smallest item of s
max(s) #largest item of s
#if strings, value is determined lexicographically

x, y, z = 1, 0, 1

#index of
s.index(x, y, z)
#index of the first occurrence of x in s
# (at or after index y and before index z)

#count
s.count(x) #total number of occurrences of x in s

'Mutable Sequence Type Operations'

i, j, k = 1, 2, 3
t = [1]

#replacement
s[i] = x #item i of s is replaced by x

#slice replacement
s[i:j] = t #slice of s from i to j is replaced by the contents of the interable t
s[i:j:k] = t #the elements of s[i:j:k] are replaced by those of t
	#t must have the same length as the slice it is replacing

#delete slice
del s[i:j] #same as s[i:j] = []

#append
s.append(x) #appends x to the end of the sequnce

#clear
s.clear() #removes all items from s, same as del s[:]

s = ex_list

#copy
s.copy() #creates a shallow copy of s, same as s[:]

#extend
s.extend(t)
s += t
	#extends s with the contents of t

#*=
s *= n #updates s with its contents repeated n time

#insert
s.insert(i, x) #inserts x into s at the index given by i

#pop
s.pop(i) #retrieves the item at i and also removes it from s
s.pop() #if no arg is given default to -1, the last item of the list

#remove
s.remove(x) #remove the first item from s where s[i] is equal to x

#reverse
s.reverse() #reverses the items of s in place