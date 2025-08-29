# smartphone.py

class Smartphone:
    def __init__(self, brand, model, battery_level=100):
        # Attributes
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
    
    # Method: make a call
    def make_call(self, number):
        if self.battery_level > 0:
            print(f"{self.brand} {self.model} is calling {number} 📞")
            self.battery_level -= 5
        else:
            print("Battery too low to make a call ⚡")
    
    # Method: charge phone
    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"{self.brand} {self.model} charged to {self.battery_level}% 🔋")

# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 15")
    phone2 = Smartphone("Samsung", "Galaxy S24", battery_level=50)

    phone1.make_call("0740027395")
    phone2.charge(30)

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_level=100, cooling_system=True):
        super().__init__(brand, model, battery_level)
        self.cooling_system = cooling_system
    
    def play_game(self, game):
        if self.battery_level >= 10:
            print(f"{self.brand} {self.model} is playing {game} 🎮")
            self.battery_level -= 10
        else:
            print("Battery too low to play a game ⚡")
          
