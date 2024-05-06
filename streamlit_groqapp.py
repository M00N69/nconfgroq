import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# Load the T5 model and tokenizer, ensuring it uses the appropriate device
device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForSeq2SeqLM.from_pretrained("t5-small").to(device)
tokenizer = AutoTokenizer.from_pretrained("t5-small")

# Define a function to generate text using the model
def generate_text(input_text):
    try:
        inputs = tokenizer.encode_plus(
            input_text,
            max_length=1024,
            padding="max_length",
            truncation=True,
            return_attention_mask=True,
            return_tensors="pt",
        ).to(device)
        outputs = model.generate(inputs["input_ids"], attention_mask=inputs["attention_mask"])
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error in text generation: {str(e)}"

# Define a function for each page
def page_reformulation():
    st.title("Reformulation des Non-Conformités")
    user_input = st.text_area("Posez votre question ici:", height=200)  # Height is in pixels
    if st.button("Envoyer"):
        with st.spinner('Attendez pendant que nous générons la réponse...'):
            response = generate_text(user_input)
            st.write(response)

def another_page():
    st.title("Another Page")
    st.write("Content for another page")

# Set up sidebar navigation
st.sidebar.title('Navigation')
option = st.sidebar.selectbox(
    'Choose a page:',
    ('Reformulation des Non-Conformités', 'Another Page')
)

if option == 'Reformulation des Non-Conformités':
    page_reformulation()
elif option == 'Another Page':
    another_page()

# Optionally, add a button to restart the app
if st.sidebar.button("Restart App"):
    st.experimental_rerun()

# Add instructions as given before
system_instruction = "Se référer en priorité aux documents qui ont été mis à disposition concernant IFSv8. Les bonnes pratiques de la reformulation de l'écart sont: doit être factuelle, doit être détaillée (référence de la procédure, zone /équipement, …), doit justifier le choix de notation, en fonction du type de déviation/non-conformité, le risque produit doit être préciser en restant dans le contexte de l’exigence, ne doit pas être assimilable à du conseil, ne doit pas être rédigée sous forme de suggestions. La reformulation de l'écart doit de préférence inclure les 4 aspects suivants:1/ L’exigence exemple: La norme exige que ….. ou exigence interne 2/ Description de la défaillance : Les responsabilités, la méthode ou les informations documentées n’ont pas été prévues à ce sujet OU Les dispositions prévues ne sont pas mises en œuvre OU Les dispositions prévues ne sont pas toujours mises en œuvre OU Les dispositions prévues et mises en œuvre ne sont pas toujours suffisamment efficaces à atteindre tel résultat prévu 3/ Preuve de la défaillance 4/ Conséquence / Impact de cet écart dans le contexte de l’exigence; toujours conclure en expliquant pour le risque est limité. Réaliser systématiquement les 2 reformulations ( toujours 1 en français et 1 en anglais) ne doivent pas inclure des conseils ou des recommandations dans la description du risque qui ne doit pas exagérer le danger. La reformulation doit être professionnelle sans citer les 4 étapes mais les rédigeant de manière harmonieuse et compréhensible"

st.write(system_instruction)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Reformulation des Non-Conformités",
        page_icon=":pencil:",
        layout="wide",
    )
    st.title("Reformulation des Non-Conformités")
    st.write("Bienvenue dans l'application de reformulation des non-conformités!")
    st.write("Veuillez sélectionner une page dans le menu de navigation à gauche.")

