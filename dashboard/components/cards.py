"""
Reusable KPI card components.
"""

from __future__ import annotations

from collections.abc import Mapping

import streamlit as st


def render_kpis(metrics: Mapping[str, str | int | float]) -> None:

    if not metrics:
        st.warning("No metrics available.")
        return

    columns = st.columns(len(metrics))

    for column, (label, value) in zip(
        columns,
        metrics.items()
    ):

        with column:

            st.metric(
                label=label,
                value=value,
            )