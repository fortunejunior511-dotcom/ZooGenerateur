import streamlit as st
import requests
import io
from PIL import Image

st.set_page_config(page_title="ZooGénérateur Pro", page_icon="🦁")

# Style pour le bouton de paiement
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 25px; background-color: #FF4B4B; color: white; font-weight: bold; }
    .pay-button {
        background-color: #28a745;
        color: white;
        padding: 15px;
        text-align: center;
        text-decoration: none;
        display: block;
        border-radius: 25px;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🦁 ZooGénérateur Pro")

# Section Génération
animal = st.text_input("Quel animal ?", placeholder="Ex: Un léopard en costume")
if st.button("Essai Gratuit (Serveur Partagé) ✨"):
    if animal:
        with st.spinner("L'IA travaille... (Si ça bloque, recliquez)"):
            API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
            try:
                response = requests.post(API_URL, json={"inputs": animal}, timeout=60)
                if response.status_code == 200:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, use_container_width=True)
                else:
                    st.error("Serveur saturé. Normal en version gratuite.")
            except:
                st.error("Délai dépassé. Recliquez !")
    else:
        st.warning("Écrivez un nom.")

st.markdown("---")

# SECTION VENTE (Pour remplir ta carte Visa)
st.subheader("🚀 Passez à la Version Ultra-Rapide")
st.write("Marre d'attendre ? Recevez vos images en 4K, sans aucune attente et sans bug.")

# Remplace le numéro par le tien
numero_whatsapp = "225XXXXXXXX" # METS TON NUMÉRO ICI
message_vente = f"Bonjour, je souhaite acheter le Pack 10 images HD pour 5€"
url_whatsapp = f"https://wa.me/{numero_whatsapp}?text={message_vente.replace(' ', '%20')}"

st.markdown(f'<a href="{url_whatsapp}" class="pay-button">Commander la version HD (5€) 💳</a>', unsafe_allow_html=True)
