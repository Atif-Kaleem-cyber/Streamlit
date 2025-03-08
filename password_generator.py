import streamlit as st
import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters if use_letters else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine all selected character sets
    all_characters = letters + numbers + symbols
    
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
            use_letters = st.checkbox("Include Letters (A-Z, a-z)", value=True)
        
        with col2:
            use_numbers = st.checkbox("Include Numbers (0-9)", value=True)
            use_symbols = st.checkbox("Include Symbols (!@#$%^&*)", value=True)
    
    # Generate password button
    if st.button("Generate Password", type="primary"):
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
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
        - **Medium**: 8-11 characters with a mix of letters and numbers
        - **Strong**: 12+ characters with a mix of letters, numbers, and symbols
        
        Tips for strong passwords:
        1. Use a mix of uppercase and lowercase letters
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