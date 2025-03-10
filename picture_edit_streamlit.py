import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("Picture Edit App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    st.write("")
    st.write("Removing background...")
    
    output = remove(image)
    
    st.image(output, caption='Edited Image.', use_column_width=True)
    
    buf = io.BytesIO()
    output.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="Download Edited Image",
        data=byte_im,
        file_name="edited_image.png",
        mime="image/png"
    )