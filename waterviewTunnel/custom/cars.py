class Car:
    # Represents a recording rule from csv
    license, entryTime, exitTime, duration, speed, fine = '', '', '', '', '', ''

    def __init__(self, licence, entryTime, exitTime, duration, speed, fine):
        self.license = licence
        self.entryTime = entryTime
        self.exitTime = exitTime
        self.duration = duration
        self.speed = speed
        self.fine = fine

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
