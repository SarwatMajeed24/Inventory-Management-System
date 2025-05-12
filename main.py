
import streamlit as st
from typing import Any
from models.inventory import Inventory
from models.product import Product
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing

DATA_FILE = "main.json"  # Default file for save/load

# Initialize inventory in session state
if 'inventory' not in st.session_state:
    st.session_state.inventory = Inventory()

inv: Inventory = st.session_state.inventory

st.title("📦 Inventory Management System")

if "loaded_file_name" in st.session_state:
    st.info(f"📁 Current file: `{st.session_state.loaded_file_name}`")

menu = ["Add Product", "View Products", "Sell Product", "Restock Product", "Save", "Load"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Product":
    p_type = st.selectbox("Product Type", ["Electronics", "Grocery", "Clothing"])
    pid = st.text_input("Product ID")
    name = st.text_input("Name")
    price = st.number_input("Price", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=0, step=1)

    extra: dict[str, Any] = {}

    if p_type == "Electronics":
        extra["brand"] = st.text_input("Brand")
        extra["warranty"] = int(st.number_input("Warranty (Years)", min_value=0, step=1))
    elif p_type == "Grocery":
        extra["expiry"] = st.date_input("Expiry Date").strftime("%Y-%m-%d")
    elif p_type == "Clothing":
        extra["size"] = st.text_input("Size")
        extra["material"] = st.text_input("Material")

    if st.button("Add Product"):
        if pid and name and quantity >= 0:
            try:
                prod: Product
                if p_type == "Electronics":
                    prod = Electronics(pid, name, float(price), int(quantity), extra["warranty"], extra["brand"])
                elif p_type == "Grocery":
                    prod = Grocery(pid, name, float(price), int(quantity), extra["expiry"])
                elif p_type == "Clothing":
                    prod = Clothing(pid, name, float(price), int(quantity), extra["size"], extra["material"])
                else:
                    raise ValueError("Invalid product type selected.")

                inv.add_product(prod)
                st.success("✅ Product added successfully.")
            except Exception as e:
                st.error(f"❌ {str(e)}")
        else:
            st.warning("Please fill in all fields.")

elif choice == "View Products":
    st.subheader("📋 Current Inventory")
    products = inv.list_all_products()
    if not products:
        st.info("No products in inventory.")
    else:
        for prod in products:
            st.text(str(prod))

elif choice == "Sell Product":
    pid_input = st.text_input("Product ID")
    qty_input = st.number_input("Quantity", min_value=1, step=1)
    if st.button("Sell"):
        if pid_input:
            try:
                inv.sell_product(pid_input, int(qty_input))
                st.success("✅ Product sold.")
            except Exception as e:
                st.error(f"❌ {str(e)}")
        else:
            st.warning("Please enter a valid product ID.")

elif choice == "Restock Product":
    pid_input = st.text_input("Product ID")
    qty_input = st.number_input("Restock Amount", min_value=1, step=1)
    if st.button("Restock"):
        if pid_input:
            try:
                inv.restock_product(pid_input, int(qty_input))
                st.success("✅ Product restocked.")
            except Exception as e:
                st.error(f"❌ {str(e)}")
        else:
            st.warning("Please enter a valid Product ID.")

elif choice == "Save":
    filename_input = st.text_input("Save As", value=DATA_FILE)
    if st.button("Save Inventory"):
        if filename_input:
            try:
                inv.save_to_file(filename_input)
                st.session_state["loaded_file_name"] = filename_input
                st.success(f"💾 Inventory saved to `{filename_input}`.")
            except Exception as e:
                st.error(f"❌ Error saving inventory: {str(e)}")
        else:
            st.warning("Please enter a filename.")

elif choice == "Load":
    filename_input = st.text_input("Load From", value=DATA_FILE)
    if st.button("Load Inventory"):
        if filename_input:
            try:
                inv.load_from_file(filename_input)
                st.session_state["loaded_file_name"] = filename_input
                st.success(f"📂 Inventory loaded from `{filename_input}`.")
            except Exception as e:
                st.error(f"❌ Error loading inventory: {str(e)}")
        else:
            st.warning("Please enter a filename.")
