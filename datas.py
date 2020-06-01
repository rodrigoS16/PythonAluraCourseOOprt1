
class Data:
    default_Data = "1900/01/01"  # declaração de atributo estatico

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def formaData(self):
        print("{:02d}/{:02d}/{:04d}".format(self.day, self.month, self.year))