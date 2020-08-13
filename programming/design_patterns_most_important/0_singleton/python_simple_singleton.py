"""
https://refactoring.guru/design-patterns/singleton/python/example
"""

class SingletonMeta(type):
    _instance = None
    
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super.__call__(*args, **kwargs)
        return cls._instance

class Singleton(metaclass=SingletonMeta):
    def a_funcion(self):
        pass

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(s1 == s2)
