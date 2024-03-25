import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend which doesn't require a display
import matplotlib.pyplot as plt

import streamlit as st
import seaborn as sns
import pandas as pd

gender_data = pd.read_csv('./data/onlinefoods.csv')

html_count_by_age = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Gender Distribution by Age</h3></center>
</div>
"""
st.markdown(html_count_by_age, unsafe_allow_html=True)

plt.figure(figsize=(15, 5))
sns.countplot(x='Age', hue='Gender', data=gender_data)  # ใช้ countplot โดยกำหนด x เป็น 'Age' และ hue เป็น 'Gender'
plt.title('Gender Distribution by Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.xticks(rotation=45)
st.pyplot()

plt.figure(figsize=(15, 5))
sns.countplot(x='Gender', data=gender_data)  # แก้เป็น gender_data แทน shopping_trends.csv
plt.title('จำนวนเพศตามช่วงอายุ')
plt.xlabel('เพศ')
plt.ylabel('จำนวน')
plt.xticks(rotation=45)
st.pyplot()

html_sales_by_gender = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Sales by Gender</h3></center>
</div>
"""
st.markdown(html_sales_by_gender, unsafe_allow_html=True)

plt.figure(figsize=(15, 5))
sns.countplot(x='Gender', hue='Output', data=gender_data)  # ใช้ countplot โดยกำหนด x เป็น 'Gender' และ hue เป็น 'Output'
plt.title('Sales by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=45)
st.pyplot()




