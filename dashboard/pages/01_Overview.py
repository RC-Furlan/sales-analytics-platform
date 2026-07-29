"""
Overview page.
"""

from __future__ import annotations

import pandas as pd
import streamlit as st

from components.cards import render_kpis
from query_executor import run_query


st.set_page_config(
    page_title="Overview",
    layout="wide",
)


@st.cache_data(show_spinner=False)
def load_metrics():

    revenue = run_query("01_revenue.sql")
    orders = run_query("02_orders.sql")
    ticket = run_query("03_average_ticket.sql")

    return {
        "Receita Total": f"R$ {revenue['ReceitaTotal'].iloc[0]:,.2f}",
        "Pedidos": f"{orders['TotalPedidos'].iloc[0]:,.0f}",
        "Ticket Médio": f"R$ {ticket['TicketMedio'].iloc[0]:,.2f}",
    }


@st.cache_data(show_spinner=False)
def load_business_summary():

    return run_query(
        "08_business_summary.sql"
    )


def main():

    st.title(
        "Sales Analytics Dashboard"
    )

    st.markdown(
        """
        Executive overview of AdventureWorks sales performance.
        """
    )

    st.divider()

    try:

        metrics = load_metrics()

        render_kpis(metrics)

        st.divider()

        summary = load_business_summary()

        total_customers = int(
            summary["TotalClientes"].iloc[0]
        )

        total_products = int(
            summary["TotalProdutos"].iloc[0]
        )

        first_sale = pd.to_datetime(
            summary["PrimeiraVenda"].iloc[0]
        )

        last_sale = pd.to_datetime(
            summary["UltimaVenda"].iloc[0]
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Business Overview"
            )

            st.markdown(
                f"""
                **Customers:** {total_customers:,}

                **Products:** {total_products:,}

                **Sales Period:** {first_sale:%Y} - {last_sale:%Y}
                """
            )

        with col2:

            st.subheader(
                "About AdventureWorks"
            )

            st.markdown(
                """
                AdventureWorks is Microsoft's sample business
                database representing a global manufacturing
                and retail company.

                The dashboard analyzes sales transactions,
                customers, products and retention indicators
                to support business decision making.
                """
            )

    except Exception as error:

        st.error(str(error))


if __name__ == "__main__":
    main()