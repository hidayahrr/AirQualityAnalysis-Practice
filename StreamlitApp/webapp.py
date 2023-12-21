import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv(r"C:\Users\1815\Downloads\Dicoding\Dashboard\all_data.csv")

st.title("Air Quality Analysis")

st.markdown(
    """
    These are the first visualizations I built on Streamlit.
    """
)

mean_co_by_year_station = all_df.groupby(['year', 'station'])['CO'].mean().unstack()

# Create a figure and plot on it
fig, ax = plt.subplots(figsize=(10, 5))

# Plot 3 garis untuk 3 station
for station in mean_co_by_year_station.columns:
    ax.plot(mean_co_by_year_station.index, mean_co_by_year_station[station], marker='o', linewidth=2, label=station)

    for i, txt in enumerate(mean_co_by_year_station[station]):
        ax.text(mean_co_by_year_station.index[i], txt, f'{txt:.2f}', ha='center', va='bottom', fontsize=8)

ax.set_title("Average CO in the Air between 2013-2017", loc="center", fontsize=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Avg CO", fontsize=12)
ax.legend()
ax.tick_params(axis='x', rotation=45, labelrotation="default", labelsize=10)
ax.tick_params(axis='y', labelsize=10)

st.pyplot(fig)

st.caption(
    """
As can be seen from the chart, average Carbon Monoxide containment in the air is pretty fluctuative. However, there's a steep 
incline in Gucheng throughout 2016 until 2017.
    """
)

mean_temp_by_month_station = all_df.groupby(['month', 'station'])['TEMP'].mean().unstack()


fig, ax = plt.subplots(figsize=(10, 5))

# Plot 3 garis untuk 3 station
for station in mean_temp_by_month_station.columns:
    plt.plot(mean_temp_by_month_station.index, mean_temp_by_month_station[station], marker='o', linewidth=2, label=station)
    
    for i, txt in enumerate(mean_temp_by_month_station[station]):
        plt.text(mean_temp_by_month_station.index[i], txt, f'{txt:.2f}', ha='center', va='top', fontsize=8)

ax.set_title("Average TEMP per Month for all year 2013-2017", loc="center", fontsize=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Avg TEMP", fontsize=12)
ax.legend()  
ax.tick_params(axis='x', rotation=45, labelrotation="default", labelsize=10)
ax.tick_params(axis='y', labelsize=10)

st.pyplot(fig)

st.caption(
    """
Average temperature of the air is very correlated for the 3 regions. Reaching the top in July, at their lowest on January.
    """
)

mean_rain_by_month_station = all_df.groupby(['month', 'station'])['RAIN'].mean().unstack()

fig, ax = plt.subplots(figsize=(10, 5))

# Plot 3 garis untuk 3 station
for station in mean_rain_by_month_station.columns:
    plt.plot(mean_rain_by_month_station.index, mean_rain_by_month_station[station], marker='o', linewidth=2, label=station)
    
    for i, txt in enumerate(mean_rain_by_month_station[station]):
        plt.text(mean_rain_by_month_station.index[i], txt, f'{txt:.2f}', ha='center', va='top', fontsize=8)

ax.set_title("Rataan curah hujan bulanan untuk all year 2013-2017", loc="center", fontsize=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Rerata curah hujan", fontsize=12)
ax.legend()  
ax.tick_params(axis = 'x', rotation=45, labelrotation="default", labelsize=10)
ax.tick_params(axis = 'y', labelsize=10)

st.pyplot(fig)

st.caption(
    """
Average rain intensity is pretty correlated for the 3 regions. Reaching the top in July, at their lowest on January and December
because it snows.
    """
)