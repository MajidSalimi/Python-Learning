from builtins import ValueError
while 1:
    try:
        name=int(input('Please Enter a Number:'))
        break
    except ValueError:
        print("Invalid input")






