x = int(input("First number?"))

y = int(input("Second number?"))

if x<0 or y<0:
    z = int((-1)*(abs(x) - 1) // abs(y)) + True
else:
    z = int((x-1)//y)+True

print(z)
