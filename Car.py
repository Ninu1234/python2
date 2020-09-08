class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.color = color
        self.company = company
        self.speedLimit = speedLimit
        self.model = model
    def start(self):
        print("started")
    def stop(self):
        print("stop")
    def accelerate(self):
        print("accelerating")
    def changegear(self):
        print("change The Gear")
Audi = Car("a6","white","Audi",150)
print(Audi.start())
print(Audi.color)