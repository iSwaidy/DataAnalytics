-- Deodat P. Sharma
-- April 18, 2023
-- the Northwind Database

USE northwind;
SHOW TABLES;
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'northwind'
  AND table_type = 'BASE TABLE';
  
 -- Example 1
 SELECT ProductName, UnitPrice
 FROM Products;

-- Example 2
SELECT *
FROM Products;

-- Example 3
SELECT ProductName AS 'Product',
UnitPrice AS 'Price(USD)',
UnitsInStock AS 'Stock'
FROM Products;

-- Example 4
SELECT CompanyName, City, Country
FROM Customers
WHERE Country = 'Germany';

-- Example 5
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 50;

-- Example 6
SELECT OrderID, CustomerID, ShipCountry, Freight
FROM Orders
WHERE ShipCountry = 'France';

-- Example 7
SELECT ProductName, UnitsInStock, ReorderLevel
FROM Products
WHERE UnitsInStock < ReorderLevel;

-- Example 8
SELECT OrderID , Freight
FROM Orders
WHERE Freight >= 100;

-- Missing Exercise 9
-- Example 10
SELECT ProductName, UnitPrice, UnitsInStock
FROM Products
WHERE UnitPrice > 20 AND UnitsInStock > 50;

-- Example 11
SELECT CompanyName, Country
FROM Customers
WHERE Country = 'UK' OR 'Ireland';

-- Exercise 12
SELECT ProductName, CategoryID, UnitPrice
FROM Products
WHERE ( CategoryID = 1 OR CategoryID =  2 )
AND UnitPrice < 20;

-- Exercise 13
SELECT CompanyName, Country
FROM Customers
WHERE Country != 'U.S.A';

-- Exercise 14
SELECT  ProductName
FROM Products
WHERE NOT Discontinued = 1;

-- Exercise 15
SELECT CompanyName, Country
From Customers
WHERE Country IN ('France', 'Germany', 'Spain');

 -- Exercise 16
SELECT ProductName, SupplierID
FROM Products
WHERE SupplierID NOT IN (1, 2, 3);

-- Exercise 17
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 12 AND 20;

-- Exercise 18
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice NOT BETWEEN 12 AND 20;

-- Exercise 19
SELECT OrderID, CustomerID, ShipRegion
FROM Orders
WHERE ShipRegion IS NULL;

-- Exercise 20
SELECT FirstName, LastName, Region
FROM Employees
WHERE Region IS NOT NULL;


-- Exercise 21
SELECT CompanyName 
FROM Customers
WHERE CompanyName LIKE 'A%';

-- Exercise 22
SELECT CompanyName
FROM Customers
WHERE CompanyName LIKE '%restaurant%';

-- Exercise 23
SELECT CompanyName
FROM Customers
WHERE CompanyName LIKE '_a%';

-- Exercise 24
SELECT OrderID, CustomerID, OrderDate
FROM Orders
WHERE OrderDate = '1997-01-01';   

-- Exercise 26
SELECT OrderID, OrderDate
FROM Orders
WHERE YEAR(OrderDate) = 1997 AND MONTH(OrderDate) = 6;

-- Exercise 27
SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC;

-- Exercise 28
SELECT CompanyName, Country, City
FROM Customers
ORDER BY Country ASC, CompanyName ASC;

-- Exercise 29
SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC
LIMIT 5;

-- Exercise 30
SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC
LIMIT 5, 5;

-- Exercise 31
SELECT DISTINCT Country
FROM Customers
ORDER BY Country;

-- Exercise 32
SELECT DISTINCT Country, City
FROM Customers
ORDER BY Country, City;

-- Exercise 33
SELECT CONCAT(FirstName, ' ', LastName) AS 'Full Name',
       Title
FROM Employees;

-- Exercise 34
SELECT CompanyName,
       CONCAT_WS(', ', Address, City, Country) AS 'Full Address'
FROM Customers;


-- Missing Exercise 35

-- Exercise 36
SELECT ProductName,
       UnitPrice AS 'Original Price',
       UnitPrice * 0.9 AS '10% Discount Price'
FROM Products
ORDER BY ProductName; 




