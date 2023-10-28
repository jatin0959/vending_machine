class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy_req(self, req_items, money):
        if req_items > self.num_items:
            raise ValueError("Not enough Items in the machine")

        total_cost = req_items * self.item_price
        if money < total_cost:
            raise ValueError("Not enough coins")

        self.num_items -= req_items
        change = money - total_cost
        return int(change)


# Read num_items and item_price
num_items, item_price = map(int, input().split())

# Initialize VendingMachine with user-provided values
vm = VendingMachine(num_items=num_items, item_price=item_price)

# Read the number of operations
num_operations = int(input())

for _ in range(num_operations):
    try:
        req_items, money = map(int, input().split())
        change = vm.buy_req(req_items=req_items, money=money)
        print(f"Change: {change} coins")
    except ValueError as e:
        print(str(e))
