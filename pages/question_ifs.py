import streamlit as st
import requests
from groq import Groq  # Adjust the import statement here

st.title("Queston IFS- Secure Page")
if st.session_state.get("logged_in"):
    st.write("You are logged in!")
else:
    st.warning("Please log in to access this page.")

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
 Food safety and quality management system
2.1 Quality management
2.1.1 Document management
2.1.1.1 A procedure shall be documented, implemented and maintained to control documents and their
amendments. All documents which are necessary for compliance with food safety, product quality,
legality, authenticity and customer requirements shall be available in their latest version. The reason
for any amendments to documents, critical to those requirements, shall be recorded.
2.1.1.2 The food safety and quality management system shall be documented, implemented and maintained
and shall be kept in one secure location. This applies to both physical and/or digital documented
systems.
2.1.1.3* All documents shall be legible, unambiguous and comprehensive. They shall be available to the
relevant personnel at all times.
2.1.2 Records and documented information
2.1.2.1 Records and documented information shall be legible, properly completed and genuine. They shall
be maintained in a way that subsequent revision or amendment is prohibited. If records are documented electronically, a system shall be maintained to ensure that only authorised personnel
have access to create or amend those records (e.g. password protection).
2.1.2.2* All records and documented information shall be kept in accordance with legal and customer
requirements. If no such requirements are defined, records and documented information shall be
kept for a minimum of one year after the shelf life. For products which have no shelf life, the duration
of record and documented information keeping shall be justified and this justification shall be
documented.
2.1.2.3 Records and documented information shall be securely stored and easily accessible.
2.2 Food safety management
2.2.1 HACCP plan
2.2.1.1* The basis of the company’s food safety management system shall be a fully implemented, systematic
and comprehensive HACCP based plan, following the Codex Alimentarius principles, good manufacturing practices, good hygiene practices and any legal requirements of the production and
destination countries which may go beyond such principles. The HACCP plan shall be specific and
implemented at the production site.
2.2.1.2* The HACCP plan shall cover all raw materials, packaging materials, products or product groups, as
well as every process from incoming goods up to the dispatch of finished products, including
product development.
2.2.1.3 The HACCP plan shall be based upon scientific literature or expert advice obtained from other
sources, which may include: trade and industry associations, independent experts and authorities.
This information shall be maintained in line with any new technical process development.
2.2.1.4 In the event of changes to raw materials, packaging materials, processing methods, infrastructure
and/or equipment, the HACCP plan shall be reviewed to ensure that product safety requirements
are complied with.
2.3 HACCP analysis
2.3.1 HACCP team
2.3.1.1 Assemble HACCP team:
The HACCP team shall have the appropriate specific knowledge and expertise and be a multidisciplinary team which includes operational staff.
2.3.1.2 Those responsible for the development and maintenance of the HACCP plan shall have an internal
team leader and shall have received appropriate training in the application of the HACCP principles
and specific knowledge of the products and processes.
2.3.2 Product description
2.3.2.1 A full description of the product shall be documented and maintained and shall contain all relevant
information on product safety, which includes, at a minimum:
• composition
• physical, organoleptic, chemical and microbiological characteristics
• legal requirements for the food safety of the product
• methods of treatment, packaging, durability (shelf life)
• conditions for storage, method of transport and distribution.
2.3.3 Identify intended use and users of the product
2.3.3.1 The intended use of the product shall be described in relation to the expected use of the product
by the end consumer, taking vulnerable groups of consumers into account.
2.3.4 Construct flow diagram
2.3.4.1 A flow diagram shall be documented and maintained for each product, or product group, and for
all variations of the processes and sub-processes (including rework and reprocessing). The flow
diagram shall identify every step and each control measure defined for CCPs and other control
measures. It shall be dated, and in the event of any change, shall be updated.
2.3.5 On-site confirmation of the flow diagram
2.3.5.1 Representatives of the HACCP team shall verify the flow diagram through on-site verifications, at
all operation stages and shifts. Where appropriate, amendments to the diagram shall be made.
2.3.6 Conduct a hazard analysis for each step
2.3.6.1 A hazard analysis shall be conducted for all possible and expected physical, chemical (including
radiological and allergens) and biological hazards. The analysis shall also include hazards linked to
materials in contact with food, packaging materials as well as hazards related to the work environment. The hazard analysis shall consider the likely occurrence of hazards and the severity of their
adverse health effects. Consideration shall be given to the specific control measures that shall be
applied to control each significant hazard.
2.3.7 Determining critical control points and other control measures
2.3.7.1 Determining whether the step at which a control measure is applied is a CCP in the HACCP system
shall be facilitated by using a decision tree or other tool(s), which demonstrates a logical reasoned
approach.
2.3.8 Establish validated critical limits for each CCP
2.3.8.1* For each CCP, critical limits shall be defined and validated to identify when a process is out of
control.
2.3.9 Establish a monitoring system for each CCP
2.3.9.1* KO N° 2: Specific monitoring procedures in terms of method, frequency of measurement or
observation and recording of results, shall be documented, implemented and maintained for
each CCP, to detect any loss of control at that CCP. Each defined CCP shall be under control.
Monitoring and control of each CCP shall be demonstrated by records.
2.3.9.2 Records of CCP monitoring shall be verified by a responsible person within the company and
maintained for a relevant period.
2.3.9.3 The operative personnel in charge of the monitoring of control measures defined for CCPs and
other control measures shall have received specific training/instruction.
2.3.9.4 Control measures, other than those defined for CCPs, shall be monitored, recorded and controlled
by measurable or observable criteria.
2.3.10 Establish corrective actions
2.3.10.1 In the event that the monitoring indicates that a particular control measure defined for a CCP or
any other control measure is not under control, corrective actions shall be documented and implemented. Such corrective actions shall also take any action relating to non-conforming products
into account and identify the root cause for the loss of control of CCPs.
2.3.11 Validate the HACCP plan and establish verification procedures
2.3.11.1 Procedures of validation, including revalidation after any modification that can impact food safety,
shall be documented, implemented and maintained to ensure that the HACCP plan is suitable to
effectively control the identified hazards.
2.3.11.2*Procedures of verification shall be documented, implemented and maintained to confirm that the
HACCP plan is working correctly. Verification activities of the HACCP plan, for example:
• internal audits
• testing
• sampling
• deviations and non-conformities
• complaints
shall be performed at least once within a 12-month period or whenever significant changes occur.
The results of this verification shall be recorded and incorporated into the HACCP plan.
2.3.12 Establish documentation and record keeping
2.3.12.1 Documentation and records related to the HACCP plan, for example:
• hazard analysis
• determination of control measures defined for CCPs and other control measures
• determination of critical limits
• processes
• procedures
• outcome of control measures defined for CCPs and other control measure monitoring
activities
• training records of the personnel in charge of the CCP monitoring
• observed deviations and non-conformities and implemented corrective actions
shall be available.


"""

def get_groq_client():
    """Initialize and return a Groq client with the API key."""
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    urls = [
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFS_Food_v8_standard_FR_1681804144%20(2).txt"
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
    """Generate a response to the user query using Groq and the loaded documents."""
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
