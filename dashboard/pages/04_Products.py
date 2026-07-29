"""
Products page.

Displays the top products by revenue.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import streamlit as st

from query_executor import run_query


st.set_page_config(
    page_title="Products",
    layout="wide",
)


@st.cache_data(show_spinner=False)
def load_products_data():
    """
    Load top products.
    """
    return run_query("06_top_products.sql")


def main():

    st.title("Top Products")

    st.markdown(
        """
        Top 10 products ranked by total revenue generated.
        """
    )

    st.divider()

    try:

        products = load_products_data()

        if products.empty:
            st.warning("The query returned no records.")
            return

        total_revenue = products["Receita"].sum()

        top_product = products.iloc[0]["Produto"]

        average_revenue = products["Receita"].mean()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Revenue",
                f"${total_revenue:,.2f}"
            )

        with col2:

            st.metric(
                "Top Product",
                top_product
            )

        with col3:

            st.metric(
                "Average Revenue",
                f"${average_revenue:,.2f}"
            )

        st.divider()

        st.subheader("Product Ranking")

        st.dataframe(
            products,
            use_container_width=True,
            hide_index=True,
        )

        chart_data = products.sort_values(
            by="Receita",
            ascending=True,
        )

        fig, ax = plt.subplots(
            figsize=(12, 6)
        )

        ax.barh(
            chart_data["Produto"],
            chart_data["Receita"],
        )

        ax.set_title(
            "Top Products by Revenue"
        )

        ax.set_xlabel(
            "Revenue"
        )

        ax.set_ylabel(
            "Product"
        )

        st.pyplot(fig)

    except Exception as error:

        st.error(str(error))


if __name__ == "__main__":
    main()