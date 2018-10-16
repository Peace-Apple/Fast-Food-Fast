"""
Module to handle data storage
"""

import psycopg2


class DatabaseConnection:

    def __init__(self):

            self.connection = psycopg2.connect(database="fastfoodfast", user="postgres", password="apple123",
                                               host="127.0.0.1", port="5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

    def create_tables(self):
        """
        This method creates tables one after the other in the database after the connection has been established.

        """

        commands = (
            """
            CREATE TABLE IF NOT EXISTS "users" (
                    user_id SERIAL NOT NULL PRIMARY KEY,
                    user_name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    phone_number VARCHAR(255) NOT NULL,
                    user_type VARCHAR(100) DEFAULT 'FALSE',
                    password VARCHAR(255) NOT NULL
                  
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "menu" (
                    item_id SERIAL NOT NULL PRIMARY KEY, 
                    item_name VARCHAR(50) NOT NULL, 
                    user_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES "users" (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
                    
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "orders" (
                    order_id SERIAL NOT NULL PRIMARY KEY, 
                    user_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES "users" (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                    item_id INTEGER NOT NULL,
                    FOREIGN KEY (item_id) REFERENCES "menu" (item_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                    order_item VARCHAR(255) NOT NULL, 
                    order_status VARCHAR(255) NOT NULL DEFAULT 'New',
                    quantity INTEGER NOT NULL,
                    order_date TIMESTAMP DEFAULT NOW() NOT NULL
                    )
            """
        )

        try:
            for command in commands:
                self.cursor.execute(command)
            self.connection.commit()
            self.cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.connection is not None:
                self.connection.close()

    def insert_user(self, user_name, email, phone_number, password):
        """
        insert user details into the table users
        :param user_name:
        :param email:
        :param phone_number:
        :param password:
        :return:
        """
        add_user = """INSERT INTO users (user_name, email, phone_number, password)
                   VALUES ('{0}', '{1}', '{2}', '{3}');""".format(user_name, email, phone_number, password)
        self.cursor.execute(add_user)
        return True

    def insert_order(self, order_item, quantity, user_id, item_id):
        """
        insert order details into the table orders
        :param order_item:
        :param quantity:
        :param user_id:
        :param item_id:
        :return:
        """
        add_order = """INSERT INTO orders (order_item, quantity, user_id, item_id)
                    VALUES ('{0}', '{1}', '{2}', '{3}');""".format(order_item, quantity, user_id, item_id)
        self.cursor.execute(add_order)
        return True

    def insert_menu_item(self, item_name, user_id):
        """
        insert menu details into the table menu
        :param item_name:
        :param user_id:
        :return:
        """
        add_item = "INSERT INTO menu (item_name, user_id) VALUES ('"+item_name+"', '"+user_id+"');"
        self.cursor.execute(add_item)
        return True

    def find_user_by_username(self, user_name):
        """
        find a specific user given a user name
        :return:
        :param user_name:
        :return:
        """

        name = "SELECT * FROM users WHERE user_name ='{}'".format(user_name)
        self.cursor.execute(name)
        check_username = self.cursor.fetchone()
        return check_username

    def find_user_by_email(self, email):
        """
        find a specific user given an email
        :param email:
        :return:
        """
        email = "SELECT * FROM users WHERE email = '{}'".format(email)
        self.cursor.execute(email)
        check_email = self.cursor.fetchone()
        return check_email

    def get_menu_items(self):
        """
        get all menu items from the menu table
        :return:
        """
        menu_items = "SELECT * FROM menu;"
        self.cursor.execute(menu_items)
        menu = self.cursor.fetchall()
        return menu

    def get_all_orders(self):
        """
        get all orders from the orders table
        :return:
        """
        all_orders = "SELECT * FROM orders;"
        self.cursor.execute(all_orders)
        orders = self.cursor.fetchall()
        return orders

    def get_a_specific_order(self, order_id):
        """
        get a specific order from the orders table using the order_id
        :param order_id:
        :return:
        """
        one = """SELECT * FROM orders WHERE order_id = '{}';""".format(order_id)
        self.cursor.execute(one)
        order = self.cursor.fetchone()
        return order

    def find_item_by_name(self, order_item):
        """
        Find a specific item given it's name
        :param order_item:
        :return:
        """
        item = """SELECT * FROM menu WHERE item_name ='{}';""".format(order_item)
        self.cursor.execute(item)
        check_item = self.cursor.fetchone()
        return check_item

    def update_order(self, order_status, order_id):
        """
        get a specific order using order_id and update order_status
        :param order_status:
        :param order_id:
        :return:
        """
        update = """UPDATE orders SET order_status = '{}' WHERE order_id = '{}';""".format(order_status, order_id)
        self.cursor.execute(update)

    def get_order_history(self, user_id):
        """
        get the order history for a user from the orders table using the user_id
        :param user_id:
        :return:
        """
        hist = """SELECT * FROM orders WHERE user_id ='{}';""".format(user_id)
        self.cursor.execute(hist)
        get_history = self.cursor.fetchall()
        return get_history

    def check_admin(self):
        """
        method to set user_type to true which gives a user admin privileges
        :return:
        """
        self.cursor.execute("UPDATE users SET user_type = 'TRUE' WHERE user_id = 3")


DatabaseConnection().create_tables()










