from menu import Pizza, Burger, Drinks, Menu
from restaurant import Restaurant
from concept import Chef, Customer, Server, Manager
from order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki',600,'large', ['shutki','onions'])
    menu.add_menu_item('pizza',pizza_1)    
    pizza_2 = Pizza('Alur vorta pizza', 400, 'small', ['alu','ble'])
    menu.add_menu_item('pizza',pizza_2)    

    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bleh','ble'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('Beef Burger',1200,'Beef', ['beef','kella'])
    menu.add_menu_item('burger',burger_2)

    coke = Drinks('Coke',30,True)
    menu.add_menu_item('drinks',coke)

    menu.show_menu()

    restaurant = Restaurant('Food Fusion', 1000)

    manager = Manager('Chan Mia',23,'chan@','Kazipara',1500,'Jan 1 2010','core')
    restaurant.add_employee('manager',manager)
    chef = Chef('Rustom',21,'chupa@','rustamNagr',3500,'Feb 1 2023', 'chef','everything')
    restaurant.add_employee('chef',chef)
    server = Server('Chotu',4,'nai@jai.com','restaurant',200,'March 1','server')
    restaurant.add_employee('server',server)

    #show employees
    #restaurant.show_employees()
    restaurant.show_employees()


    #customer_1 placing an order
    customer_1 = Customer('Shakib Khan', 123, 'kingkhan@', "banani", 10000)
    order_1 = Order(customer_1,[pizza_1,coke])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    #customer_1 paying for order_1
    restaurant.receive_payment(order_1,2000,customer_1)
    print(restaurant.revenue, restaurant.balance)

    customer_2 = Customer('Shakibal', 23, 'kkk@', "banani", 10000)
    order_2 = Order(customer_2,[burger_2,coke])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)

    #customer_1 paying for order_1
    restaurant.receive_payment(order_2,2000,customer_2)
    print("After second customer-- ", restaurant.revenue, restaurant.balance)
    # pay rent
    restaurant.pay_expense(restaurant.rent,'Rent')
    print('after rent ',restaurant.revenue,restaurant.balance,restaurant.expense)

    restaurant.pay_salary(restaurant.server)
    print('after saraly ',restaurant.revenue,restaurant.balance,restaurant.expense)





if __name__ == '__main__':
    main()
