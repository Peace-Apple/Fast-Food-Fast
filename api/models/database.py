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
                    user_type VARCHAR(100) NOT NULL,
                    password VARCHAR(255) NOT NULL
                  
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "menu" (
                    item_id SERIAL NOT NULL PRIMARY KEY, 
                    item_name VARCHAR(50) NOT NULL, 
                    price INTEGER NOT NULL,
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


    def insert_user(self, user_name, email, phone_number, password, user_type):
        add_user = "INSERT INTO users (user_name, email, phone_number, password, user_type)" \
                   " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(user_name, email, phone_number, password, user_type)
        self.cursor.execute(add_user)


    def insert_order(self, user_id, item_id ):
        add_order = "INSERT INTO orders (user_id, item_id)"\
                    "VALUES ('{0}','{1}')".format(user_id, item_id)
        self.cursor.execute(add_order)


    def insert_menu_item(self, user_id, item_name):
        add_item = "INSERT INTO menu (user_id, item_name)"\
                    "VALUES ('{0}', '{1}')" .format(user_id, item_name)
        self.cursor.execute(add_item)

    def get_all_users(self):
        all_users = "SELECT * FROM users;"
        self.cursor.execute(all_users)
        users = self.cursor.fetchall()
        return users

    def get_a_specific_user(self, user_id):
        specific_user = "SELECT * FROM users WHERE user_name = '{}'".format(user_id)
        self.cursor.execute(specific_user)
        user = self.cursor.fetchone()
        return user

    def get_menu_items(self, user_id):
        menu_item = "SELECT * FROM menu WHERE item_name ='{}'".format(user_id)
        self.cursor.execute(menu_item)
        menu = self.cursor.fetchone()
        return menu

    def get_all_orders(self):
        all_orders = "SELECT * FROM orders;"
        self.cursor.execute(all_orders)
        orders = self.cursor.fetchall()
        return orders

    def get_a_specific_order(self, order_id):
        one = "SELECT * FROM orders WHERE order_item = '{}'".format(order_id)
        self.cursor.execute(one)
        order = self.cursor.fetchone()
        return order

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

    def find_user_by_username(self, username):
        """
        find a specific user given a user name
        :return:
        :param username:
        :return:
        """
        name = "SELECT * FROM users WHERE user_name ='{}'".format(username)
        self.cursor.execute(name)
        check_username = self.cursor.fetchone()
        return check_username


    def find_user_by_id(self, user_id):
        """
        find a specific user given a user id
        :param user_id:
        :return:
        """
        user = "SELECT * FROM users WHERE user_id = '{}'".format(user_id)
        self.cursor.execute(user)
        check_id = self.cursor.fetchone()
        return check_id


    def get_order_history(self):
        pass

    def update_order(self):
        pass











