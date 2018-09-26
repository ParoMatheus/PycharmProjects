def check(a,b):
    if a > b:
        return False
    else:
        return True

name = input("Please enter a String")
dictionary = {}
words =[]
word = ""
for n in range(0,len(name)-1):
    x = check(name[n],name[n+1])
    dictionary["%s"%(n)] = x
array =[]
for a in dictionary:
    if dictionary["%s"%(a)] == True:
        array.append(a)
print(dictionary)
print(array)
for num in range(0,len(array)-1):
    if int(array[num])+1 == int(array[num+1]):
        word = word + name[int(int(array[num]))]
    else:
        if word != "":
            word = word + name[int(int(array[num]))]
            words.append(word)
        word = ""
        
print(words)
