/*
Northwind Practice
Cris Ramirez
*/

USE northwind;

-- Question 1
	
    SELECT CategoryID, CategoryName, Description
	FROM Categories;

-- Question 2
	
    SELECT ProductID, ProductName, QuantityPerUnit
	FROM Products
	WHERE QuantityPerUnit LIKE '%box%';

-- Question 3
	
    SELECT ProductID, ProductName, Discontinued
	FROM Products
	WHERE Discontinued = 1;

-- Question 4
	
    SELECT EmployeeID,
       CONCAT(FirstName, ' ', LastName) 
       AS FullName, Title
	FROM Employees;

-- Question 5
	
    SELECT CustomerID, CompanyName, Country
	FROM Customers
	WHERE Country IN ('Germany', 'France');

-- Question 6
	
    SELECT COUNT(OrderID) 
		AS TotalOrders
	FROM Orders;

-- Question 7
	
    SELECT SupplierID, CompanyName, ContactName, ContactTitle
	FROM Suppliers
	WHERE ContactTitle IN ('Sales Representative', 'Sales Manager');

-- Question 8
	
    SELECT OrderID, CustomerID, ShipCountry, ShippedDate
	FROM Orders
	WHERE ShipCountry = 'USA';

-- Question 9
	
    SELECT OrderID, CustomerID, RequiredDate, ShippedDate
	FROM Orders
	WHERE ShippedDate > RequiredDate;

--  Question 10
	
    SELECT ProductID, ProductName, UnitsInStock, ReorderLevel, Discontinued
	FROM Products
	WHERE UnitsInStock <= ReorderLevel
		AND Discontinued = 0;