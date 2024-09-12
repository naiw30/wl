import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
money = pd.read_csv("money_data7.csv")

# User input for year selection
option = st.selectbox('Choose a year:', ('2020', '2021', '2022'))
option2 = int(option)

st.write('You selected:', option)

# Filter data for the selected year
filtered_money = money[money['A_YEAR'] == option2]

# Define plot settings
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
months = filtered_money['A_MONTH']

# Plot American rate
axs[0, 0].plot(months, filtered_money['A_RATE'], color='red', marker='o')
axs[0, 0].set_title('America rate')
axs[0, 0].set_xticks(months)

# Plot Korean rate
axs[0, 1].plot(months, filtered_money['K_RATE'], color='blue', marker='o')
axs[0, 1].set_title('Korea rate')
axs[0, 1].set_xticks(months)

# Plot Kospi rate
axs[1, 0].plot(months, filtered_money['KOSPI'], color='green', marker='o')
axs[1, 0].set_title('Kospi Rate')
axs[1, 0].set_xticks(months)

# Plot House price
axs[1, 1].plot(months, filtered_money['HOUSE_PRICE'], color='yellow', marker='o')
axs[1, 1].set_title('House Price')
axs[1, 1].set_xticks(months)

# Adjust layout
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)
