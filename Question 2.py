class CarTrade:
    def __init__(self):
        self.car_year = 0
        self.car_make = 'none'
        self.car_model = 'none'

    def getString(self, car_year, car_make, car_model):
        self.car_year = car_year
        self.car_make = car_make
        self.car_model = car_model

        if self.car_year >= 2020:
            print('WOW! Your {} {} {} is practically new. Expect the best offers.'.format(self.car_year, self.car_make.upper(), self.car_model.upper()))
        elif self.car_year in range(2014, 2019):
            print('Your {} {} {} can be traded.'.format(self.car_year, self.car_make.upper(), self.car_model.upper()))
        elif self.car_year in range(2010, 2013):
            print("Your {} {} {} can be traded, but you won't get much for it.".format(self.car_year, self.car_make.upper(), self.car_model.upper()))
        elif self.car_year <= 2013:
            print("Unfortunately, we cannot accept your {} {} {}. It's too old to be traded.".format(self.car_year, self.car_make.upper(), self.car_model.upper()))

    def printString(self):
        lead = "Your car's information: "
        print("\n{} {} {} {}".format(lead.upper(), self.car_year, self.car_make.upper(), self.car_model.upper()))


if __name__ == "__main__":
    car = CarTrade()

    car_year = int(input("Car year?\n"))
    car_make = input("Car make?\n")
    car_model = input("Car model?\n")

    car.getString(car_year, car_make, car_model)
    car.printString()