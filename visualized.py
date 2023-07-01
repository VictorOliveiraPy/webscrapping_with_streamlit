import subprocess

import pandas as pd
import requests
import streamlit as st

from repository.database import TransactionsTable

repository = TransactionsTable()


def extract_data():
    repository.create_table()
    subprocess.call(["scrapy", "crawl", "ml", "-o", "data.csv", "-t", "csv"])


def display_data():
    r = requests.get("http://localhost:9000/items").json()
    df = pd.DataFrame(r)
    st.dataframe(df)


if st.button('Extract Data - Mercado Livre'):
    st.text("Loading...")
    extract_data()


if st.button('Display data - Mercado Livre'):
    st.text("Dados de ofertas do mercado livre")
    display_data()
