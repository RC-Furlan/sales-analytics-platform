/*
==========================================
MÉTRICA 01
Receita Total
==========================================
*/

SELECT
    SUM(TotalDue) AS ReceitaTotal
FROM Sales.SalesOrderHeader;