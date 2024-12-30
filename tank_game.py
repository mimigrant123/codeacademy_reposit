import random
from random import randint


class TankGame:
    def __init__(self, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        # Hard-coded starting tank location is 2, 1
        self.tank_loc_x = 2
        self.tank_loc_y = 1
        # Starting direction: tank facing north/up
        self.direction = "up"
        self.num_of_shots = 0
        self.shots_in_directions = {"left": 0, "right": 0, "up": 0, "down": 0}
        self.target_loc_x = randint(0, N)
        self.target_loc_y = randint(0, N)
        self.hit_count = 0
        while self.tank_loc_x == self.target_loc_x and self.tank_loc_y == self.target_loc_y:
            self.target_loc_x = randint(0, N)
            self.target_loc_y = randint(0, N)





    def print_map(self):
        """Print the current map of the game.

        Example output for a 7x7 map:
           0  1  2  3  4  5  6
        0  .  .  .  .  .  .  .
        1  .  .  T  .  .  .  .
        2  .  .  .  .  .  .  .
        3  .  .  .  .  .  .  .
        4  .  .  .  .  .  .  .
        5  .  .  .  .  .  .  .
        6  .  .  .  .  .  .  .

        where T is the location of the tank,
        where . (the dot) is an empty space on the map,
        where the horizontal axis is the x location of the tank and,
        where the vertical axis is the y location of the tank.
        """
        # Print the numbers for the x axis
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            # Print the numbers for the y axis
            print(f"{i} ", end="")
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(" T ", end="")
                elif self.target_loc_x == j and self.target_loc_y == i:
                    print(" o ", end="")
                else:
                    print(" . ", end="")

            print()

    def steer_left(self):
        if self.direction == "up":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "up"

    def steer_right(self):
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "up"

    def forward(self):
        if self.direction == "up":
            self.tank_loc_y -= 1
        elif self.direction == "right":
            self.tank_loc_x += 1
        elif self.direction == "down":
            self.tank_loc_y += 1
        elif self.direction == "left":
            self.tank_loc_x -= 1

    def backward(self):
        if self.direction == "up":
            self.tank_loc_y += 1
        elif self.direction == "right":
            self.tank_loc_x -= 1
        elif self.direction == "down":
            self.tank_loc_y -= 1
        elif self.direction == "left":
            self.tank_loc_x += 1

    def shoot(self):
        self.num_of_shots += 1
        self.shots_in_directions[self.direction] += 1
        if self.direction == "up" and self.tank_loc_x == self.target_loc_x and self.tank_loc_y > self.target_loc_y:
            self.hit_count += 1
            print("Hit!")
            self.target_loc_x = randint(0, self.N)
            self.target_loc_y = randint(0, self.N)
        elif self.direction == "right" and self.tank_loc_y == self.target_loc_y and self.tank_loc_x < self.target_loc_x:
            self.hit_count += 1
            print("Hit!")
            self.target_loc_x = randint(0, self.N)
            self.target_loc_y = randint(0, self.N)
        elif self.direction == "down" and self.tank_loc_x == self.target_loc_x and self.tank_loc_y < self.target_loc_y:
            self.hit_count += 1
            print("Hit!")
            self.target_loc_x = randint(0, self.N)
            self.target_loc_y = randint(0, self.N)
        elif self.direction == "left" and self.tank_loc_y == self.target_loc_y and self.tank_loc_x > self.target_loc_x:
            self.hit_count += 1
            print("Hit!")
            self.target_loc_x = randint(0, self.N)
            self.target_loc_y = randint(0, self.N)


    def info(self):
        print(f"Direction: {self.direction}")
        print(f"Coordinates: {(self.tank_loc_x), self.tank_loc_y}")
        print(f"Number of shots: {self.num_of_shots}")
        print((f"Number of hits: {self.hit_count}"))
        print(f"Shots in directions: {self.shots_in_directions}")



if __name__ == "__main__":
    # Initialize your game object
    tg = TankGame()
    # Start game loop
    while True:
        tg.print_map()

        command = input("Input a command: ")
        if command == "left":
            tg.steer_left()
        elif command == "right":
            tg.steer_right()
        elif command == "info":
            tg.info()
        elif command == "forward":
            tg.forward()
        elif command == "backward":
            tg.backward()
        elif command == "shoot":
            tg.shoot()