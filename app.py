
import streamlit as st
from collections import Counter
import string

st.set_page_config(
    page_title="DECRYPTIQ",
    page_icon="🔐",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #101010;
    color: #f4f0e8;
}
[data-testid="stSidebar"] {
    background: #1b1b1b;
}
h1, h2, h3 {
    color: #e8b45a !important;
}
.stButton button {
    background: #e8b45a;
    color: #111111;
    border: none;
    font-weight: bold;
}
.stTextArea textarea, .stTextInput input {
    background: #242424;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    key = ''.join(c.upper() for c in key if c.isalpha() and c.isascii())
    if not key:
        return "Please enter a valid alphabetic key."
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

st.title("⌁ DECRYPTIQ")
st.caption("SMART DECRYPTION & CRYPTANALYSIS LAB")
st.markdown("---")

st.sidebar.title("DECRYPTIQ")
st.sidebar.caption("Developed by Mradul Sharma")
page = st.sidebar.radio(
    "NAVIGATION",
    ["Decrypt Workspace", "Caesar Brute Force",
     "Frequency Analyzer", "Cipher Learning Lab", "About Project"]
)

if page == "Decrypt Workspace":
    st.header("Decryption Workspace")
    cipher = st.selectbox("Choose Cipher", ["Caesar Cipher", "Vigenere Cipher"])
    message = st.text_area("Enter ciphertext", placeholder="Type your encrypted message here...")
    
    if cipher == "Caesar Cipher":
        shift = st.slider("Shift value", 0, 25, 3)
        if st.button("DECRYPT MESSAGE"):
            st.success("Decryption complete")
            st.code(caesar_decrypt(message, shift))
    else:
        key = st.text_input("Secret key", placeholder="Enter keyword")
        if st.button("DECRYPT MESSAGE"):
            st.code(vigenere_decrypt(message, key))

elif page == "Caesar Brute Force":
    st.header("Caesar Cipher — Brute Force")
    st.write("Try every possible shift for a Caesar cipher.")
    message = st.text_area("Enter ciphertext", placeholder="Example: Khoor Zruog")
    if st.button("TRY ALL SHIFTS"):
        for shift in range(26):
            st.write(f"**Shift {shift}:** {caesar_decrypt(message, shift)}")

elif page == "Frequency Analyzer":
    st.header("Letter Frequency Analyzer")
    message = st.text_area("Paste text to analyze")
    if st.button("ANALYZE TEXT"):
        letters = [c.upper() for c in message if c.isascii() and c.isalpha()]
        if letters:
            counts = Counter(letters)
            st.bar_chart({letter: counts.get(letter, 0) for letter in string.ascii_uppercase})
            st.write("Letter counts:", dict(sorted(counts.items())))
        else:
            st.warning("Please enter some alphabetic text.")

elif page == "Cipher Learning Lab":
    st.header("Cipher Learning Lab")
    st.subheader("Caesar Cipher")
    st.write("A substitution cipher that shifts each letter by a fixed number.")
    st.code("Plaintext: HELLO\nShift: 3\nCiphertext: KHOOR")
    st.subheader("Vigenere Cipher")
    st.write("Uses a repeating keyword to apply different letter shifts.")
    st.info("These tools demonstrate classical ciphers. They do not automatically decrypt arbitrary ciphertext or break modern AES encryption.")

else:
    st.header("About DECRYPTIQ")
    st.write("DECRYPTIQ is an educational cryptography project for learning classical encryption, decryption and basic frequency analysis.")
    st.write("**Developed by Mradul Sharma**")
    st.write("Technology: Python and Streamlit")
    st.caption("Educational use only — not a modern encryption-breaking tool.")

st.markdown("---")
st.caption("DECRYPTIQ  •  Cryptography Learning Project  •  Developed by Mradul Sharma")
