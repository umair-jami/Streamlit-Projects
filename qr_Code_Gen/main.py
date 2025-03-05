import qrcode as qr
import streamlit as st
from io import BytesIO #For Showing img without saving it in the storage
from PIL import Image # For resizing image

st.title("QR Code Generator")

# Get user input for the QR code URL
url = st.text_input("Add QR URL")

if url:
    # Generate the QR code
    img = qr.make(url)

    # Convert QR code to PIL Image
    img = img.convert("RGB")

    # Resize to 200x200 pixels
    img = img.resize((400, 400), Image.Resampling.LANCZOS)

    # Save the image to a BytesIO object
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Display the resized QR code image
    st.image(buffer, caption="QR Code (200x200)", use_container_width=False)
