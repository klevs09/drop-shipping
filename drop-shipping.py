import time

# Sample product catalog (Product Name: [Supplier Price, Selling Price])
products = {
    "Phone Case": [5, 15],
    "Wireless Earbuds": [20, 50],
    "Smartwatch": [30, 80],
    "LED Strip Lights": [10, 25],
    "Gaming Mouse": [15, 40]
}

# Function to display products
def show_products():
    print("\n📦 Available Products:")
    print("-" * 40)
    for index, (product, prices) in enumerate(products.items(), start=1):
        print(f"{index}. {product} - ${prices[1]}")  # Showing only selling price
    print("-" * 40)

# Function to process an order
def place_order():
    show_products()
    
    choice = input("\nEnter the product name you want to buy: ").strip()
    
    if choice in products:
        supplier_price, selling_price = products[choice]
        print(f"\n✅ {choice} added to cart! Selling Price: ${selling_price}")
        
        quantity = int(input("Enter quantity: "))
        total_price = selling_price * quantity
        
        print(f"\n🛒 Order Summary: {quantity} x {choice} = ${total_price}")
        
        confirm = input("\nConfirm order? (yes/no): ").strip().lower()
        if confirm == "yes":
            process_supplier_order(choice, quantity, supplier_price)
        else:
            print("❌ Order canceled.")
    else:
        print("⚠️ Product not found. Try again!")

# Function to simulate order fulfillment by the supplier
def process_supplier_order(product, quantity, supplier_price):
    print("\n📩 Sending order to supplier...")
    time.sleep(2)  # Simulating processing time
    total_cost = supplier_price * quantity
    print(f"\n✅ Supplier confirmed order. Cost: ${total_cost}")
    
    print("\n📦 Shipping product to customer...")
    time.sleep(2)  # Simulating shipping time
    print(f"\n🎉 Order for {quantity} x {product} has been shipped to the customer!")

# Run the dropshipping program
def run_dropshipping_store():
    print("🚀 Welcome to the Simple Dropshipping Store!")
    while True:
        print("\nOptions:")
        print("1. View Products")
        print("2. Place an Order")
        print("3. Exit")
        
        option = input("\nEnter your choice: ").strip()
        if option == "1":
            show_products()
        elif option == "2":
            place_order()
        elif option == "3":
            print("👋 Thank you for visiting! Exiting...")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

# Start the program
run_dropshipping_store()
