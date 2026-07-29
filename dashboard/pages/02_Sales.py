"""
Sales page.

Displays the revenue evolution over time.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import streamlit as st

from query_executor import run_query


st.set_page_config(
    page_title="Sales",
    layout="wide",
)


@st.cache_data(show_spinner=False)
def load_sales_data():
    """
    Load revenue over time.
    """
    return run_query("04_sales_over_time.sql")


def main():

    st.title("Sales Performance")

    st.markdown(
        """
        Historical revenue analysis based on AdventureWorks sales records.
        This page highlights revenue evolution and key sales indicators
        across the analyzed period.
        """
    )

    st.divider()

    try:

        sales = load_sales_data()

        if sales.empty:
            st.warning("The query returned no records.")
            return

        required_columns = [
            "Ano",
            "Receita",
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in sales.columns
        ]

        if missing_columns:
            st.error(
                f"Missing columns: {', '.join(missing_columns)}"
            )
            return

        total_revenue = sales["Receita"].sum()

        average_revenue = sales["Receita"].mean()

        best_year_row = sales.loc[
            sales["Receita"].idxmax()
        ]

        best_year = best_year_row["Ano"]

        best_year_revenue = best_year_row["Receita"]

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Revenue",
                f"R$ {total_revenue:,.2f}",
            )

        with col2:

            st.metric(
                "Average Annual Revenue",
                f"R$ {average_revenue:,.2f}",
            )

        with col3:

            st.metric(
                "Best Sales Year",
                str(best_year),
            )

        st.divider()

        fig, ax = plt.subplots(figsize=(12, 5))

        ax.plot(
            sales["Ano"],
            sales["Receita"],
            linewidth=2,
            marker="o",
        )

        ax.set_title(
            "Revenue Evolution"
        )

        ax.set_xlabel(
            "Year"
        )

        ax.set_ylabel(
            "Revenue"
        )

        ax.grid(True)

        st.pyplot(fig)

        st.info(
            f"The highest revenue was recorded in {best_year}, "
            f"reaching R$ {best_year_revenue:,.2f}."
        )

        st.subheader(
            "Revenue History"
        )

        st.dataframe(
            sales,
            use_container_width=True,
            hide_index=True,
        )

    except Exception as error:

        st.error(str(error))


if __name__ == "__main__":
    main()