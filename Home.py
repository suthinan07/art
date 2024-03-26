import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend which doesn't require a display
import matplotlib.pyplot as plt

import streamlit as st
import seaborn as sns
import pandas as pd

gender_data = pd.read_csv('./data/onlinefoods.csv')

# Gender Distribution by Age
html_count_by_age = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Gender Distribution by Age</h3></center>
</div>
"""
st.markdown(html_count_by_age, unsafe_allow_html=True)

plt.figure(figsize=(15, 5))
sns.countplot(x='Age', hue='Gender', data=gender_data)
plt.title('Gender Distribution by Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.xticks(rotation=45)
st.pyplot()

# Gender Distribution
html_gender_distribution = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Gender Distribution</h3></center>
</div>
"""
st.markdown(html_gender_distribution, unsafe_allow_html=True)

plt.figure(figsize=(15, 5))
sns.countplot(x='Gender', data=gender_data)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=45)
st.pyplot()

# Sales by Gender
html_sales_by_gender = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Sales by Gender</h3></center>
</div>
"""
st.markdown(html_sales_by_gender, unsafe_allow_html=True)

plt.figure(figsize=(15, 5))
sns.countplot(x='Gender', hue='Output', data=gender_data)
plt.title('Sales by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=45)
st.pyplot()




