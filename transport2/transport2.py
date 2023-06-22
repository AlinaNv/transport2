#coding=windows-1251
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
            return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity=50) 
  #вот эту строку честно подсмотрела, без этого super() ничего не получалось

Autobus2=Autobus('Renaul Logan',180,12)
print(Autobus2.seating_capacity())

