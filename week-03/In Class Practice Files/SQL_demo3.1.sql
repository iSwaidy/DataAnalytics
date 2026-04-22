-- Cris
-- April 20, 2026
-- the Northwind Database

USE northwind;
SHOW TABLES;

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'northwind'
  AND table_type = 'BASE TABLE';
  
  SELECT ProductName, UnitPrice
  FROM Products;
  SELECT * FROM Products;
  
SELECT 
    ProductName AS 'Product',
    UnitPrice AS 'Price(USD)',
    UnitsInStock AS 'Stock'
FROM Products;

SELECT CompanyName, City, Country
FROM Customers
WHERE Country = 'Germany';

SELECT ProductName, UnitPrice
FROM Products
Where UnitPrice > 50;

SELECT OrderID, CustomerID, ShipCountry, Freight
FROM Orders
WHERE ShipCountry = 'France';

SELECT ProductName, UnitInStock, ReorderLevel
FROM Products
WHERE UnitsInStock < ReorderLevel;

SELECT OrderID, Freight
FROM Orders
WHERE Freight >= 100;

SELECT ProductName, UnitPrice, UnitsInStock
FROM Products
WHERE UnitPrice > 20 AND UnitsInStock > 50;

SELECT CompanyName, Country
FROM Customers
WHERE Country = 'UK'
   OR Country = 'Ireland';
   
SELECT CompanyName, Country
From Customers
WHERE NOT Country = 'USA';
   
SELECT ProductName
FROM Products
WHERE Discountinued !=1;
   
SELECT CompanyName, Country
FROM Customers
WHERE Country IN ('France', 'Germany', 'Spain');

SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 10 AND 20;

SELECT OrderID, CustomerID, ShipRegion
FROM Orders
WHERE Shipregion IS NULL;

SELECT FirstName, LastName, Region
FROM Employees
WHERE Region IS NOT NULL;

SELECT OrderID, CustomerID, OrderDate
FROM Orders
WHERE Orderdate = '1997-01-01';

SELECT OrderID, OrderDate
FROM Orders
WHERE YEAR(OrderDate) = 1997
  AND MONTH(OrderDate) = 6;
  
SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC;

SELECT CompanyName, Country, City
FROM Customers
ORDER BY Country, CompanyName;

-- 29.

SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC
LIMIT 5;

-- 30.

SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC
LIMIT 5 OFFSET 5;

SELECT 
    ProductName,
    UnitPrice AS 'Original Price',
    UnitPrice * 0.9 AS '10% Discount Price'
FROM Products;
