
def multiply(n, m):
    result = 0

    for i in range(m):
        result += n

    return result


def powers(n, m):
    result = n
    if m == 0:
        return 1

    for num in range(m-1):
        result = multiply(result, n)

    return result


x = int(input("please introduce the base"))
y = int(input("please introduce the power"))
print(powers(x, y))
