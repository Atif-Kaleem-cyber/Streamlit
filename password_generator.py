import streamlit as st
import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_numbers=True, use_symbols=True):
    # Define character sets
    lowercase = string.ascii_lowercase if use_lowercase else ''
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine all selected character sets
    all_characters = lowercase + uppercase + numbers + symbols
    
    if not all_characters:
        return "Please select at least one character type!"
    
    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    st.set_page_config(
        page_title="Password Generator",
        page_icon="🔐",
        layout="centered"
    )
    
    st.title("🔐 Password Generator")
    st.write("Generate secure passwords with customizable options!")
    
    # Password options
    with st.container():
        st.subheader("Password Options")
        col1, col2 = st.columns(2)
        
        with col1:
            length = st.slider("Password Length", min_value=4, max_value=50, value=12)
            use_lowercase = st.checkbox("Include Lowercase (a-z)", value=True)
            use_uppercase = st.checkbox("Include Uppercase (A-Z)", value=True)
        
        with col2:
            use_numbers = st.checkbox("Include Numbers (0-9)", value=True)
            use_symbols = st.checkbox("Include Symbols (!@#$%^&*)", value=True)
    
    # Generate password button
    if st.button("Generate Password", type="primary"):
        password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols)
        
        if "Please select" in password:
            st.error(password)
        else:
            st.success("Your generated password:")
            st.code(password, language=None)
            
            # Copy button
            st.button("📋 Copy to Clipboard", 
                     help="Click to copy the password",
                     on_click=lambda: st.write(
                         f'<script>navigator.clipboard.writeText("{password}");</script>',
                         unsafe_allow_html=True
                     ))
    
    # Password strength indicators
    with st.expander("Password Strength Guidelines"):
        st.markdown("""
        - **Weak**: Less than 8 characters
        - **Medium**: 8-11 characters with a mix of different character types
        - **Strong**: 12+ characters with a mix of lowercase, uppercase, numbers, and symbols
        
        Tips for strong passwords:
        1. Use both uppercase and lowercase letters
        2. Include numbers and special characters
        3. Make it at least 12 characters long
        4. Avoid using personal information
        """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "Made with ❤️ using Streamlit"
    )

if __name__ == "__main__":
    main() 