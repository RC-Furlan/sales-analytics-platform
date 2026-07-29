"""
ABC Curve page.

Classifies products according to cumulative revenue contribution.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import streamlit as st

from query_executor import run_query


st.set_page_config(
    page_title="ABC Curve",
    layout="wide",
)


@st.cache_data(show_spinner=False)
def load_products_data():
    """
    Load products revenue data.
    """
    return run_query("06_top_products.sql")


def main():

    st.title("ABC Curve")

    st.markdown(
        """
        Product classification based on cumulative revenue contribution.
        """
    )

    st.divider()

    try:

        products = load_products_data()

        if products.empty:
            st.warning("The query returned no records.")
            return

        abc = products.copy()

        abc = abc.sort_values(
            by="Receita",
            ascending=False,
        )

        total_revenue = abc["Receita"].sum()

        abc["RevenueShare"] = (
            abc["Receita"]
            / total_revenue
        )

        abc["CumulativeShare"] = (
            abc["RevenueShare"]
            .cumsum()
        )

        abc["Class"] = "C"

        abc.loc[
            abc["CumulativeShare"] <= 0.80,
            "Class",
        ] = "A"

        abc.loc[
            (
                abc["CumulativeShare"] > 0.80
            )
            &
            (
                abc["CumulativeShare"] <= 0.95
            ),
            "Class",
        ] = "B"

        class_summary = (
            abc["Class"]
            .value_counts()
            .sort_index()
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Class A Products",
                int(class_summary.get("A", 0))
            )

        with col2:

            st.metric(
                "Class B Products",
                int(class_summary.get("B", 0))
            )

        with col3:

            st.metric(
                "Class C Products",
                int(class_summary.get("C", 0))
            )

        st.divider()

        fig, ax = plt.subplots(
            figsize=(12, 6)
        )

        ax.plot(
            range(1, len(abc) + 1),
            abc["CumulativeShare"] * 100,
            marker="o",
            linewidth=2,
        )

        ax.axhline(
            y=80,
            linestyle="--",
        )

        ax.axhline(
            y=95,
            linestyle="--",
        )

        ax.set_title(
            "ABC Curve"
        )

        ax.set_xlabel(
            "Products"
        )

        ax.set_ylabel(
            "Cumulative Revenue (%)"
        )

        ax.grid(True)

        st.pyplot(fig)

        st.subheader(
            "ABC Classification"
        )

        display_df = abc.copy()

        display_df["RevenueShare"] = (
            display_df["RevenueShare"] * 100
        ).round(2)

        display_df["CumulativeShare"] = (
            display_df["CumulativeShare"] * 100
        ).round(2)

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
        )

    except Exception as error:

        st.error(str(error))


if __name__ == "__main__":
    main()