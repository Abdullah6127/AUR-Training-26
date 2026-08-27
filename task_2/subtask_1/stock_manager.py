import sys

def load_stock(filename):
    stock = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                element = line.split(",")
                if len(element) != 2:
                    raise Exception
                stock[element[0]] = int(element[1])
        return stock
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception:
        print(f"Error: File '{filename}' has a corrupted format.")
        sys.exit(1)

def get_key(input, keys):
    if input.isdigit():
        index = int(input) - 1
        if 0 <= index < len(keys):
            return keys[index]
        return None
    return input

def add_stock(stock):
    display_stock(stock)
    while True:
        item = input("Enter stock name or ID: ").lower().strip()
        if not item:
            print("Invalid input, try again.")
            continue
        item = get_key(item, list(stock.keys()))
        if item is None:
            print("Invalid input, try again.")
            continue
        break

    while True:
            try:
                amount = int(input("Enter the amount to be added: "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid input, enter an integer.")
                continue
            break
    
    if item in stock:
        stock[item] += amount
        print(f"Updated {item} stock to {stock[item]}.")
    else:
        stock[item] = amount
        print(f"Added new item '{item}' with stock {amount}.")

def remove_stock(stock):
    display_stock(stock)
    if not list(stock.keys()):
        return
    
    while True:
        item = input("Enter stock name or ID: ").lower().strip()
        item = get_key(item, list(stock.keys()))
        if not item or item not in stock:
            print("Invalid item, try again.")
            continue
        break
        
    while True:
            try:
                amount = int(input("Enter the amount to be removed: "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid input, enter an integer.")
                continue
            break    

    if stock[item] - amount < 0:
        print( f"Cannot remove {amount}. Current stock for {item} is only {stock[item]}.")
    else:
        stock[item] -= amount
        print(f"Updated {item} stock to {stock[item]}.")

    if stock[item] == 0:
        del stock[item]

def display_stock(stock):
    if not stock:
        print("\nStock is empty.\n")
        return
    print("\n----------- Stock -----------")
    for i, (item, count) in enumerate(stock.items()):
        print(f"{i+1}. {item}: {count}")
    print("-----------------------------\n")

def save_stock(filename, stock):
    try:
        with open(filename, "w") as f:
            for item, count in stock.items():
                f.write(f"{item},{count}\n")
        print("Stock saved successfully!")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    stock = load_stock("stock.txt")
    while True:
        print("=============== Stock Manager Menu ===============")
        print("1) Add Stock")
        print("2) Remove Stock")
        print("3) Show Stock's Content")
        print("4) Save & Quit")
        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            add_stock(stock)
        elif choice == "2":
            remove_stock(stock)
        elif choice == "3":
            display_stock(stock)
        elif choice == "4":
            save_stock("stock.txt", stock)
            print("Exiting program...")
            break
        else:
            print("Invalid option, try again.\n")

if __name__ == "__main__":
    main()