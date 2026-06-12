import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter", layout="centered")

st.title("💱 Global Live Currency Converter")

# قاموس العملات مع أعلام الدول الحقيقية
currencies_dict = {
    "USD": "🇺🇸 United States (USD) - US Dollar",
    "DZD": "🇩🇿 Algeria (DZD) - Algerian Dinar",
    "EUR": "🇪🇺 European Union (EUR) - Euro",
    "GBP": "🇬🇧 United Kingdom (GBP) - British Pound",
    "CAD": "🇨🇦 Canada (CAD) - Canadian Dollar",
    "AED": "🇦🇪 United Arab Emirates (AED) - UAE Dirham",
    "SAR": "🇸🇦 Saudi Arabia (SAR) - Saudi Riyal",
    "TRY": "🇹🇷 Turkey (TRY) - Turkish Lira",
    "CNY": "🇨🇳 China (CNY) - Chinese Yuan"
}

url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(url)
    data = response.json()
    rates = data['rates']
    
    display_list = [currencies_dict[c] for c in rates.keys() if c in currencies_dict]
    
    col1, col2 = st.columns(2)
    with col1:
        selected_from = st.selectbox("From", display_list, index=display_list.index("🇺🇸 United States (USD) - US Dollar"))
    with col2:
        selected_to = st.selectbox("To", display_list, index=display_list.index("🇩🇿 Algeria (DZD) - Algerian Dinar"))
        
    amount = st.number_input("Amount", value=1.0)
    
    if st.button("Convert"):
        # استخراج رمز العملة (أول كلمة بعد العلم مباشرة)
        base_currency = selected_from.split()[1]
        target_currency = selected_to.split()[1]
        
        amount_in_usd = amount / rates[base_currency]
        final_amount = amount_in_usd * rates[target_currency]
        
        st.success(f"Result: {amount} {base_currency} = **{final_amount:.2f}** {target_currency}")

except Exception as e:
    st.error("Error loading data. Please check your internet connection.")