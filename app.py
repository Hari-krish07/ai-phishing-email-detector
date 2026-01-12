import streamlit as st
import joblib

# Load model and vectorizer (cached for performance)
@st.cache_resource
def load_artifacts():
    model = joblib.load('models/phishing_model.joblib')
    vectorizer = joblib.load('models/vectorizer.joblib')
    return model, vectorizer

model, vectorizer = load_artifacts()

# Page config
st.set_page_config(
    page_title="AI Phishing Email Detector",
    layout="centered"
)

# Header
st.title("🔍 AI Phishing Email Detector")  # 1️⃣ Header emoji
st.caption("Machine Learning–based phishing detection using Logistic Regression")

st.markdown(
    """
    **Model details**
    - Accuracy: **96.24%**
    - Dataset: **18,000+ emails**
    - Focus: High phishing recall for security use cases
    """
)

st.divider()

# Input
email_text = st.text_area(
    label="📧 Email Content",  # 2️⃣ Input emoji
    height=220,
    placeholder="Paste the full email content here for analysis..."
)

# Action
if st.button("🚀 Analyze Email"):  # 3️⃣ Button emoji
    if not email_text.strip():
        st.warning("⚠️ Please paste an email before analysis.")
    else:
        with st.spinner("Analyzing email content..."):
            X = vectorizer.transform([email_text])
            pred = model.predict(X)[0]
            confidence = model.predict_proba(X)[0][pred] * 100

        st.divider()

        if pred == 1:
            st.error("🚨 Phishing Email Detected")  # 4️⃣ Result emoji
        else:
            st.success("✅ Email Appears Safe")     # 5️⃣ Result emoji

        st.markdown(f"**Confidence:** {confidence:.1f}%")

        st.markdown(
            """
            **Interpretation**
            - High confidence indicates strong model certainty
            - Designed to minimize missed phishing attempts
            """
        )

# Footer
st.divider()
st.caption("Built by Hari | AI Phishing Detector")
