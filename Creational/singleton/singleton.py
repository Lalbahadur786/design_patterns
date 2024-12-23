"""
"""
# Singlton design pattern usefil in 
# Database connection management
# Logger
# Configuration management
# Caching and many more where central (global) point of control is required
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value):
        self.value = value

# Client code
if __name__ == "__main__":
    obj1 = Singleton("First Object")
    print(obj1.value)
    print("Trying to create another object of Singleton class")
    obj2 = Singleton("Second Object")
    print(obj2.value)
    print("Now accessing Object 1.")
    print(obj1.value)
    print("Are obj1 and obj2 the same instance?", obj1 is obj2)
