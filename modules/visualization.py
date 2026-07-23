import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

def revenue_by_category(df):
    df['Revenue'] = df['Price'] * df['Quantity']
    categoty_revenue = df.groupby('Category')['Revenue'].sum()
    print(categoty_revenue)
    categoty_revenue.plot(kind= 'bar')
    plt.title('Revenue by Category',c = 'red' )
    plt.xlabel('Category', c = 'blue')
    plt.ylabel('Revenue', c= 'blue')
    plt.grid(axis= 'y')
    plt.xticks(rotation= 45)
    st.pyplot(plt.gcf())
    plt.clf()
def revenue_by_city(df):
    df['revenue'] = df['Price'] * df['Quantity']
    Revenue_by_city = df.groupby('City')['revenue'].sum()
    Revenue_by_city.plot(kind= 'bar') 
    plt.title('Revenue by City',c= 'red')
    plt.xlabel('City', c='blue')
    plt.ylabel('Revenue', c= 'blue')
    plt.grid(axis='y')
    st.pyplot(plt.gcf())
    plt.clf()
def payment_mode_distribution(df):
    payment_mode = df['Payment_Mode'].value_counts()
    payment_mode.plot(kind= 'pie', autopct= '%1.1f%%', startangle= 90)
    plt.title('Payment Mode Distribution')
    plt.ylabel('')
    plt.axis('equal')
    st.pyplot(plt.gcf())
    plt.clf()
def sales_trend(df):
    df['Revenue'] = df['Price'] * df['Quantity']
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    order_data = df.groupby('Order_Date')['Revenue'].sum()
    order_data.plot(kind= 'line', marker= 'o', ls= 'dashed')
    plt.title('Sales Trends Over Time')
    plt.xlabel('Dates')
    plt.ylabel('Revenue')
    st.pyplot(plt.gcf())
    plt.clf()   


def top_selling_products(df):

    st.write("Before adding Revenue:", df.columns.tolist())

    df["Revenue"] = df["Price"] * df["Quantity"]

    st.write("After adding Revenue:", df.columns.tolist())

    selling_prod = df.groupby("Product")["Revenue"].sum()

    most_selling_product = selling_prod.sort_values(ascending=False).head(10)

    most_selling_product.plot(kind="barh", color="blue")

    plt.title("Top Revenue Generating Products")
    plt.xlabel("Revenue")

    st.pyplot(plt.gcf())
    plt.clf()
    
def sold_by_category(df):
    sold_by_cat = df.groupby('Category')['Quantity'].sum()
    sold_by_cat.plot(kind='barh')
    plt.xlabel('Quantity')
    plt.ylabel('Category')
    st.pyplot(plt.gcf())
    plt.clf()

























































