import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(
            r"D:\\python_basics\\Repo\\YaroshenkoQaPython" + r"\\become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # The additional metods

    def get_all_primary_keys_from_table(self, id, table):
        query = f"SELECT {id} FROM {table}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_all_from_table(self, table):
        query = f"SELECT * FROM {table}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_from_table_by_id(self, table, id):
        query = f"SELECT * FROM {table} WHERE id = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_sum_column_from_table(self, column, table):
        query = f"SELECT sum({column}) FROM {table}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_count_column_table(self, column, table):
        query = f"SELECT count({column}) FROM {table}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_record_from_table_by_field_name(self, table, field_name, value):
        query = f"SELECT * FROM {table} WHERE {field_name} = {value}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_customer(self, id, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) VALUES ({id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_record_from_table_by_id(self, table, id):
        query = f"DELETE FROM {table} WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_order(self, id, customer_id, product_id, order_date):
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) VALUES ({id}, {customer_id}, {product_id}, '{order_date}')"
        self.cursor.execute(query)
        self.connection.commit()
