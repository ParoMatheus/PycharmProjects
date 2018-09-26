def check(a,b):
    if a > b:
        return False
    else:
        return a

expression = input("Please enter a String")
words= []
word=  ""

for letter in range(0,len(expression)-1):
    x = check(expression[letter],expression[letter+1])
    if(x==False and word != ""):
        word+= expression[letter]
        words.append(word)
        word=""

    if(letter == (len(expression)-2) and word!= ""):
        word += expression[letter]
        word += expression[letter+1]
        words.append(word)
    elif (x != False):
            word += x

l = words[0]

for n in range(0,len(words)-1):
    if len(words[n]) >= len(words[n+1]):
        l = words[n]
    else:
        l = words[n+1]
        continue
print(l)
##This took long