from modules.loader import (load_csv, 
                            dataset_shape,
                            colum_name,
                            missing_value,
                            dataset_statistics,
                            buisness_insight
                            )
from modules.visualization import (revenue_by_category, 
                                   revenue_by_city,
                                   payment_mode_distribution,
                                   sales_trend, 
                                   top_selling_products,
                                   sold_by_category)
from modules.visulization_by_seaborn import (correlation_heatmap,
                                            revenue_distribution,
                                            revenue_boxplot)
def main():
    df = load_csv("data/sample_sales.csv")
    # it will give total no. of rows and column
    dataset_shape(df)
    # checks all columns name
    colum_name(df)
    # check if null value is there 
    missing_value(df)
    # Describes the dataset by calculating all imp paramaters like (count, mean, SD, minimum, 25th percentile, median(50%), etc)
    dataset_statistics(df)
    # It iwll count the total sum of Price
    buisness_insight(df)  
    # It will print the total revenue by category 
    revenue_by_category(df)  
    # It will print comperison betn 
    revenue_by_city(df)
    # 
    payment_mode_distribution(df) 
    #
    sales_trend(df)
    
    top_selling_products(df)   
    #
    sold_by_category(df)
    
    correlation_heatmap(df)

    revenue_distribution(df)

    revenue_boxplot(df)


if __name__ == "__main__":
    main()


