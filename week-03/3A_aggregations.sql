/*
Exercise 3A - Week 03
Cris Ramirez
*/

USE northwind;

-- 1.

SELECT MIN(UnitPrice) 
	AS CheapestPrice
FROM products;

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);

-- 2. 

SELECT AVG(UnitPrice) AS AveragePrice
FROM products;

SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM products;

-- 3.

SELECT MAX(UnitPrice) AS HighestPrice
FROM products;

SELECT p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
FROM products p
JOIN suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (SELECT MAX(UnitPrice) FROM products);

-- 4.

SELECT SUM(MonthlySalary) AS TotalMonthlyPayroll
FROM employees;

-- 5. 

SELECT MAX(MonthlySalary) AS HighestSalary, 
       MIN(MonthlySalary) AS LowestSalary
FROM employees;

-- 6.

SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID) AS ItemCount
FROM suppliers s
JOIN products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;

-- 7. 

SELECT c.CategoryName, AVG(p.UnitPrice) AS AveragePrice
FROM categories c
JOIN products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

-- 8. 

SELECT s.CompanyName, COUNT(p.ProductID) AS ItemCount
FROM suppliers s
JOIN products p ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

-- 9. 

SELECT ProductID, ProductName, (UnitPrice * UnitsInStock) AS InventoryValue
FROM products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;