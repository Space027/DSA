class Car:
    def __init__(self,color,tspeed,brand,age,speed):
        self.color=color
        self.tspeed=int(tspeed)
        self.brand=brand
        self.age=int(age)
        self.speed=int(speed)
    def accelarate(self):
        if self.speed>self.tspeed-5:
            print("MAXIMUM SPEED REACHED!")
            self.speed=self.tspeed
        else:
            self.speed=self.speed+5
            print("CAR SPEED INCREASED. \nCURRENT SPEED",self.speed)
    def deccelarate(self):
        if self.speed<5:
            print("MINIMUM SPEED REACHED!")
            self.speed=0
        else:
            self.speed=self.speed-5
            print("CAR SPEED DECREASED. \nCURRENT SPEED",self.speed)
    def info(self):
        print("Your car is a",self.age,"year old "+self.color+" "+self.brand+" car with a top speed of",self.tspeed)

C1=Car('red',120,'Ford',12,100)
C1.info()


C2=Car('blue',300,'Ferrari',2,150)
C2.info()
for i in range(25):
    C2.deccelarate()

class Electric(Car):
    def __init__(self,color,tspeed,brand,age,speed,bcapacity):
        super().__init__(color,tspeed,brand,age,speed)
        self.bcapacity=int(bcapacity)
    def charging(self):
        self.bcapacity+=10
        print("CHARGING... \nCAPACITY CURRENTLY AT",self.bcapacity)

E1=Electric('white',250,'BYD',1,100,300)
E1.charging()
E1.deccelarate()
E1.deccelarate()

class Sport(Car):
    def __init__(self,color,tspeed,brand,age,speed,bcapacity,mode):
        super().__init__(color,tspeed,brand,age,speed)
        self.bcapacity=int(bcapacity)
        self.mode=mode
    def charging(self):
        self.bcapacity+=10
        print("CHARGING... \nCAPACITY CURRENTLY AT",self.bcapacity)
    def change_mode(self):
        if self.mode=='normal':
            print("NORMAL MODE")
            if self.speed>120:
                print("REDUCING SPEED")
                self.speed=120
                print("SPEED NOW",self.speed)
            else:
                print('NORMAL MODE ACTIVATED')
        if self.mode=='sport':
            print('SPORT MODE')
            if self.speed<120:
                print("INCREASING SPEED")
                self.speed+=50
                print("SPEED NOW",self.speed)
            else:
                print('SPEED MODE ACTIVATED')

S1=Sport('green',400,'Lamoghini',4,100,400,'sport')
S1.change_mode()

        