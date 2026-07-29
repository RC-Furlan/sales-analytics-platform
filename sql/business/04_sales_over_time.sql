/*
==========================================
MÉTRICA 04
Receita por Ano
==========================================
*/

SELECT
    YEAR(OrderDate) AS Ano,
    SUM(TotalDue) AS Receita
FROM Sales.SalesOrderHeader
GROUP BY YEAR(OrderDate)
ORDER BY Ano;

/*
==========================================
Receita por Ano e Mês
==========================================
*/

SELECT
    YEAR(OrderDate) AS Ano,
    MONTH(OrderDate) AS Mes,
    SUM(TotalDue) AS Receita
FROM Sales.SalesOrderHeader
GROUP BY
    YEAR(OrderDate),
    MONTH(OrderDate)
ORDER BY
    Ano,
    Mes;