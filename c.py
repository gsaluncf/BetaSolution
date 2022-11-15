class Car:

    def __init__(self, speed=0):  # initialize function, sets all the variables up and equal to zero
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):  # function to declare the speed of the car
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):  # function to raise the speed of the car
        self.speed += 5

    def brake(self):  # function to reduce the speed of the car
        if self.speed < 5:  # make sure the speed never goes under 0
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):  # function to keep track of how far the car has gone. adds the current speed to the odometer every time the car is updated
        self.odometer += self.speed
        self.time += 1  # keep track of how long the program has been running for

    def average_speed(self):  # function to calculate the average speed
        if self.time != 0:
            return self.odometer / self.time  # use the time to calculate the average. clever!
        else:  # make sure that average speed is only being calculated when the car has moved
            pass

    def goto_mechanic(self):
        pass


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:  # loop that goes on forever
        action = input("What should I do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, show average [S]peed?, or [Q]uit?").upper()  # print the options for hte player
        if action not in "ABOSQ" or len(
                action) != 1:  # make sure that the input is something the computer can understand (not sure why we do this before the  chain of if's. seems like you could add an else at the end of the ifs and it would work just as well
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()  # call the functions from earlier
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        elif action == 'Q':
            quit()  # quite ends the program
        my_car.step()  # after actions take the step to update the car's odometer
        my_car.say_state()  # update the text box after having done whatever action
