import streamlit as st
import requests
import io
from PIL import Image

# 1. Configuration Professionnelle
st.set_page_config(page_title="ZooGénérateur Pro", page_icon="🦁")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3.5em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🦁 ZooGénérateur Pro")
st.subheader("Créez des animaux uniques en haute définition")

# 2. Moteur de génération plus robuste (SDXL)
def generer_image(prompt_text):
    # Ce modèle est plus récent et plus stable
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    
    # Remplacez 'VOTRE_CLE_ICI' par votre jeton Hugging Face si vous en avez un, 
    # sinon le serveur gratuit a des limites plus strictes.
    headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"} 
    
    try:
        response = requests.post(API_URL, json={"inputs": prompt_text}, timeout=80)
        if response.status_code == 200:
            return response.content
        return response.status_code
    except:
        return None

# 3. Interface Utilisateur
animal = st.text_input("Quel animal voulez-vous créer ?", placeholder="Ex: Un lion avec une armure de chevalier")
style = st.selectbox("Style artistique", ["Réalisme National Geographic", "Cinématique 4K", "Dessin animé Pixar", "Style Peinture à l'huile"])

if st.button("Lancer la création ✨"):
    if animal:
        with st.spinner("L'IA génère votre chef-d'œuvre... Patientez environ 20-30 secondes."):
            # On ajoute des mots clés pour booster la qualité
            full_prompt = f"{animal}, {style}, highly detailed, 8k resolution, masterpiece"
            resultat = generer_image(full_prompt)
            
            if isinstance(resultat, bytes):
                image = Image.open(io.BytesIO(resultat))
                st.image(image, caption=f"Voici votre {animal}", use_container_width=True)
                
                # Option de téléchargement
                buf = io.BytesIO()
                image.save(buf, format="PNG")
                st.download_button("Télécharger en HD 📥", buf.getvalue(), "mon_animal.png")
            elif resultat == 503:
                st.warning("Le serveur est en train de chauffer... Réessayez dans 15 secondes, il sera prêt.")
            else:
                st.error("Le serveur est très sollicité. Cliquez à nouveau sur le bouton.")
    else:
        st.warning("Veuillez d'abord écrire le nom d'un animal.")

st.markdown("---")
st.info("💡 **Aide :** Si l'image ne s'affiche pas du premier coup, c'est que l'IA est très demandée. Un deuxième clic règle souvent le problème !")
