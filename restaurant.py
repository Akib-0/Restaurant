class Restaurant:
    def __init__(self,name,rent,menu=[]) -> None:
        self.name = name
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self,employee_type,employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee
    
    def add_order(self,order):
        self.orders.append(order)

    def receive_payment(self,order,amount,customer):
        if order.bill <= amount:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('Not enough money')
        
    def pay_expense(self,amount,despriction):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {despriction}')
        else:
            print(f'NOt enough money to pay {amount}')

    def pay_salary(self,employee):
        print(f'$$$$$   paying salary for {employee.name}, amount: {employee.salary}')
        if employee.salary <self.balance:
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receive_salary()
        else:
            print("Not enough money")

    def show_employees(self):
        print(f'.......SHOWING EMPLOYEES........')
        if self.chef is not None:
            print(f'Chef: {self.chef.name}, salary: {self.chef.salary}')
        if self.server is None:
            print("Blehhhhh")
        else:
            print(f'Server: {self.server.name}, salary: {self.server.salary}')
            
        
        
