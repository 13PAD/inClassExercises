class Car:
    # My program uses a custom class called car to help
    # easily manipulate the data and store it easily.
    def __init__(self, licence, entryTime, exitTime, duration, speed, fine):
        self.license = licence
        self.entryTime = entryTime
        self.exitTime = exitTime
        self.duration = duration
        self.speed = speed
        self.fine = fine
