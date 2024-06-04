import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',    
    password='Ali2003!', 
    database='pizza_shop'    
)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(15),
    Address VARCHAR(255)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATETIME,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Pizzas (
    PizzaID INT AUTO_INCREMENT PRIMARY KEY,
    PizzaName VARCHAR(100),
    Price DECIMAL(5, 2)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT,
    PizzaID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (PizzaID) REFERENCES Pizzas(PizzaID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Ingredients (
    IngredientID INT AUTO_INCREMENT PRIMARY KEY,
    PizzaID INT,
    IngredientName VARCHAR(100),
    FOREIGN KEY (PizzaID) REFERENCES Pizzas(PizzaID)
)
''')



customers = [
    ('Ali', 'Aliyev', 'alialyevv423@gmail.com', '051-595-65-52', 'Azerbaijan Baku'),
    ('Yunus', 'Mammadov', 'mammadov212@gmail.com', '070-221-12-21', 'Azerbaijan Baku'),
    ('Mahammad', 'Eyvazov', 'eyvazov44@gmail.com', '051-323-32-44', 'Azerbaijan Baku'),
    ('Kanan', 'Barxudarli', 'barxudarli87@gmail.com', '055-456-65-14', 'Azerbaijan Baku'),
    ('Ramil', 'Qarayev', 'qarayev13@gmail.com', '050-431-12-11', 'Azerbaijan Baku'),
    ('Huseyn', 'Aliyev', 'radon@gmail.com', '051-444-34-44', 'Azerbaijan Baku'),
    ('Amin', 'Aliyev', 'aminaliyev@gmail.com', '051-211-11-44', 'Azerbaijan Baku'),
    ('Sardar', 'Aliyev', 'sardaraliyev@gmail.com', '055-376-21-76', 'Azerbaijan Baku'),
    ('Ramin', 'İbrahimov', 'iramin414@gmail.com', '070-233-21-33', 'Azerbaijan Baku')
]

cursor.executemany('''
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES (%s, %s, %s, %s, %s)
''', customers)

orders = [
    (1, '2024-05-23', 18.00),
    (2, '2024-05-12', 27.00),
    (3, '2024-03-01', 40.00),
    (2, '2024-05-20', 27.98),
    (2, '2024-05-19', 44.00),
    (3, '2024-05-02', 48.00),
    (4, '2024-05-19', 11.00),
    (5, '2024-02-21', 27.98),
    (6, '2024-01-13', 21.98)
]

cursor.executemany('''
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES (%s, %s, %s)
''', orders)

pizzas = [
    ('Margherita', 8),
    ('Pepperoni', 9),
    ('BBQ Chicken', 11),
    ('Hawaiian', 10.99),
    ('Veggie', 9.99),
    ('Meat Lovers', 12),
    ('Four Cheese', 11),
    ('Supreme', 13.99),
    ('Buffalo Chicken', 11.99),
    ('Mediterranean', 10.99)
]

cursor.executemany('''
INSERT INTO Pizzas (PizzaName, Price) VALUES (%s, %s)
''', pizzas)

ingredients = [
    (2, 'Tomato Sauce'),
    (2, 'Mozzarella'),
    (2, 'Pepperoni'),
    (3, 'BBQ Sauce'),
    (3, 'Mozzarella'),
    (3, 'Grilled Chicken'),
    (3, 'Red Onions'),
    (3, 'Cilantro'),
    (4, 'Tomato Sauce'),
    (4, 'Mozzarella'),
    (4, 'Ham'),
    (4, 'Pineapple'),
    (5, 'Tomato Sauce'),
    (5, 'Mozzarella'),
    (5, 'Bell Peppers'),
    (5, 'Olives'),
    (5, 'Onions'),
    (5, 'Mushrooms'),
    (6, 'Tomato Sauce'),
    (6, 'Mozzarella'),
    (6, 'Pepperoni'),
    (6, 'Sausage'),
    (6, 'Bacon'),
    (6, 'Ham'),
    (7, 'Tomato Sauce'),
    (7, 'Mozzarella'),
    (7, 'Cheddar'),
    (7, 'Parmesan'),
    (7, 'Gorgonzola'),
    (8, 'Tomato Sauce'),
    (8, 'Mozzarella'),
    (8, 'Pepperoni'),
    (8, 'Sausage'),
    (8, 'Bell Peppers'),
    (8, 'Onions'),
    (8, 'Olives'),
    (8, 'Mushrooms'),
    (9, 'Buffalo Sauce'),
    (9, 'Mozzarella'),
    (9, 'Grilled Chicken'),
    (9, 'Red Onions'),
    (9, 'Ranch or Blue Cheese Drizzle'),
    (10, 'Tomato Sauce'),
    (10, 'Mozzarella'),
    (10, 'Feta Cheese'),
    (10, 'Spinach'),
    (10, 'Olives'),
    (10, 'Red Onions'),
    (10, 'Sun-dried Tomatoes')
]

cursor.executemany('''
INSERT INTO Ingredients (PizzaID, IngredientName) VALUES (%s, %s)
''', ingredients)

conn.commit()
conn.close()