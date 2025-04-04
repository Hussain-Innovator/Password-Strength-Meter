import streamlit as st
import re

def check_password_strength(password):
    strength_score = 0

    # Length Check
    if len(password) < 6:
        return "Weak", "Password too short! Use at least 6 characters."
    elif len(password) >= 10:
        strength_score += 2
    else:
        strength_score += 1

    # Check for Character Variety
    if re.search(r"[a-z]", password):  # Lowercase
        strength_score += 1
    if re.search(r"[A-Z]", password):  # Uppercase
        strength_score += 1
    if re.search(r"[0-9]", password):  # Numbers
        strength_score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Special Characters
        strength_score += 1

    # Check for common patterns
    common_patterns = ["password", "123456", "qwerty", "abc123", "letmein"]
    for pattern in common_patterns:
        if pattern in password.lower():
            return "Weak", "Avoid common passwords like 'password123'."

    # Determine strength level
    if strength_score <= 2:
        return "Weak", "Try adding numbers, uppercase letters, and special characters."
    elif strength_score == 3 or strength_score == 4:
        return "Moderate", "Good, but consider making it longer and adding special characters."
    else:
        return "Strong", "Great job! Your password is strong. 🎉"

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, suggestion = check_password_strength(password)
    
    # Color-coded message
    if strength == "Weak":
        st.error(f"❌ {strength}: {suggestion}")
    elif strength == "Moderate":
        st.warning(f"⚠️ {strength}: {suggestion}")
    else:
        st.success(f"✅ {strength}: {suggestion}")
