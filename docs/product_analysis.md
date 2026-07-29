# Análise de Produtos

## Perguntas de Negócio

- Quais produtos geram maior receita?
- Quais produtos vendem mais unidades?
- Quais categorias geram maior faturamento?

## Tabelas Utilizadas

- Sales.SalesOrderDetail
- Production.Product
- Production.ProductSubcategory
- Production.ProductCategory

## Métricas

- Receita = SUM(LineTotal)
- Quantidade Vendida = SUM(OrderQty)