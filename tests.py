import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from prospects;", ttl=600)

st.write(df)