import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def create_quote_image(quote_text):
    # Create an image
    img_width, img_height = 800, 400
    img = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", size=40)
    except IOError:
        font = ImageFont.load_default()

    # Calculate text size and position
    text_width, text_height = draw.textsize(quote_text, font=font)
    text_x = (img_width - text_width) // 2
    text_y = (img_height - text_height) // 2

    # Add text to the image
    draw.text((text_x, text_y), quote_text, fill="black", font=font)

    return img

# Streamlit app
st.title("Quote to Image Generator")

# Input field for the quote
quote = st.text_input("Enter your quote:")

if st.button("Generate Image"):
    if quote.strip():
        # Create the image
        image = create_quote_image(quote)

        # Display the image
        st.image(image, caption="Your Quote Image", use_column_width=True)

        # Option to download the image
        img_path = "quote_image.png"
        image.save(img_path)
        with open(img_path, "rb") as file:
            btn = st.download_button(
                label="Download Image",
                data=file,
                file_name="quote_image.png",
                mime="image/png"
            )
    else:
        st.warning("Please enter a quote!")