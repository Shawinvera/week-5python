class Smartphone:
    def __init__(self, brand, model, battery_life, price):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # Battery life in hours
        self.price = price  # Price in USD

    def make_call(self, phone_number):
        print(f"Making a call to {phone_number}...")

    def send_message(self, phone_number, message):
        print(f"Sending message to {phone_number}: {message}")

    def charge(self):
        print(f"Charging {self.brand} {self.model}...")
        self.battery_life = 100  # Fully charged
        print(f"{self.brand} {self.model} is now fully charged!")
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, price, gpu_type, ram_size):
        super().__init__(brand, model, battery_life, price)  # Calling the parent constructor
        self.gpu_type = gpu_type  # Type of the GPU
        self.ram_size = ram_size  # RAM size in GB

    def start_game(self, game_name):
        print(f"Starting {game_name} on {self.brand} {self.model}...")
    
    # Overriding the make_call method to demonstrate polymorphism
    def make_call(self, phone_number):
        print(f"Gaming phone cannot make calls in Gaming Mode. Switch to normal mode to call.")
# Creating a regular Smartphone object
regular_phone = Smartphone("Apple", "iPhone 14", 20, 999)

# Creating a Gaming Smartphone object
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 18, 799, "Adreno 650", 16)

# Calling methods on the regular smartphone
regular_phone.make_call("123-456-7890")
regular_phone.send_message("123-456-7890", "Hello, how are you?")
regular_phone.charge()

# Calling methods on the gaming smartphone
gaming_phone.make_call("987-654-3210")
gaming_phone.send_message("987-654-3210", "Let's game tonight!")
gaming_phone.start_game("PUBG Mobile")
gaming_phone.charge()
