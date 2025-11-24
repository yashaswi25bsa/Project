# Crop Profit Calculator

crops = {}  # store crop data

def add_crop():
    name = input("Enter crop name: ")
    cost = float(input("Enter total cost of seeds: "))
    yield_amount = float(input("Enter expected yield (kg/units): "))
    price_per_unit = float(input("Enter selling price per unit: "))
    crops[name] = {
        "cost": cost,
        "yield": yield_amount,
        "price": price_per_unit
    }
    print(f"{name} added successfully!")

def calculate_profit():
    if not crops:
        print("No crops added yet.")
        return
    for name, data in crops.items():
        revenue = data["yield"] * data["price"]
        profit = revenue - data["cost"]
        print(f"\n{name}:")
        print(f"  Revenue: ${revenue:.2f}")
        print(f"  Cost: ${data['cost']:.2f}")
        print(f"  Profit: ${profit:.2f}")

def view_crops():
    if not crops:
        print("No crops added yet.")
        return
    print("\nCrop Summary:")
    for name, data in crops.items():
        print(f"- {name}: Yield={data['yield']} units, Selling Price=${data['price']} per unit")

def main():
    while True:
        print("\n--- Crop Profit Calculator ---")
        print("1. Add Crop")
        print("2. View Crops")
        print("3. Calculate Profit")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_crop()
        elif choice == "2":
            view_crops()
        elif choice == "3":
            calculate_profit()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()