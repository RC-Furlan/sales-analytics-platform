/*=================================
CLIENTES E PEDIDOS

SELECT
    c.CustomerID,
    soh.SalesOrderID,
    soh.TotalDue
FROM Sales.Customer AS c

INNER JOIN Sales.SalesOrderHeader AS soh
    ON c.CustomerID = soh.CustomerID;

RECEITA POR CLIENTE


SELECT

    c.CustomerID,

    SUM(soh.TotalDue) AS ReceitaTotal

FROM Sales.Customer AS c

INNER JOIN Sales.SalesOrderHeader AS soh

    ON c.CustomerID = soh.CustomerID

GROUP BY

    c.CustomerID

ORDER BY

    ReceitaTotal DESC;



TOP 10 CLIENTES

SELECT TOP (10)

    c.CustomerID,

    SUM(soh.TotalDue) AS ReceitaTotal

FROM Sales.Customer AS c

INNER JOIN Sales.SalesOrderHeader AS soh

    ON c.CustomerID = soh.CustomerID

GROUP BY

    c.CustomerID

ORDER BY

    ReceitaTotal DESC;



CLIENTE + NOME

SELECT TOP (10)

    c.CustomerID,

    p.FirstName,

    p.LastName,

    SUM(soh.TotalDue) AS ReceitaTotal

FROM Sales.Customer AS c

INNER JOIN Person.Person AS p

    ON c.PersonID = p.BusinessEntityID

INNER JOIN Sales.SalesOrderHeader AS soh

    ON c.CustomerID = soh.CustomerID

GROUP BY

    c.CustomerID,

    p.FirstName,

    p.LastName

ORDER BY

    ReceitaTotal DESC;
====================================================*/


SELECT TOP (10)

    c.CustomerID,

    CONCAT(p.FirstName, ' ', p.LastName) AS Cliente,

    COUNT(DISTINCT soh.SalesOrderID) AS QuantidadePedidos,

    SUM(soh.TotalDue) AS ReceitaTotal

FROM Sales.Customer AS c

INNER JOIN Person.Person AS p
    ON c.PersonID = p.BusinessEntityID

INNER JOIN Sales.SalesOrderHeader AS soh
    ON c.CustomerID = soh.CustomerID

GROUP BY

    c.CustomerID,

    CONCAT(p.FirstName, ' ', p.LastName)

ORDER BY

    ReceitaTotal DESC;