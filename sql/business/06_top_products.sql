/*====================================================
RECEITA POR PRODUTO
====================================================*/

SELECT

    ProductID,

    SUM(LineTotal) AS Receita

FROM Sales.SalesOrderDetail

GROUP BY ProductID

ORDER BY Receita DESC;

/*====================================================
RECEITA POR PRODUTO
====================================================*/

SELECT

    p.ProductID,

    p.Name,

    SUM(sod.LineTotal) AS Receita

FROM Sales.SalesOrderDetail AS sod

INNER JOIN Production.Product AS p

    ON sod.ProductID = p.ProductID

GROUP BY

    p.ProductID,

    p.Name

ORDER BY Receita DESC;

/*====================================================
TOP 10 PRODUTOS POR RECEITA
====================================================*/

SELECT TOP (10)

    p.ProductID,

    p.Name,

    SUM(sod.LineTotal) AS Receita

FROM Sales.SalesOrderDetail AS sod

INNER JOIN Production.Product AS p

    ON sod.ProductID = p.ProductID

GROUP BY

    p.ProductID,

    p.Name

ORDER BY Receita DESC;

/*====================================================
TOP 10 PRODUTOS POR QUANTIDADE
====================================================*/

SELECT TOP (10)

    p.ProductID,

    p.Name,

    SUM(sod.OrderQty) AS QuantidadeVendida

FROM Sales.SalesOrderDetail AS sod

INNER JOIN Production.Product AS p

    ON sod.ProductID = p.ProductID

GROUP BY

    p.ProductID,

    p.Name

ORDER BY QuantidadeVendida DESC;

/*====================================================
RECEITA POR CATEGORIA
====================================================*/

SELECT

    pc.Name AS Categoria,

    SUM(sod.LineTotal) AS Receita

FROM Sales.SalesOrderDetail AS sod

INNER JOIN Production.Product AS p

    ON sod.ProductID = p.ProductID

INNER JOIN Production.ProductSubcategory AS ps

    ON p.ProductSubcategoryID = ps.ProductSubcategoryID

INNER JOIN Production.ProductCategory AS pc

    ON ps.ProductCategoryID = pc.ProductCategoryID

GROUP BY

    pc.Name

ORDER BY Receita DESC;