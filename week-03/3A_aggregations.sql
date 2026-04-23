/*
Exercise 3A - Week 03
Cris Ramirez
*/

USE northwind;

-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to find the name of the product that has that price.

SELECT MIN(UnitPrice) 
	AS CheapestPrice
FROM products;

-- CheapestPrice 2.50

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);

-- Geitost 

-- 2.  Write a query to find the average price of all items that Northwind sells.

SELECT AVG(UnitPrice) AS AveragePrice
FROM products;

-- Average Price 28.86636364

-- BONUS: AI Feedback
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM products;

-- Average Price Rounded 28.87

-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then write a second query to find the name of the product with that price, plus the name of the supplier for that product.

SELECT MAX(UnitPrice) AS HighestPrice
FROM products;

-- Highest Price 263.5000

SELECT p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
FROM products p
JOIN suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (SELECT MAX(UnitPrice) FROM products);

-- Product Name Cte de Blaye Supplier Name  Aux joyeux ecclsiastiques

-- 4. Write a query to find total monthly payroll.

SELECT SUM(salary) AS TotalMonthlyPayroll
FROM employees;

-- Total Monthly Payroll 20362

-- 5.  Write a query to identify the highest salary and the lowest salary amounts which any employee makes.

SELECT MAX(salary) AS HighestSalary, 
       MIN(salary) AS LowestSalary
FROM employees;

-- highest 3119.15  lowest 1744.21

-- 6. Write a query to find the name and supplier ID of each supplier and the number of items they supply. 

SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID) AS ItemCount
FROM suppliers s
JOIN products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;

-- 7. Write a query to find the list of all category names and the average price for items in each category

SELECT c.CategoryName, AVG(p.UnitPrice) AS AveragePrice
FROM categories c
JOIN products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what is the name of each supplier and the number of items they supply.

SELECT s.CompanyName, COUNT(p.ProductID) AS ItemCount
FROM suppliers s
JOIN products p ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

-- 9. Write a query to list products currently in inventory by the product id, product name, and inventory value. Sort the results in descending order by value. If two or more have the same value, order by product name.

SELECT ProductID, ProductName, (UnitPrice * UnitsInStock) AS InventoryValue
FROM products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;