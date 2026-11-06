import streamlit as st

st.title("Price Calculator")

price = st.number_input("Product Price", min_value=0.0, value=1000.0, step=10.0)
discount = st.slider("Discount Percentage", min_value=0, max_value=50, value=10)

if st.button("Calculate"):
    final_price = price - (price * discount / 100)
    st.success(f"Original Price: {price:.2f} | Discount: {discount}% | Final Price: {final_price:.2f}")
    st.table([["Before", "After"], [f"{price:.2f}", f"{final_price:.2f}"]])