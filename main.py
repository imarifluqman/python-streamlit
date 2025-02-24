import streamlit as st
import requests


st.set_page_config(page_title="Home", page_icon="🏠")

API_URL = "https://fakestoreapi.com/products"

# Function to fetch products
def fetch_products():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return []

# Initialize cart in session state
if "cart" not in st.session_state:
    st.session_state.cart = []

# Function to add item to cart
def add_to_cart(product):
    st.session_state.cart.append(product)


# Function to remove item from cart
def remove_from_cart(product):
    if product in st.session_state.cart:
        st.session_state.cart.remove(product)

# Fetch products
products = fetch_products()

# UI Layout
st.title("🛒 E-Commerce Store")

# Tabs for Products & Cart
tab1, tab2 = st.tabs(["🛍️ Products", f"🛒 Cart {len(st.session_state.cart) if st.session_state.cart else ''}" ])

# Products Page
with tab1:
    st.subheader("Available Products")
    cols = st.columns(4)
    
    # Display products
    for index, product in enumerate(products):
        with cols[index % 4]:
            with st.container(border=True,):
                st.image(product["image"], width=250)
                st.write(f"**{product['title']}**")
                st.write(f"💲 {product['price']}")
                if st.button("Add to Cart", key=f"add_{product['id']}"):
                    add_to_cart(product)
                    st.rerun()
                
                
    
    
name, phone, address, order_placed = "", "", "", False
# Cart Page
with tab2:
    st.subheader("Your Shopping Cart")
    
    if st.session_state.cart:
        total_price = 0
        for product in st.session_state.cart:
            st.image(product["image"], width=200)
            st.write(f"**{product['title']}** - 💲{product['price']}")
            total_price += product["price"]
            if st.button("Remove", key=f"remove_{product['id']}"):
                remove_from_cart(product)
                st.rerun()
        
        st.write(f"### 🏷️ Total: 💲{total_price}")
        
        
        st.divider()
        st.subheader("Enter your details to place order:")
        with st.form("order_form"):
            name = st.text_input("Enter your name", key="name")
            mobile = st.text_input("Enter your phone number", key="phone")
            address = st.text_input("Enter your address", key="address")
            order_placed = st.form_submit_button("Place Order")
            
        if order_placed:
            st.write("🎉 Order Placed Successfully!")
            st.write(f"Name: {name}")
            st.write(f"Phone: {mobile}")
            st.write(f"📦 Order will be delivered to {address}")
            
    else:
        st.write("🛒 Your cart is empty!")
 
