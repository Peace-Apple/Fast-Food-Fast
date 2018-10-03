"""
Module to handle data storage
"""

import psycopg2


class DatabaseConnection:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(database="fastfoodfast", user="postgres", password="apple123",
                                               host="127.0.0.1", port="5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Database opened successfully")

        except:
            print("Database connection failed")

    def create_tables(self):
        """
        This method creates tables one after the other in the database after the connection has been established.

        """
        commands = (
            """
            CREATE TABLE IF NOT EXISTS "users" (
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(25) NOT NULL,
                    email VARCHAR(50) UNIQUE NOT NULL,
                    phone_number INTEGER NOT NULL,
                    user_type BOOLEAN NOT NULL DEFAULT FALSE,
                    password VARCHAR(255) NOT NULL,
                    is_loggedin BOOLEAN DEFAULT FALSE
                );
            """,
            """
            CREATE TABLE IF NOT EXISTS "menu" (
                    item_id SERIAL PRIMARY KEY, 
                    item_name VARCHAR(50) NOT NULL, 
                    price INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES "users" (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
                    
                );
            """,
            """
            CREATE TABLE IF NOT EXISTS "orders" (
                    order_id SERIAL PRIMARY KEY, 
                    user_id INTEGER NOT NULL,
                    item_id INTEGER NOT NULL, 
                    order_status VARCHAR(25) NOT NULL DEFAULT 'New',
                    quantity INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES "users" (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (item_id) REFERENCES "menu" (item_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                    order_date TIMESTAMP DEFAULT NOW()
                );
            """)

        try:
            for command in commands:
                self.cursor.execute(command)
            self.connection.commit()
            self.cursor.close()
            print("Tables created successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.connection is not None:
                self.connection.close()

    def insert_user(self, user_name, email, phone_number, password):
        add_user = "INSERT INTO users (user_name, email, phone_number, password)\
         VALUES ('"+user_name+"', '"+email+"', '"+phone_number+"', '"+password+"')"
        self.cursor.execute(add_user)

    def insert_order(self, ):
        add_order = "INSERT INTO orders (user_id, item_id)\
         VALUES (%s,%s)"
        self.cursor.execute(add_order)


    def insert_menu_item(self):
        add_item = "INSERT INTO menu (user_id, item_name)\
         VALUES ('"+user_id+"','"+item_name+"')"
        self.cursor.execute(add_item)














