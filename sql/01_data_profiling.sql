/*====================================================
AUDITORIA - QUANTIDADE DE REGISTROS
====================================================*/

SELECT COUNT(*) AS TotalClientes
FROM Sales.Customer;

SELECT COUNT(*) AS TotalPedidos
FROM Sales.SalesOrderHeader;

SELECT COUNT(*) AS TotalItensPedido
FROM Sales.SalesOrderDetail;

SELECT COUNT(*) AS TotalProdutos
FROM Production.Product;

/*====================================================
PERÍODO DAS VENDAS
====================================================*/

SELECT
    MIN(OrderDate) AS PrimeiraVenda,
    MAX(OrderDate) AS UltimaVenda
FROM Sales.SalesOrderHeader;

/*====================================================
PRODUTOS SEM SUBCATEGORIA
====================================================*/

SELECT COUNT(*) AS ProdutosSemSubcategoria
FROM Production.Product
WHERE ProductSubcategoryID IS NULL;

/*====================================================
CLIENTES SEM PERSONID
====================================================*/

SELECT COUNT(*) AS ClientesSemPessoa
FROM Sales.Customer
WHERE PersonID IS NULL;

/*====================================================
VERIFICAÇÃO DE DUPLICIDADE
====================================================*/

SELECT
    CustomerID,
    COUNT(*) AS Quantidade
FROM Sales.Customer
GROUP BY CustomerID
HAVING COUNT(*) > 1;

/*====================================================
PRODUTOS SEM VENDAS
====================================================*/

SELECT
    p.ProductID,
    p.Name
FROM Production.Product AS p
LEFT JOIN Sales.SalesOrderDetail AS sod
    ON p.ProductID = sod.ProductID
WHERE sod.ProductID IS NULL
ORDER BY p.Name;

