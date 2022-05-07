cmd = input("to start press enter to exit press U")
print("hi welcome to duke the best car game")
name = input("enter name >>")
print(f"your name is {name}")
print("to get familiar with controls type 'help' or 'HELP' ")
print(f"there are a heck a lot of things you can do with your car{name}"
      f" lets "
      f"get going")
while cmd.upper != "U":
    started = False

    command = str(input("> ")).upper()
    if command.upper() == 'HELP':
        print('''to enter the car press f 
     to leave the car press f again
     to start the car press e
     to stop the car press q
     to move forward press w
     to move backwards press s
     to turn right press d 
    to turn left press a
    to quit the game press u''')
    inside_car = False
    if str(command.upper()) == "F":
        if inside_car:
            print("left the car")
            inside_car = False
        else:
            print("entered the car")
            inside_car = True
    if str(command.upper()) == "W":
        print("moved forward")
    if str(command.upper()) == "S":
        print("moved backwards")
    if str(command.upper()) == "E":
        if started:
            print("car already started")
        else:
            print("started the car")
            started = True
    if str(command.upper()) == "D":
        print("turned right")
    if str(command.upper()) == "L":
        print("turned left")
    if command.upper() == "Q":
        if started == True:
            print("car stopped")
            started = False
        else:
            print("car already stopped")
    if str(command.upper()) == "A":
        print("turned left")
    if str(command.upper()) == "U":
        print("exited the game")
        break
    else:
        print("unable to process invalid input")
