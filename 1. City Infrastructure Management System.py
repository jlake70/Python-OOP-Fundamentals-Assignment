# Task 1

class Vehicle:
    def __init__(self, registration_number, vehicle_type, owner):
        self.registration_number = registration_number
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The owner of vehicle {self.registration_number} has been updated to {self.owner}.")


vehicle1 = Vehicle("RED123", "Car", "Alice")
vehicle2 = Vehicle("BLUE789", "Motorcycle", "Bob")
vehicle3 = Vehicle("GREEN456", "Truck", "Charlie")


print(f"Vehicle 1 owner: {vehicle1.owner}")
print(f"Vehicle 2 owner: {vehicle2.owner}")
print(f"Vehicle 3 owner: {vehicle3.owner}")


vehicle1.update_owner("Josh")
vehicle2.update_owner("Mayling")
vehicle3.update_owner("Nate")


print(f"Vehicle 1 new owner: {vehicle1.owner}")
print(f"Vehicle 2 new owner: {vehicle2.owner}")
print(f"Vehicle 3 new owner: {vehicle3.owner}")



