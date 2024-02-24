import streamlit as st

def currency_converter(amount, from_currency, to_currency):
    # Conversion rates (for simplicity, rates are hardcoded)
    rates = {'USD': 1.0, 'EUR': 0.87, 'PKR': 279.13}
    
    # Convert the amount to USD first
    usd_amount = amount / rates[from_currency]
    
    # Convert the USD amount to the target currency
    result = usd_amount * rates[to_currency]
    
    return result

def main():
    st.title("Currency Converter")
    
    amount = st.number_input("Enter amount:", min_value=0.01, step=0.01)
    from_currency = st.selectbox("From Currency:", options=['USD', 'EUR', 'PKR'])
    to_currency = st.selectbox("To Currency:", options=['USD', 'EUR', 'PKR'])
    
    if st.button("Convert"):
        converted_amount = currency_converter(amount, from_currency, to_currency)
        st.success(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
