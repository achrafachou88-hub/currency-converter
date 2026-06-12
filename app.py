import streamlit as st
import requests

# إعداد واجهة الموقع
st.set_page_config(page_title="Global Currency Converter", layout="centered")
st.title("🌍 تحويل العملات العالمي لجميع الدول")

# قاموس شامل بجميع عملات دول العالم مع أعلامها
currencies = {
    "🇩🇿 DZD - الدينار الجزائري": "DZD",
    "🇺🇸 USD - الدولار الأمريكي": "USD",
    "🇪🇺 EUR - اليورو الأوروبي": "EUR",
    "🇬🇧 GBP - الجنيه الإسترليني": "GBP",
    "🇨🇦 CAD - الدولار الكندي": "CAD",
    "🇯🇵 JPY - الين الياباني": "JPY",
    "🇸🇦 SAR - الريال السعودي": "SAR",
    "🇦🇪 AED - الدرهم الإماراتي": "AED",
    "🇪🇬 EGP - الجنيه المصري": "EGP",
    "🇶🇦 QAR - الريال القطري": "QAR",
    "🇰🇼 KWD - الدينار الكويتي": "KWD",
    "🇧🇭 BHD - الدينار البحريني": "BHD",
    "🇴🇲 OMR - الريال العماني": "OMR",
    "🇯🇴 JOD - الدينار الأردني": "JOD",
    "🇹🇳 TND - الدينار التونسي": "TND",
    "🇲🇦 MAD - الدرهم المغربي": "MAD",
    "🇹🇷 TRY - الليرة التركية": "TRY",
    "🇨🇳 CNY - اليوان الصيني": "CNY",
    "🇦🇺 AUD - الدولار الأسترالي": "AUD",
    "🇨🇭 CHF - الفرنك السويسري": "CHF",
    "🇮🇳 INR - الروبية الهندية": "INR",
    "🇷🇺 RUB - الروبل الروسي": "RUB",
    "🇰🇷 KRW - الوون الكوري الجنوبي": "KRW",
    "🇧🇷 BRL - الريال البرازيلي": "BRL",
    "🇲🇽 MXN - البيزو المكسيكي": "MXN",
    "🇿🇦 ZAR - الراند الجنوب أفريقي": "ZAR",
    "🇸🇬 SGD - الدولار السنغافوري": "SGD",
    "🇳🇿 NZD - الدولار النيوزيلندي": "NZD",
    "🇸🇪 SEK - الكرونا السويدية": "SEK",
    "🇳🇴 NOK - الكرونا النرويجية": "NOK",
    "🇩🇰 DKK - الكرونا الدنماركية": "DKK",
    "🇵🇱 PLN - الزلوتي البولندي": "PLN",
    "🇭🇺 HUF - الفورنت المجري": "HUF",
    "🇨🇿 CZK - الكورونا التشيكية": "CZK",
    "🇷🇴 RON - الليو الروماني": "RON",
    "🇧🇬 BGN - الليف البلغاري": "BGN",
    "🇭🇰 HKD - دولار هونج كونج": "HKD",
    "🇮🇩 IDR - الروبية الإندونيسية": "IDR",
    "🇲🇾 MYR - الرينجيت الماليزي": "MYR",
    "🇵🇭 PHP - البيزو الفلبيني": "PHP",
    "🇹🇭 THB - البات التايلاندي": "THB",
    "🇻🇳 VND - الدونج الفيتنامي": "VND",
    "🇵🇰 PKR - الروبية الباكستانية": "PKR",
    "🇱KR LKR - الروبية السريلانكية": "LKR",
    "🇰🇿 KZT - التينغ الكازاخستاني": "KZT",
    "🇰🇪 KES - الشلن الكيني": "KES",
    "🇳🇬 NGN - النيرا النيجيري": "NGN",
    "🇦🇷 ARS - البيزو الأرجنتيني": "ARS",
    "🇨🇱 CLP - البيزو التشيلي": "CLP",
    "🇨🇴 COP - البيزو الكولومبي": "COP",
    "🇵🇪 PEN - سول بيروفي": "PEN",
    "🇺🇾 UYU - البيزو الأوروغواياني": "UYU"
}

# تصميم الحقول
amount = st.number_input("أدخل المبلغ:", value=1.0, min_value=0.0)

from_curr = st.selectbox("من:", list(currencies.keys()))
to_curr = st.selectbox("إلى:", list(currencies.keys()))

if st.button("تحويل الآن"):
    from_code = currencies[from_curr]
    to_code = currencies[to_curr]
    
    if from_code == to_code:
        st.warning("يرجى اختيار عملتين مختلفتين للتحويل.")
    else:
        try:
            # جلب أسعار العملات باستخدام API موثوق ومجاني
            url = f"https://api.exchangerate-api.com/v4/latest/{from_code}"
            response = requests.get(url)
            data = response.json()
            
            rate = data['rates'][to_code]
            result = amount * rate
            
            st.success(f"✅ {amount} {from_code} = {result:.2f} {to_code}")
        except Exception as e:
            st.error("حدث خطأ أثناء جلب سعر التحويل، تأكد من اتصالك بالإنترنت أو جرب عملة أخرى.")