import streamlit as st
import pandas as pd
from modules.visualization import ( 
    revenue_by_category,
    revenue_by_city,
    payment_mode_distribution,
    sales_trend, 
    top_selling_products,
    sold_by_category
)

from modules.visulization_by_seaborn import (
    correlation_heatmap,
    revenue_distribution,
    revenue_boxplot
)


st.set_page_config(page_title="AutoInsight", page_icon="📊", layout="wide")

st.title("📊 AutoInsight")

uploaded_file = st.file_uploader("Upload your Sales CSV . ASAP 😡😈😼", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("CSV Uploaded Successfully! 🥳🕺😝")

    st.subheader("Dataset Preview")
    st.dataframe(df)

    # ---------------- BUSINESS INSIGHTS ----------------

    revenue = (df["Price"] * df["Quantity"]).sum()
    quantity = df["Quantity"].sum()
    avg_order = df["Price"].mean()
    highest_sale = df["Price"].max()
    lowest_sale = df["Price"].min()

    max_product = df.loc[df["Price"].idxmax(), "Product"]
    min_product = df.loc[df["Price"].idxmin(), "Product"]

    top_category = (
        df.groupby("Category")["Quantity"]
        .sum()
        .idxmax()
    )

    top_city = (
        df.groupby("City")["Quantity"]
        .sum()
        .idxmax()
    )

    payment_mode = (
        df["Payment_Mode"]
        .value_counts()
        .idxmax()
    ) 

    st.header("📈 Business Insights")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💰 Total Revenue", f"₹{revenue:,}")
        st.metric("📦 Total Quantity", quantity)
        st.metric("📊 Average Order Value", f"₹{avg_order:.2f}")

    with col2:
        st.metric("📈 Highest Sale", f"₹{highest_sale:,}")
        st.metric("📉 Lowest Sale", f"₹{lowest_sale:,}")
        st.metric("⭐ Most Expensive Product", max_product)

    with col3:
        st.metric("🏆 Top Category", top_category)
        st.metric("🏙️ Top City", top_city)
        st.metric("💳 Most Used Payment Mode", payment_mode)

    st.divider()

    st.header("📊 Visualizations")

    revenue_by_category(df)

    revenue_by_city(df)

    payment_mode_distribution(df)

    sales_trend(df)

    top_selling_products(df)

    sold_by_category(df)

    correlation_heatmap(df)

    revenue_distribution(df)

    revenue_boxplot(df)
