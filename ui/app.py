import streamlit as st
import requests

st.set_page_config(page_title="Release Quality Demo", page_icon="✓")

st.title("Transaction Release Quality Demo")
st.caption("A small UI used to demonstrate critical-path release validation.")

api_url = st.sidebar.text_input("API URL", "http://127.0.0.1:8000")

st.header("Create transaction")

with st.form("transaction_form"):
    amount = st.number_input("Amount", min_value=0.0, value=100.0, step=10.0)
    source = st.text_input("Source account", "ACCOUNT-A")
    destination = st.text_input("Destination account", "ACCOUNT-B")
    key = st.text_input("Idempotency key", "ui-key-001")
    submitted = st.form_submit_button("Submit transaction")

if submitted:
    payload = {
        "amount": amount,
        "source": source,
        "destination": destination,
        "idempotency_key": key,
    }
    try:
        response = requests.post(f"{api_url}/transactions", json=payload, timeout=5)
        if response.status_code == 201:
            st.success(f"Transaction authorized: {response.json()['transaction_id']}")
        else:
            st.error(f"Request failed: {response.status_code} — {response.text}")
    except requests.RequestException as exc:
        st.error(f"API unavailable: {exc}")

st.divider()
st.header("Quality signals")
st.write("Critical flow: authentication → transaction → authorization → status.")
