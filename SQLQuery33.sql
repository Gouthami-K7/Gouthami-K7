CREATE DATABASE Shopping_cart1;
CREATE TABLE amazon1(
    Sno INT PRIMARY KEY,
    Product_name VARCHAR(231),
    Product_Pin BIGINT UNIQUE,
    Quantity_grams BIGINT,
    Price INT,
    Category_ID INT,
    FOREIGN KEY (Category_ID) REFERENCES Categories(Category_ID)
);

CREATE TABLE Categories (
    Category_ID INT PRIMARY KEY,
    Category_Name VARCHAR(100)
);

INSERT INTO Categories VALUES (1, 'Grains');
INSERT INTO Categories VALUES (2, 'Oils');
INSERT INTO Categories VALUES (3, 'Dry Fruits');
INSERT INTO Categories VALUES (4, 'Spices');

INSERT INTO amazon1(Sno, Product_name, Product_Pin, Quantity_grams, Price, Category_ID)
VALUES 
(1,'RiceBag','837299292','2500',1351,1),
(2,'OilPacket','53742343','750',150,2),
(3,'MoonDal','729929264','50',79,1),
(4,'Almond','372132452','500',499,3),
(5,'DryKiwi','543267843','20',45,3),
(6,'KasuriMethi','53252766','100',25,4);

CREATE TABLE Customers (
    Customer_ID INT PRIMARY KEY,
    Customer_Name VARCHAR(100),
    Email VARCHAR(100) UNIQUE
);

INSERT INTO Customers VALUES 
(1, 'Gouthami', 'gouthami@gmail.com'),
(2, 'Rebecca', 'rebecca@gmail.com'),
(3, 'Madhu', 'madhu@gmail.com'),
(4, 'Siri', 'siri@gmail.com');

CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Customer_ID INT,
    Product_Sno INT,
    Order_Date DATE,
    Quantity INT,
    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
    FOREIGN KEY (Product_Sno) REFERENCES amazon1(Sno)
);

INSERT INTO Orders VALUES 
(101, 1, 2, '2025-09-01', 2), 
(102, 2, 4, '2025-09-02', 1), 
(103, 3, 1, '2025-09-03', 3), 
(104, 4, 3, '2025-09-04', 5); 
SELECT 
    O.Order_ID,
    C.Customer_Name,
    A.Product_name,
    Cat.Category_Name,
    O.Quantity,
    A.Price,
    (O.Quantity * A.Price) AS Total_Amount
FROM Orders O
INNER JOIN Customers C ON O.Customer_ID = C.Customer_ID
INNER JOIN amazon1 A ON O.Product_Sno = A.Sno
INNER JOIN Categories Cat ON A.Category_ID = Cat.Category_ID;



SELECT 
    C.Customer_Name,
    O.Order_ID,
    A.Product_name,
    Cat.Category_Name
FROM Customers C
LEFT JOIN Orders O ON C.Customer_ID = O.Customer_ID
LEFT JOIN amazon1 A ON O.Product_Sno = A.Sno
LEFT JOIN Categories Cat ON A.Category_ID = Cat.Category_ID;


SELECT 
    A.Product_name,
    Cat.Category_Name,
    O.Order_ID,
    C.Customer_Name
FROM Orders O
RIGHT JOIN amazon1 A ON O.Product_Sno = A.Sno
LEFT JOIN Customers C ON O.Customer_ID = C.Customer_ID
LEFT JOIN Categories Cat ON A.Category_ID = Cat.Category_ID;

SELECT 
    C.Customer_Name,
    A.Product_name,
    O.Order_ID
FROM Orders O
FULL OUTER JOIN Customers C ON O.Customer_ID = C.Customer_ID
FULL OUTER JOIN amazon1 A ON O.Product_Sno = A.Sno;


SELECT 
    Cat.Category_Name,
    SUM(O.Quantity * A.Price) AS Total_Sales
FROM Orders O
INNER JOIN amazon1 A ON O.Product_Sno = A.Sno
INNER JOIN Categories Cat ON A.Category_ID = Cat.Category_ID
GROUP BY Cat.Category_Name;

SELECT 
    C.Customer_Name,
    A.Product_name,
    A.Price
FROM Orders O
INNER JOIN Customers C ON O.Customer_ID = C.Customer_ID
INNER JOIN amazon1 A ON O.Product_Sno = A.Sno
WHERE (O.Quantity * A.Price) = (
    SELECT MAX(O2.Quantity * A2.Price)
    FROM Orders O2
    INNER JOIN amazon1 A2 ON O2.Product_Sno = A2.Sno
    WHERE O2.Customer_ID = O.Customer_ID
);

