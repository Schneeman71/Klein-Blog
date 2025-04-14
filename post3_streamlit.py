import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Pandemic Gaming Trends Explorer")

@st.cache_data
def load_data():
    return pd.read_csv("steam_cleaned_dataset.csv", parse_dates=['Month'])

df = load_data()

st.sidebar.header("Filters")

games = st.sidebar.multiselect(
    "Select Game(s):",
    options=df["Game Title"].unique(),
    default=df["Game Title"].unique()
)

game_type = st.sidebar.radio(
    "Game Type:",
    options=["All", "Multiplayer", "Non-Multiplayer"],
    index=0
)

min_year = df["Month"].dt.year.min()
max_year = df["Month"].dt.year.max()
year_range = st.sidebar.slider("Select Year Range:", min_year, max_year, (min_year, max_year))

filtered_df = df[
    (df["Game Title"].isin(games)) &
    (df["Month"].dt.year >= year_range[0]) &
    (df["Month"].dt.year <= year_range[1])
]

if game_type != "All":
    filtered_df = filtered_df[filtered_df["Game Type"] == game_type]

tab1, tab2 = st.tabs(["Average Player Count", "Growth Rate (%)"])

with tab1:
    st.subheader("Monthly Average Player Count")
    fig1 = px.line(
        filtered_df,
        x="Month",
        y="Average Player Count",
        color="Game Title",
        markers=True,
        title="Player Count Over Time"
    )
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.subheader("Monthly Growth Rate (%)")
    fig2 = px.line(
        filtered_df,
        x="Month",
        y="Monthly Growth Rate",
        color="Game Title",
        markers=True,
        title="Growth Rate Over Time"
    )
    st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Filtered Data Table"):
    st.dataframe(filtered_df)

csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_steam_data.csv',
    mime='text/csv',
)
