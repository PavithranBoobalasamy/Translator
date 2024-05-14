import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Title of the app
st.title("Simple Translator")

# Text input box for user to enter text to translate
text_to_translate = st.text_area("Enter text to translate", "")

# Selectbox for choosing target language
target_language = st.selectbox("Select target language", ["English", "French", "Spanish", "German", "Chinese", "Japanese"])

# Translate button
if st.button("Translate"):
    # Translate the input text to the selected language
    if target_language == "English":
        translated_text = translator.translate(text_to_translate, src='auto', dest='en').text
    elif target_language == "French":
        translated_text = translator.translate(text_to_translate, src='auto', dest='fr').text
    elif target_language == "Spanish":
        translated_text = translator.translate(text_to_translate, src='auto', dest='es').text
    elif target_language == "German":
        translated_text = translator.translate(text_to_translate, src='auto', dest='de').text
    elif target_language == "Chinese":
        translated_text = translator.translate(text_to_translate, src='auto', dest='zh-CN').text
    elif target_language == "Japanese":
        translated_text = translator.translate(text_to_translate, src='auto', dest='ja').text

    # Display the translated text
    st.write("Translated text:")
    st.write(translated_text)
