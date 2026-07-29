/*
==========================================
MÉTRICA 03
Ticket Médio
==========================================
*/

SELECT
    AVG(TotalDue) AS TicketMedio
FROM Sales.SalesOrderHeader;