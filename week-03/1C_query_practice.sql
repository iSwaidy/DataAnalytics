/*
Exercise 1C - Week 03
Cris Ramirez
*/

USE northwind;

-- 1. Write a query to list the product id, product name, and unit price of every product. 
-- This time, display them in ascending order by price.

	SELECT ProductID, ProductName, UnitPrice
	FROM products
	ORDER BY UnitPrice ASC;

-- 2. What are the products that we carry where we have at least 100 units on hand? 
-- Order them in descending order by price.

	SELECT ProductID, ProductName, UnitPrice, UnitsInStock
	FROM products
	WHERE UnitsInStock >= 100
	ORDER BY UnitPrice DESC;

-- 3. What are the products that we carry where we have at least 100 units on hand?

	SELECT ProductID, ProductName, UnitPrice, UnitsInStock
	FROM products
	WHERE UnitsInStock >= 100
	ORDER BY UnitPrice DESC, ProductName ASC;

-- 4. write a query against the orders table that displays the total number of distinct customers who have placed orders, based on customer ID.

	SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
	FROM orders;

-- 5. Write a query against the orders table that displays the total number of distinct customers who have placed orders, by customer ID, for each country where orders have been shipped. 

	SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
	FROM orders
	GROUP BY ShipCountry
	ORDER BY CustomerCount DESC;

-- 6. Write a query to list each of the job titles in employees, along with a count of how many employees hold each job title.
	
	SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
	FROM products
	WHERE UnitsInStock < 25 AND UnitsOnOrder >= 1
	ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- 7. Write a query to list each of the job titles in employees, along with a count of how many employees hold each job title.

	SELECT Title, COUNT(*) AS EmployeeCount
	FROM employees
	GROUP BY Title;
    
-- 8. What employees have a monthly salary that is between $2000 and $2500? Write a query that orders them by job title.

	SELECT EmployeeID, FirstName, LastName, Title, Salary
	FROM employees
	WHERE Salary BETWEEN 2000 AND 2500
	ORDER BY Title;