"""
Churn page.

Customer retention and inactivity analysis.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import streamlit as st

from query_executor import run_query


st.set_page_config(
    page_title="Customer Retention",
    layout="wide",
)


@st.cache_data(show_spinner=False)
def load_recency_data():
    """
    Load customer recency information.
    """
    return run_query("07_customer_recency.sql")


def classify_risk(days_without_purchase):

    if days_without_purchase <= 180:
        return "Low"

    if days_without_purchase <= 365:
        return "Medium"

    return "High"


def main():

    st.title("Customer Retention")

    st.markdown(
        """
        Customer inactivity and churn risk analysis.
        """
    )

    st.divider()

    try:

        customers = load_recency_data()

        if customers.empty:
            st.warning(
                "The query returned no records."
            )
            return

        customers["Risk"] = customers[
            "DiasSemComprar"
        ].apply(classify_risk)

        customers = customers.sort_values(
            by="DiasSemComprar",
            ascending=False,
        )

        total_customers = len(customers)

        high_risk = len(
            customers[
                customers["Risk"] == "High"
            ]
        )

        medium_risk = len(
            customers[
                customers["Risk"] == "Medium"
            ]
        )

        low_risk = len(
            customers[
                customers["Risk"] == "Low"
            ]
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Customers",
                total_customers
            )

        with col2:

            st.metric(
                "Low Risk",
                low_risk
            )

        with col3:

            st.metric(
                "Medium Risk",
                medium_risk
            )

        with col4:

            st.metric(
                "High Risk",
                high_risk
            )

        st.divider()

        risk_summary = (
            customers["Risk"]
            .value_counts()
            .reindex(
                ["Low", "Medium", "High"],
                fill_value=0
            )
        )

        fig, ax = plt.subplots(
            figsize=(10, 5)
        )

        ax.bar(
            risk_summary.index,
            risk_summary.values,
        )

        ax.set_title(
            "Customer Risk Distribution"
        )

        ax.set_xlabel(
            "Risk Level"
        )

        ax.set_ylabel(
            "Number of Customers"
        )

        st.pyplot(fig)

        st.subheader(
            "Customer Details"
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