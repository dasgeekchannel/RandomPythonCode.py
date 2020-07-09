while True:
    try:
        cinput = input("Enter your name: ")
        dinput = int(input("Enter your age: "))
    except ValueError:
        print("You need to enter a real number.")
    else:
        calc_inp = 100 - dinput
        print("Your name is,", cinput, "you are,", dinput, "years old", "you will be one hundred years old in just", calc_inp, "years!")
        break
