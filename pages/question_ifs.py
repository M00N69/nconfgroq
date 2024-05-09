import streamlit as st
import requests
from groq import Groq  # Import the Groq API client assuming this is a valid import

# Placeholder for the long text (replace with actual content)
long_text_placeholder = """
1 Governance and commitment
1.1 Policy
1.1.1* The senior management shall develop, implement and maintain a corporate policy, which shall
include, at a minimum:
• food safety, product quality, legality and authenticity
• customer focus
• food safety culture
• sustainability.
This corporate policy shall be communicated to all employees and shall be broken down into
specific objectives for the relevant departments.
Objectives about food safety culture shall include, at a minimum, communication about food safety
policies and responsibilities, training, employee feedback on food safety related issues and performance measurement.
1.1.2 All relevant information related to food safety, product quality, legality and authenticity shall be
communicated effectively and in a timely manner to the relevant personnel.
1.2 Corporate structure
1.2.1* KO N° 1: The senior management shall ensure that employees are aware of their responsibilities
related to food safety and product quality and that mechanisms are implemented to monitor
the effectiveness of their operation. Such mechanisms shall be identified and documented.
1.2.2 The senior management shall provide sufficient and appropriate resources to meet the product
and process requirements.
1.2.3* The department responsible for food safety and quality management shall have a direct reporting
relationship to the senior management. An organisational chart, showing the structure of the
company, shall be documented and maintained.
1.2.4 The senior management shall ensure that all processes (documented and undocumented) are
known by the relevant personnel and are applied consistently
1.2.5* The senior management shall maintain a system to ensure that the company is kept informed of
all relevant legislation, scientific and technical developments, industry codes of practice, food
safety and product quality issues, and that they are aware of factors that can influence food defence
and food fraud risks.
1.2.6* The senior management shall ensure that the certification body is informed of any changes that
may affect the company’s ability to conform to the certification requirements. This shall include,
at a minimum:
• any legal entity name change
• any production site location change.
For the following specific situations:
• any product recall
• any product recall and/or withdrawal decided by authorities for food safety and/or food fraud
reasons
• any visit from authorities which results in mandatory action connected to food safety, and/or
food fraud
the certification body shall be informed within three (3) working days.
1.3 Management review
1.3.1* The senior management shall ensure that the food safety and quality management system is
reviewed. This activity shall be planned within a 12-month period and its execution shall not exceed
15 months. Such reviews shall include, at a minimum:
• a review of objectives and policies including elements of food safety culture
• results of audits and site inspections
• positive and negative customer feedback
• process compliance
• food fraud assessment outcome
• food defence assessment outcome
• compliance issues
• status of corrections and corrective actions
• notifications from authorities.
1.3.2 Actions from the management review shall be aimed at supporting improvement. The management
review shall assess follow-up actions from previous management reviews and any change that
could affect the food safety and quality management system. The management review shall be
fully documented.
1.3.3 The senior management shall identify and review (e.g. by internal audits or on-site inspections)
the infrastructure and work environment needed to ensure food safety, product quality, legality
and authenticity, at least once within a 12-month period, or whenever significant changes occur.
This shall include, at a minimum:
• buildings
• supply systems
• machines and equipment
• transport
• staff facilities
• environmental conditions
• hygienic conditions
• workplace design
• external influences (e.g. noise, vibration).
Based on risks, the results of the review shall be considered for investment planning.
"""

def get_groq_client():
    """Initialize and return a Groq client with the API key."""
    return groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    urls = [
        "https://raw.githubusercontent.com/m00n69/nconfgroq/main/ifs_food_v8_audit_checklist_guideline_v1_en_1706090430.txt"
    ]
    documents = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            documents.append(response.text)
        else:
            st.error(f"Failed to load document from: {url}. Status code: {response.status_code}")
    if not documents:
        st.error("No documents loaded successfully.")

    # Add the long text as additional document content
    documents.append(long_text_placeholder)

    return documents

def generate_response(user_input, documents):
    """Generate a response to user query using Groq and loaded documents."""
    client = get_groq_client()

    system_instruction = """
    Utilisez exclusivement les informations du contexte fourni, en particulier les documents chargés, pour générer des réponses. Les réponses doivent être en français, basées uniquement sur les données fournies sans extrapolation. Aucun lien externe ou référence directe à des sources non incluses dans les documents ne doit être utilisé. Vérifiez la précision des clauses mentionnées par rapport au fichier ifsv8.txt en utilisant les autres documents comme références complémentaires.
    """

    messages = [
        {"role": "user", "content": user_input},
        {"role": "system", "content": system_instruction}
    ]
    for doc in documents:
        messages.append({"role": "assistant", "content": doc})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192"
    )

    return chat_completion.choices[0].message.content

def main():
    st.title("Question sur les normes IFS v8")

    documents = load_documents()

    if documents:
        user_input = st.text_area("Posez votre question ici:", height=300)
        if st.button("Envoyer"):
            with st.spinner('Génération de la réponse en cours...'):
                response = generate_response(user_input, documents)
                st.write(response)
    else:
        st.error("Document loading failed, cannot proceed.")

if __name__ == "__main__":
    main()
