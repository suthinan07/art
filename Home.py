import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend which doesn't require a display
import matplotlib.pyplot as plt

import streamlit as st
import seaborn as sns
import pandas as pd

gender_data = pd.read_csv('./data/onlinefoods.csv')

html_count_by_age = "<center><h3>Gender Distribution by Age</h3></center>"

st.markdown(html_count_by_age, unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(15, 5))
sns.countplot(x='Age', hue='Gender', data=gender_data, ax=ax)
ax.set_title('Gender Distribution by Age')
ax.set_xlabel('Age')
ax.set_ylabel('Count')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Gender Distribution
html_gender_distribution = "<center><h3>Gender Distribution</h3></center>"
st.markdown(html_gender_distribution, unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(15, 5))
sns.countplot(x='Gender', data=gender_data, ax=ax)
ax.set_title('Gender Distribution')
ax.set_xlabel('Gender')
ax.set_ylabel('Count')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Sales by Gender
html_sales_by_gender = "<center><h3>Sales by Gender</h3></center>"
st.markdown(html_sales_by_gender, unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(15, 5))
sns.countplot(x='Gender', hue='Output', data=gender_data, ax=ax)
ax.set_title('Sales by Gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Count')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)