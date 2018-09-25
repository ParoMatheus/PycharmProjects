string = ""
lives = 3
while True:

    try:
        command = input("Give me a command:    ").capitalize()
        if command not in ["S","N","W","E"]:
            print("input not allowed, try again")
            continue
        print(command," registered")
    except:
        print("Something went wrong")
    string += command.capitalize()
    if len(string)%10 == 0:
        print("you have lost a life, time is running out")
        lives-=1
    if lives == 0:
        print("You have lost")
        break
    if string.__contains__("SSNWES"):
        print("you won in %s" % (len(string)))
        break
