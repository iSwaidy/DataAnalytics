/*
Exercise 4.C - Week 2
Cris Ramirez
*/

USE northwind;

-- a) What is the name of the table that holds the items Northwind sells?
--    Answer: The products table holds the items Northwind sells.

-- b) What is the name of the table that holds the types/categories of the items Northwind sells? 
--    Answer: The categories table holds the types/categories of items.

-- Step 5: Employees query

	SELECT * FROM employees;

-- Which employee's name makes her sound like a bird?
--    Answer: Margaret Peacock (last name is a bird).

-- Step 6: Products query

	SELECT * FROM products;
    
-- How many records does your query return? Using the toolbar options at the top of  the query pane, how can you change your query to retrieve only 10 rows?
--    Answer: The query returns 77 records; change the "Limit to 1000 rows" dropdown in the toolbar to "Limit to 10 rows".
-- BONUS: How could you write the query to limit the number of rows returned?
--    Answer: Add LIMIT 10 at the end of the query (source: MySQL documentation at dev.mysql.com/doc).

	SELECT * FROM products LIMIT 10;

-- Step 7: Categories query

	SELECT * FROM categories;
    
-- What is the category id of seafood?
--    Answer: The category id of Seafood is 8.

-- Step 8: Order sample

	SELECT OrderID, OrderDate, ShipName, ShipCountry
	FROM orders
	LIMIT 50;