'''
https://medium.com/datadriveninvestor/design-patterns-a-quick-guide-to-observer-pattern-d0622145d6c2

Subject: class FootballGame

'''

from abc import ABC, abstractmethod

class Observer(ABC):
    def __init__(self):
        self.excitement_level = 0

    @abstractmethod
    def update(self):
        pass

'''
This is the Subject that the Observer (Audience) observe
'''
class FootballGame:
    def __init__(self):
        self.__scored = False
        self.__audience = []
    
    '''
    audience register() to observe the game
    '''
    def register(self, audience: Observer):
        self.__audience.append(audience)

    def set_score(self, score: bool):
        self.__scored = score
        self.__notify()
    
    def __notify(self):
        for audience in self.__audience:
            audience.update()

class YoungAudience(Observer):
    def update(self):
        self.excitement_level += 1
        if self.excitement_level > 3:
            print("Young: it's more than 3! It's: ", self.excitement_level)
        else:
            print("Young: hmmm still ", self.excitement_level)

class OldAudience(Observer):
    def update(self):
        self.excitement_level += 1
        if self.excitement_level > 5:
            print("Old: this is it, more than 5! it's: ", self.excitement_level)
        else:
            print("Old: hmmmm still ", self.excitement_level)

if __name__ == "__main__":
    game = FootballGame()
    young_1 = YoungAudience()
    young_2 = YoungAudience()
    old_1 = OldAudience()
    game.register(young_1)
    game.register(young_2)
    game.register(old_1)

    for _ in range(7):
        game.set_score(True)
