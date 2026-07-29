"""
Customers page.

Displays the top customers by revenue.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import streamlit as st

from query_executor import run_query


st.set_page_config(
    page_title="Customers",
    layout="wide",
)


@st.cache_data(show_spinner=False)
def load_customers_data():
    """
    Load top customers.
    """
    return run_query("05_top_customers.sql")


def main():

    st.title("Customer Analysis")

    st.markdown(
        """
        Top 10 customers ranked by total revenue generated.
        """
    )

    st.divider()

    try:

        customers = load_customers_data()

        if customers.empty:
            st.warning("The query returned no records.")
            return

        required_columns = [
            "Cliente",
            "QuantidadePedidos",
            "ReceitaTotal",
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in customers.columns
        ]

        if missing_columns:
            st.error(
                f"Missing columns: {', '.join(missing_columns)}"
            )
            return

        total_revenue = customers[
            "ReceitaTotal"
        ].sum()

        top_customer = customers.iloc[0][
            "Cliente"
        ]

        average_revenue = customers[
            "ReceitaTotal"
        ].mean()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Revenue",
                f"R$ {total_revenue:,.2f}"
            )

        with col2:

            st.metric(
                "Top Customer",
                top_customer
            )

        with col3:

            st.metric(
                "Average Revenue",
                f"R$ {average_revenue:,.2f}"
            )

        st.divider()

        fig, ax = plt.subplots(
            figsize=(12, 6)
        )

        plot_data = customers.sort_values(
            by="ReceitaTotal",
            ascending=True,
        )

        ax.barh(
            plot_data["Cliente"],
            plot_data["ReceitaTotal"],
        )

        ax.set_title(
            "Top Customers by Revenue"
        )

        ax.set_xlabel(
            "Revenue"
        )

        ax.set_ylabel(
            "Customer"
        )

        st.pyplot(fig)

        st.subheader(
            "Customer Ranking"
        )

        st.dataframe(
            customers,
            use_container_width=True,
            hide_index=True,
        )

    except Exception as error:

        st.error(str(error))


if __name__ == "__main__":
    main()