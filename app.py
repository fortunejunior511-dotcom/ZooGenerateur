import streamlit as st
from openai import OpenAI
import requests

# 1. Look Premium
st.set_page_config(page_title="ZooGénérateur Pro - Ultra HD", page_icon="💎")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 25px; height: 3.5em; background-color: #FF4B4B; color: white; font-weight: bold; }
    .whatsapp-btn { background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 25px; display: block; text-decoration: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦁 ZooGénérateur Pro")
st.write("---")

# 2. Configuration de la Clé (C'est ici qu'on mettra l'argent)
# Pour l'instant, on laisse vide. Quand tu auras 5$, on mettra ta clé ici.
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 

def generer_image_luxe(prompt_text):
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt_text,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        return str(e)

# 3. Interface de vente
st.subheader("🎨 Création d'image Ultra-Réaliste")
animal = st.text_input("Décrivez l'animal de vos rêves :", placeholder="Un lion en armure dorée, style 3D Disney")

if st.button("Lancer la création (Version Premium) ✨"):
    if "sk-xxx" in OPENAI_API_KEY:
        st.error("🚨 Maintenance en cours sur le serveur HD. Veuillez utiliser l'option WhatsApp ci-dessous pour commander.")
    else:
        with st.spinner("L'IA génère une image parfaite..."):
            url_image = generer_image_luxe(animal)
            if "http" in url_image:
                st.image(url_image, caption="Votre chef-d'œuvre est prêt !")
            else:
                st.error("Erreur de solde. Contactez le support.")

st.write("---")

# 4. Le bouton qui va remplir ta carte VISA
st.subheader("💰 Commande Express")
st.write("Recevez 5 images 4K de vos animaux préférés pour seulement 3 000 FCFA.")

numero = "TON_NUMERO_ICI" # METS TON NUMÉRO ICI (Ex: 22507...)
text_wa = f"Bonjour, je viens du site ZooGénérateur. Je veux commander un pack d'images HD."
link = f"https://wa.me/{numero}?text={text_wa.replace(' ', '%20')}"

st.markdown(f'<a href="{link}" class="whatsapp-btn">Commander par WhatsApp (Paiement Mobile)</a>', unsafe_allow_html=True)
