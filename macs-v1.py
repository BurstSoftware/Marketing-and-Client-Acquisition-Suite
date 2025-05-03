import streamlit as st
import qrcode
from PIL import Image
import io
import pandas as pd
import plotly.express as px

# Streamlit page configuration
st.set_page_config(page_title="Marketing & Client Acquisition Suite", layout="wide")

# Title
st.title("Marketing & Client Acquisition Suite")
st.markdown("A comprehensive tool for growing your business through marketing and competitive positioning.")

# Sidebar for navigation
st.sidebar.header("Navigation")
tool = st.sidebar.selectbox("Select Tool", [
    "AI Advertising Writer",
    "Business Marketing Checklist",
    "Competitive Analysis Dashboard",
    "Static QR Code Generator"
])

# AI Advertising Writer
if tool == "AI Advertising Writer":
    st.header("AI Advertising Writer")
    st.markdown("Generate tailored ad copy for your target audience.")
    
    audience = st.text_input("Target Audience (e.g., Young Professionals, Small Business Owners):")
    product = st.text_input("Product/Service (e.g., Coffee Shop, Online Course):")
    tone = st.selectbox("Tone", ["Professional", "Casual", "Persuasive", "Friendly"])
    
    if st.button("Generate Ad Copy"):
        if audience and product:
            # Simulated AI-generated ad copy (replace with actual AI model integration if available)
            ad_copy = f"Discover {product} tailored for {audience}! With a {tone.lower()} approach, we bring you the best in quality and value. Act now and elevate your experience!"
            st.success("Generated Ad Copy:")
            st.write(ad_copy)
        else:
            st.error("Please fill in all fields.")

# Business Marketing Checklist
elif tool == "Business Marketing Checklist":
    st.header("Business Marketing Checklist")
    st.markdown("Ensure a systematic marketing strategy across multiple channels.")
    
    checklist = {
        "Social Media Campaign": False,
        "Email Marketing": False,
        "SEO Optimization": False,
        "Content Creation": False,
        "Paid Advertising": False,
        "Local Promotions": False
    }
    
    st.subheader("Marketing Tasks")
    for task in checklist:
        checklist[task] = st.checkbox(task, value=checklist[task])
    
    completed = sum(checklist.values())
    total = len(checklist)
    st.progress(completed / total)
    st.write(f"Progress: {completed}/{total} tasks completed")
    
    if st.button("Download Checklist"):
        checklist_status = "\n".join([f"{task}: {'Completed' if status else 'Pending'}" for task, status in checklist.items()])
        st.download_button("Download Checklist", checklist_status, "marketing_checklist.txt")

# Competitive Analysis Dashboard
elif tool == "Competitive Analysis Dashboard":
    st.header("Competitive Analysis Dashboard")
    st.markdown("Analyze competitors' strengths and weaknesses to inform your strategy.")
    
    # Sample competitor data (replace with user-uploaded or dynamic data)
    competitors = st.text_area("Enter competitors (one per line):", "Competitor A\nCompetitor B\nCompetitor C")
    competitors_list = [c.strip() for c in competitors.split("\n") if c.strip()]
    
    if competitors_list:
        # Simulated data for competitors
        data = {
            "Competitor": competitors_list,
            "Pricing": [50, 45, 60],
            "Market Share (%)": [30, 25, 20],
            "Customer Rating": [4.5, 4.0, 3.8]
        }
        df = pd.DataFrame(data)
        
        st.subheader("Competitor Metrics")
        st.dataframe(df)
        
        # Plotly chart for visualization
        fig = px.bar(df, x="Competitor", y=["Pricing", "Market Share (%)", "Customer Rating"],
                     barmode="group", title="Competitor Analysis")
        st.plotly_chart(fig)
        
        # Download data
        csv = df.to_csv(index=False)
        st.download_button("Download Competitor Data", csv, "competitor_analysis.csv", "text/csv")

# Static QR Code Generator
elif tool == "Static QR Code Generator":
    st.header("Static QR Code Generator")
    st.markdown("Create QR codes linking to landing pages or promotions.")
    
    url = st.text_input("Enter URL for QR Code (e.g., https://yourwebsite.com):")
    
    if st.button("Generate QR Code"):
        if url:
            # Generate QR code
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save image to bytes
            img_bytes = io.BytesIO()
            img.save(img_bytes, format="PNG")
            img_bytes.seek(0)
            
            # Display QR code
            st.image(img_bytes, caption="Generated QR Code", use_column_width=False)
            
            # Download QR code
            st.download_button("Download QR Code", img_bytes, "qr_code.png", "image/png")
        else:
            st.error("Please enter a valid URL.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Streamlit for small businesses.")
