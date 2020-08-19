'''
https://en.wikipedia.org/wiki/State_pattern

this example implements this FSM:

state 1: lower case
state 2: upper case

1 ---> 2
^      |
|      |
|------|

'''

from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def write_name(self, context, name: str):
        pass

class LowerCaseState(State):
    def write_name(self, context, name: str):
        print(name.lower())
        context.set_state(MultipleUpperCaseState())

class MultipleUpperCaseState(State):
    def write_name(self, context, name: str):
        print(name.upper())
        context.set_state(LowerCaseState())

class StateContext:
    def __init__(self):
        self.__state = LowerCaseState()
    
    def set_state(self, state):
        self.__state = state
    
    def write_name(self, name):
        self.__state.write_name(self, name)

if __name__ == "__main__":
    context = StateContext()

    context.write_name("Monday")
    context.write_name("Tuesday")
    context.write_name("Wednesday")
    context.write_name("Thursday")
    context.write_name("Friday")
    context.write_name("Saturday")
    context.write_name("Sunday")
