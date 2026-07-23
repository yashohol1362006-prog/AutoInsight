import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df):

    df["Revenue"] = df["Price"] * df["Quantity"]

    correlation = df[["Price", "Quantity", "Revenue"]].corr()

    plt.figure(figsize=(6,5))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")
    plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

def revenue_distribution(df):

    df["Revenue"] = df["Price"] * df["Quantity"]

    plt.figure(figsize=(8,5))

    sns.histplot(
        df["Revenue"],
        bins=10,
        kde=True
    )

    plt.title("Revenue Distribution")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

def revenue_boxplot(df):

    df["Revenue"] = df["Price"] * df["Quantity"]

    plt.figure(figsize=(8,3))

    sns.boxplot(
        x=df["Revenue"]
    )

    plt.title("Revenue Box Plot")
    plt.show()      