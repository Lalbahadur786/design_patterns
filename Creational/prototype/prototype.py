import copy

# Base prototype class
class Prototype:
    def clone(self):
        return copy.deepcopy(self)

# Vehicle prototype class
class Vehicle(Prototype):
    def __init__(self, _type, brand, engine, features):
        self.engine = engine
        self._type = _type
        self.brand = brand
        self.features = features or []
    
    def __str__(self):
        return f"Vehicle(_type={self._type}, brand={self.brand}, engine={self.engine}, features={self.features})"

# Client code
if __name__ == "__main__":
    # First creation of object
    base_suv = Vehicle("Mahindra SUV", "Mahindra", "1850 HP GTX", ["parking camera", "AC", "Music"])
    print(f"original prototype: \n {base_suv} \n")

    # Customizing for the customer 1
    customize_suv1 = base_suv.clone()
    customize_suv1.features.append("Leather seats")
    print(f"cloned and customize for customer 1: \n {customize_suv1} \n")

    # Customizing for the customer 2
    customize_suv2 = base_suv.clone()
    customize_suv2.engine = "2000 HP GTG"
    customize_suv2.features.append("Solar roof")
    print(f"cloned and customize for customer 2: \n {customize_suv2} \n")
