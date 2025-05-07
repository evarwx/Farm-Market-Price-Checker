import streamlit as st
import google.generativeai as genai
import os
from datetime import date

# Set API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyD4WveSDzvsuoW_M-ovQ6ifh3HDZOW3_SM"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Title
st.title("🌾 Farm Market Price Checker (AI-Powered)")
st.write("Select your crop and region to get AI-generated market price insights.")

# Crop and Region Input
crops = [
    "Wheat", "Rice", "Onion", "Potato", "Tomato", "Maize", "Sugarcane", "Barley",
    "Pulses", "Cotton", "Soybean", "Groundnut", "Mustard", "Chickpeas", "Green Gram",
    "Jowar", "Bajra", "Sunflower", "Garlic", "Ginger"
]

# Expanded State List
states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
    "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
    "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
    "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]


# State → District Mapping
state_districts = {
    "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Nellore"],
    "Arunachal Pradesh": ["Itanagar", "Tawang", "Pasighat"],
    "Assam": ["Guwahati", "Dibrugarh", "Silchar", "Jorhat"],
    "Bihar": ["Patna", "Gaya", "Muzaffarpur", "Bhagalpur"],
    "Chhattisgarh": ["Raipur", "Bilaspur", "Durg", "Korba"],
    "Goa": ["Panaji", "Margao"],
    "Gujarat": ["Ahmedabad", "Surat", "Rajkot", "Vadodara"],
    "Haryana": ["Gurgaon", "Hisar", "Ambala", "Panipat"],
    "Himachal Pradesh": ["Shimla", "Mandi", "Dharamshala"],
    "Jharkhand": ["Ranchi", "Dhanbad", "Jamshedpur", "Bokaro"],
    "Karnataka": ["Bengaluru", "Mysuru", "Hubli", "Mangalore"],
    "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur"],
    "Maharashtra": ["Pune", "Mumbai", "Nagpur", "Nashik"],
    "Manipur": ["Imphal", "Churachandpur"],
    "Meghalaya": ["Shillong", "Tura"],
    "Mizoram": ["Aizawl", "Lunglei"],
    "Nagaland": ["Kohima", "Dimapur"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Puri"],
    "Punjab": ["Ludhiana", "Amritsar", "Jalandhar", "Patiala"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota"],
    "Sikkim": ["Gangtok", "Namchi"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar"],
    "Tripura": ["Agartala", "Udaipur"],
    "Uttar Pradesh": ["Lucknow", "Varanasi", "Kanpur", "Meerut"],
    "Uttarakhand": ["Dehradun", "Haridwar", "Nainital"],
    "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Siliguri"]
}



crop = st.selectbox("Select your crop", crops)
state = st.selectbox("Select your state", states)

# Show districts based on selected state
districts = state_districts.get(state, [])
if districts:
    district = st.selectbox("Select your district", districts)
else:
    district = st.text_input("Enter your district manually")

if st.button("Get Market Prices"):
    prompt = f"""
    You are a smart agriculture market assistant AI.

    A farmer from *{state}* is selling *{crop}* today ({date.today().strftime('%Y-%m-%d')}).
    Give an estimated market price report for this crop in that region.

    Return response in the following format:

    - *Crop*:
    - *State*:
    - *Market Name* (you can make a relevant market name based on the state):
    - *Date*:
    - *Minimum Price (₹/quintal)*:
    - *Maximum Price (₹/quintal)*:
    - *Modal Price (₹/quintal)*:
    - *Confidence Level*:
    """

    with st.spinner("Analyzing and fetching results..."):
        response = model.generate_content(prompt)
        st.success("Here is the estimated price data:")
        st.markdown(response.text.strip())
        
        # Sidebar
st.sidebar.title("🌿 Farmer's Assistant")

# Contact Info
contact_number = st.sidebar.text_input("📞 Your Contact Number")

# About Us Section
st.sidebar.markdown("### 📘 About Us")
st.sidebar.info("""
This app provides AI-generated market price insights for Indian farmers.


""")

# Contact Section
st.sidebar.markdown("### 📬 Need Help?")
st.sidebar.write("Email: support@farmpriceai.in")
st.sidebar.write("WhatsApp: +91-8759349583")
