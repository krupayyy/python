# Create a class called counter which stores a counter and provides methods to increment, decrement, reset and return counter
# Class
class counter:
# Object attributes
    def __init__(self,counter1 = 0):
        self.counter1 = counter1
 # Methods
    def increment(self,inccounter):
      self.counter1 += inccounter
    def decrement(self,decounter):
      self.counter1 -= decounter
    def reset(self):
      self.counter1 = 0
    def  getcounter(self):
        return self.counter1

venubadpapacounter = counter(0)
krupa = counter()
krupa.increment(5)
krupa.increment(10)
krupa.decrement(6)
venubadpapacounter.decrement(4)
venubadpapacounter.reset()
print(krupa.getcounter())
print(venubadpapacounter.getcounter())




