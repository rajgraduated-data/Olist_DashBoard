import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


customers = pd.read_csv('olist_customers_dataset.csv')
orders = pd.read_csv('olist_orders_dataset.csv')
order_items = pd.read_csv('olist_order_items_dataset.csv')


orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders_delivered = orders[orders['order_status'] == 'delivered'].copy()

df = orders_delivered.merge(customers, on='customer_id', how='left')
df = df.merge(order_items[['order_id', 'price']], on='order_id', how='left')
df = df[['customer_id', 'order_id', 'order_purchase_timestamp', 'price']].dropna()

#Calculation Part
reference_date = df['order_purchase_timestamp'].max() + timedelta(days=1)

rfm = df.groupby('customer_id').agg(
    Recency=('order_purchase_timestamp', lambda x: (reference_date - x.max()).days),
    Frequency=('order_id', 'count'),
    Monetary=('price', 'sum')
).reset_index()

rfm['R_Score'] = pd.qcut(rfm['Recency'], q=5, labels=[5,4,3,2,1]).astype(int)
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=5, labels=[1,2,3,4,5]).astype(int)
rfm['M_Score'] = pd.qcut(rfm['Monetary'].rank(method='first'), q=5, labels=[1,2,3,4,5]).astype(int)

rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
rfm['Total_Score'] = rfm['R_Score'] + rfm['F_Score'] + rfm['M_Score']

def segment(row):
    if row['R_Score'] >= 4 and row['F_Score'] >= 4: return 'Champions'
    elif row['R_Score'] >= 3 and row['F_Score'] >= 3: return 'Loyal'
    elif row['R_Score'] >= 4 and row['F_Score'] <= 2: return 'New'
    elif row['R_Score'] <= 2 and row['F_Score'] >= 3: return 'At Risk'
    elif row['R_Score'] <= 2 and row['F_Score'] <= 2: return 'Lost'
    return 'Regular'

rfm['Segment'] = rfm.apply(segment, axis=1)


rfm.to_csv('rfm_customer_data.csv', index=False)

segment_summary = rfm.groupby('Segment').agg(
    Customer_Count=('customer_id', 'count'),
    Avg_Recency=('Recency', 'mean'),
    Avg_Frequency=('Frequency', 'mean'),
    Avg_Monetary=('Monetary', 'mean')
).round(2).reset_index()

segment_summary.to_csv('segment_summary.csv', index=False)

print("✅ Done! These file are ready to use 1. rfm_customer_data.csv , 2. segment_summary.csv:")