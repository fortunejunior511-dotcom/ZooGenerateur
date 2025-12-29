import streamlit as st
from openai import OpenAI
import requests

# 1. Look Premium
st.set_page_config(page_title="ZooGénérateur Pro - Ultra HD", page_icon="💎")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 25px; height: 3.5em; background-color: #FF4B4B; color: white; font-weight: bold; border: none; }
    .whatsapp-btn { 
        background-color: #25D366; 
        color: white; 
        padding: 15px; 
        text-align: center; 
        border-radius: 25px; 
        display: block; 
        text-decoration: none; 
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🦁 ZooGénérateur Pro")
st.subheader("L'IA qui crée vos animaux en Haute Définition")
st.write("---")

# 2. Configuration (La clé sera activée après ton premier encaissement)
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
        return "maintenance"

# 3. Interface de saisie
animal = st.text_input("Quel animal voulez-vous transformer en œuvre d'art ?", placeholder="Ex: Un guépard avec des lunettes de soleil en or")

if st.button("Lancer la création Ultra HD ✨"):
    if animal:
        if "sk-xxx" in OPENAI_API_KEY:
            st.warning("🚀 **Accès Premium Limité** : Le serveur HD est actuellement réservé aux commandes prioritaires via WhatsApp pour éviter la saturation.")
        else:
            with st.spinner("L'IA génère une image parfaite..."):
                url_image = generer_image_luxe(animal)
                if url_image != "maintenance":
                    st.image(url_image, caption="Qualité Ultra HD générée par DALL-E 3", use_container_width=True)
                else:
                    st.error("Erreur de connexion au serveur de luxe.")
    else:
        st.warning("Veuillez entrer une description.")

st.write("---")

# 4. TON BOUTON DE PAIEMENT (WhatsApp)
st.subheader("💰 Commande Express & Paiement Mobile")
st.write("Recevez vos images 4K par WhatsApp sans aucune attente.")

# Ton numéro est configuré ici
link_wa = "https://wa.me/2250554178128?text=Bonjour%20ZooGénérateur%2C%20je%20souhaite%20commander%20un%20pack%20d'images%20HD"

st.markdown(f'<a href="{link_wa}" class="whatsapp-btn">Commander mes images HD (Paiement Mobile)</a>', unsafe_allow_html=True)
