'''
https://blog.bitsrc.io/keep-it-simple-with-the-strategy-design-pattern-c36a14c985e9
'''

from abc import ABC, abstractmethod

class AuthStrategy(ABC):
    @abstractmethod
    def auth(self):
        pass

class Basic(AuthStrategy):
    def auth(self):
        print("with basic auth")

class OAuth(AuthStrategy):
    def auth(self):
        print("with oauth")

class OpenId(AuthStrategy):
    def auth(self):
        print("with openid")

class AuthProgram:
    def __init__(self, strategy=Basic()):
        self.__strategy = strategy
    
    def set_strategy(self, strategy):
        self.__strategy = strategy
    
    def authenticate(self):
        self.__strategy.auth() # see, this context does not need to know the implementation

if __name__ == "__main__":
    ap = AuthProgram(OpenId())
    ap.authenticate()
    