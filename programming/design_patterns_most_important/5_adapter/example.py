'''
educative.io
'''

from abc import ABC, abstractmethod

class Aircraft(ABC):
    @abstractmethod
    def fly(self):
        pass

class AirBalloon:
    def fly(self, gas: str):
        print(f"fly with gas: {gas}")

class Adapter(Aircraft):
    def __init__(self, airballoon: AirBalloon):
        self.balloon = airballoon
    
    def fly(self):
        self.balloon.fly("helium")

# client code
if __name__ == "__main__":
    balloon = AirBalloon()
    balloon_adapter = Adapter(balloon)
    balloon_adapter.fly()
