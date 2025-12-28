import streamlit as st
import requests
import io
import time
from PIL import Image

# 1. Look Professionnel (Bouton rouge et police)
st.set_page_config(page_title="AnimAI Pro", page_icon="🐾")

st.markdown("""
    <style>
    /* Change la couleur du bouton en rouge */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3.5em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
    }
    /* Change la couleur au survol de la souris */
    .stButton>button:hover {
        background-color: #ff3333;
        color: white;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🦁 ZooGénérateur Pro")

# 2. Fonction de génération
def generer_image(prompt_text):
    # Modèle plus rapide pour éviter le message "Serveur occupé"
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    try:
        response = requests.post(API_URL, json={"inputs": prompt_text}, timeout=60)
        if response.status_code == 200:
            if len(response.content) > 1000:
                return response.content
            else:
                return "corrupt"
        elif response.status_code == 503:
            return "loading"
        else:
            return None
    except:
        return None

# 3. Interface
animal = st.text_input("Quel animal ?", placeholder="Ex: Un lion avec une couronne")
style = st.selectbox("Style artistique", ["Photographie", "Dessin animé", "Cyberpunk", "3D Render"])

# Le bouton qui redeviendra rouge grâce au CSS en haut
if st.button("Lancer la création ✨"):
    if animal:
        with st.spinner("L'IA travaille... Patientez quelques secondes."):
            resultat = generer_image(f"{animal}, {style}, high quality, cinematic")
            
            if resultat == "loading":
                st.warning("Le serveur gratuit se réveille... Recliquez dans 10 secondes.")
            elif resultat == "corrupt":
                st.error("Image incomplète. Recliquez sur le bouton.")
            elif isinstance(resultat, bytes):
                image = Image.open(io.BytesIO(resultat))
                st.image(image, use_container_width=True)
                
                buf = io.BytesIO()
                image.save(buf, format="PNG")
                st.download_button("Télécharger l'image 📥", buf.getvalue(), "animal.png")
            else:
                st.error("Serveur saturé. Attendez un peu et réessayez.")
    else:
        st.warning("Écrivez un nom d'animal.")
        st.info("💡 Version Gratuite. Pour obtenir des images 4K sans attente, contactez le support.")
