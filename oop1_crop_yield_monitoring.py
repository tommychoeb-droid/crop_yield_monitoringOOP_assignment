"""
OOP1 Assignment
Crop Yield Monitoring System

Domain: Agriculture
Demonstrates:
- Two classes
- Attributes and objects
- Instance methods
- A class method
- One Python data structure: list
- Searching/displaying records
- Object interaction
"""


class Crop:
    """Represents a crop record."""

    def __init__(self, crop_id, farmer_name, crop_type, area_hectares,
                 expected_yield_kg, actual_yield_kg=0):
        self.crop_id = crop_id
        self.farmer_name = farmer_name
        self.crop_type = crop_type
        self.area_hectares = area_hectares
        self.expected_yield_kg = expected_yield_kg
        self.actual_yield_kg = actual_yield_kg

    @classmethod
    def create_from_input(cls):
        """Create a Crop object using information entered by the user."""
        print("\n--- Add New Crop ---")
        crop_id = input("Crop ID: ").strip()
        farmer_name = input("Farmer name: ").strip()
        crop_type = input("Crop type: ").strip()
        area_hectares = float(input("Farm area (hectares): "))
        expected_yield_kg = float(input("Expected yield (kg): "))
        actual_yield_kg = float(input("Actual yield (kg, enter 0 if unknown): "))

        return cls(
            crop_id,
            farmer_name,
            crop_type,
            area_hectares,
            expected_yield_kg,
            actual_yield_kg
        )

    def calculate_yield_difference(self):
        """Return the difference between actual and expected yield."""
        return self.actual_yield_kg - self.expected_yield_kg

    def yield_status(self):
        """Return a simple status based on actual versus expected yield."""
        if self.actual_yield_kg == 0:
            return "Not recorded"
        if self.actual_yield_kg >= self.expected_yield_kg:
            return "Target met"
        return "Below target"

    def display_info(self):
        """Display this crop's information."""
        difference = self.calculate_yield_difference()

        print(f"\nCrop ID: {self.crop_id}")
        print(f"Farmer: {self.farmer_name}")
        print(f"Crop type: {self.crop_type}")
        print(f"Area: {self.area_hectares:.2f} hectares")
        print(f"Expected yield: {self.expected_yield_kg:.2f} kg")
        print(f"Actual yield: {self.actual_yield_kg:.2f} kg")
        print(f"Yield difference: {difference:+.2f} kg")
        print(f"Status: {self.yield_status()}")


class CropYieldMonitor:
    """Manages crop records."""

    def __init__(self):
        # The assignment requires only one data structure.
        self.crops = []

    def add_crop(self, crop):
        """Add a Crop object to the list."""
        self.crops.append(crop)

    def search_crop(self, crop_id):
        """Search the list for a crop using its ID."""
        for crop in self.crops:
            if crop.crop_id.lower() == crop_id.lower():
                return crop
        return None

    def display_all(self):
        """Display all stored crop records."""
        if not self.crops:
            print("\nNo crop records available.")
            return

        print("\n========== ALL CROP RECORDS ==========")
        for crop in self.crops:
            crop.display_info()
            print("-" * 38)

    def search_and_display(self, crop_id):
        """Search for a record and display it if found."""
        crop = self.search_crop(crop_id)

        if crop is None:
            print(f"\nNo crop record found for ID: {crop_id}")
        else:
            print("\n========== SEARCH RESULT ==========")
            crop.display_info()


def show_menu():
    """Display the program menu."""
    print("\n======================================")
    print("      CROP YIELD MONITORING SYSTEM")
    print("======================================")
    print("1. Add crop record")
    print("2. View all crop records")
    print("3. Search for a crop")
    print("4. Exit")


def main():
    """Run the Crop Yield Monitoring System."""
    monitor = CropYieldMonitor()

    # Creating initial Crop objects and demonstrating object interaction.
    crop1 = Crop("C001", "Musa Kamara", "Rice", 2.5, 5000, 4700)
    crop2 = Crop("C002", "Abdul Sesay", "Cassava", 1.8, 3500, 3800)

    monitor.add_crop(crop1)
    monitor.add_crop(crop2)

    print("Welcome to the Crop Yield Monitoring System.")
    print("Two sample crop objects have been loaded for demonstration.")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                new_crop = Crop.create_from_input()
                monitor.add_crop(new_crop)
                print("\nCrop record added successfully.")
            except ValueError:
                print("\nInvalid numeric input. Please try again.")

        elif choice == "2":
            monitor.display_all()

        elif choice == "3":
            crop_id = input("Enter crop ID to search: ").strip()
            monitor.search_and_display(crop_id)

        elif choice == "4":
            print("\nThank you for using the Crop Yield Monitoring System.")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
