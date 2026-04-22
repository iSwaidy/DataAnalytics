/*
Exercise 1C - Week 03
Cris Ramirez
*/


USE northwind;

-- 1. 
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM products p
JOIN categories c 
	ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName;

-- 2. 
	SELECT p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
	FROM products p
	JOIN suppliers s 
		ON p.SupplierID = s.SupplierID
	WHERE p.UnitPrice > 75
	ORDER BY p.ProductName;

-- 3. 
	SELECT p.ProductID, p.ProductName, p.UnitPrice, 
       c.CategoryName, s.CompanyName AS SupplierName
	FROM products p
	JOIN categories c 
		ON p.CategoryID = c.CategoryID
	JOIN suppliers s 
		ON p.SupplierID = s.SupplierID
	ORDER BY p.ProductName;

-- 4. 
	SELECT o.OrderID, o.ShipName, o.ShipAddress, sh.CompanyName AS Shipper
	FROM orders o
	JOIN shippers sh 
		ON o.ShipVia = sh.ShipperID
	WHERE o.ShipCountry = 'Germany'
	ORDER BY sh.CompanyName, o.ShipName;

-- 5. 
	SELECT o.ShipName, o.ShipAddress, sh.CompanyName AS Shipper, 
       COUNT(*) AS OrderCount
	FROM orders o
	JOIN shippers sh 
		ON o.ShipVia = sh.ShipperID
		WHERE o.ShipCountry = 'Germany'
	GROUP BY o.ShipName, o.ShipAddress, sh.CompanyName
	ORDER BY sh.CompanyName, o.ShipName;

-- 6. 
	SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
	FROM orders o
	JOIN `order details` od 
		ON o.OrderID = od.OrderID
	JOIN products p 
		ON od.ProductID = p.ProductID
	WHERE p.ProductName = 'Sasquatch Ale';