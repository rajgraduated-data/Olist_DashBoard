## 📋 Overview

This project performs **RFM (Recency, Frequency, Monetary) analysis** on customer transaction data from Olist, a Brazilian e-commerce platform. The analysis segments customers into distinct groups based on their purchasing behavior, enabling data-driven marketing strategies and customer relationship management.

## 🎯 Project Objectives

- Analyze customer purchasing patterns using RFM methodology
- Segment customers into meaningful groups (Champions, Loyal, At Risk, Lost, etc.)
- Identify high-value customers and those at risk of churning
- Provide actionable insights for targeted marketing campaigns
- Visualize customer distribution and behavior patterns

## 📊 Dashboard Preview

![RFM Dashboard](dashboard.png)

The interactive dashboard displays:
- **Key Metrics**: Total Customers, Total Revenue, Average Customer Value, Champions Count
- **Customer Distribution**: Breakdown across 6 segments
- **At-Risk & Lost Customers**: Percentage analysis
- **RFM Score Distribution**: Customer distribution across score ranges
- **Average Monetary by Segment**: Revenue contribution per segment
- **Recency vs Frequency**: Scatter plot with Monetary as size indicator

## 🔧 Features

- **Automated RFM Calculation**: Computes Recency, Frequency, and Monetary values for each customer
- **Customer Scoring**: Assigns 1-5 scores for each RFM dimension using quintiles
- **Intelligent Segmentation**: Categorizes customers into 6 distinct segments:
  - **Champions**: High recency, frequency, and monetary values
  - **Loyal**: Consistent purchasers with good value
  - **New**: Recent customers with potential for growth
  - **At Risk**: Previously valuable customers showing declining engagement
  - **Lost**: Inactive customers with low engagement
  - **Regular**: Average customers with moderate activity

- **Comprehensive Reporting**: Generates detailed CSV outputs for further analysis
- **Data Visualization**: Creates insightful charts and graphs

## 📁 Dataset

This project uses the **Olist E-commerce Dataset** from Kaggle, which contains:
- `olist_customers_dataset.csv`: Customer information
- `olist_orders_dataset.csv`: Order details with timestamps
- `olist_order_items_dataset.csv`: Order items with pricing information

### Key Data Points
- **Total Customers**: 96,478
- **Total Revenue**: $13.22M
- **Average Customer Value**: $137.04
- **Analysis Period**: Historical order data
