file = open("text.txt")
alphabet = " abcdefghijklmnopqrstuvwxyz"
vowels = ["a","e","o","i","u"]
number = 0;
end = ""
for line in file:
    for letters in line:
        if letters in vowels:
            number = number + 1
    else:
        end = end + alphabet[number]
        number = 0

print(end)