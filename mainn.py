# password_meter_streamlit.py
import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", layout="centered")

st.title("🔐 Password Strength Meter")

# Password input (visible as dots)
password = st.text_input("Enter your password", type="password")

def check_password_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add a lowercase letter")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Add a number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Add a special character")

    return strength, suggestions

def show_strength_meter(strength):
    meter = ["[-----]", "[#----]", "[##---]", "[###--]", "[####-]", "[#####]"]
    label = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }
    st.markdown(f"**Strength Meter:** `{meter[strength]}` **({label[strength]})**")

if password:
    strength, suggestions = check_password_strength(password)
    show_strength_meter(strength)

    if strength < 5:
        st.warning("Suggestions to improve your password:")
        for s in suggestions:
            st.write(f"• {s}")
