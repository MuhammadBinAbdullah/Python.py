class Robot:
    
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello Muhammad! My internal systems are fixed. My name is {self.name}.")

robot1 = Robot("Tom")
robot2 = Robot("Jerry")

print("Fixing and Launching Robots")
robot1.introduce()
robot2.introduce()
