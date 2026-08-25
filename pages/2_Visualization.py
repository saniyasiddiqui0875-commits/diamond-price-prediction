import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diamonds.csv")

df = df.drop(columns=["Unnamed: 0"])

st.title("📊Diamond Data Visualization")

st.write("This page shows visualizations of the Diamond dataset")

st.subheader("Dataset Preview")

st.dataframe(df.head())

st.subheader("Distribution of Diamond Prices")

fig, ax = plt.subplots()

ax.hist(df["price"], bins=30)

ax.set_xlabel("Price")
ax.set_ylabel("Count")
ax.set_title("Distribution of Diamond Prices")

st.pyplot(fig)

st.subheader("Carat vs Price")

fig, ax = plt.subplots()

ax.scatter(df["carat"], df["price"], alpha=0.5)

ax.set_title("Carat vs Price")
ax.set_xlabel("Carat")
ax.set_ylabel("Price")

st.pyplot(fig)

st.subheader("Cut Distribution")

fig, ax = plt.subplots()

df["cut"].value_counts().plot(kind="bar", ax=ax)

ax.set_title("Cut Distribution")
ax.set_xlabel("Cut")
ax.set_ylabel("Count")

st.pyplot(fig)

st.subheader("Color Distribution")

fig, ax = plt.subplots()

df["color"].value_counts().plot(kind="bar", ax=ax)

ax.set_title("Color Distribution")
ax.set_xlabel("Color")
ax.set_ylabel("Count")

st.pyplot(fig)

st.subheader("Clarity Distribution")

fig, ax = plt.subplots()

df["clarity"].value_counts().plot(kind="bar", ax=ax)

ax.set_title("Clarity Distribution")
ax.set_xlabel("Clarity")
ax.set_ylabel("Count")

st.pyplot(fig)
