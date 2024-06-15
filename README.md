# EXPLICATIONS CODE NCONFORMITOR GROQAPP

Importation des bibliothèques

streamlit : bibliothèque pour créer des applications web interactives
bcrypt : bibliothèque pour crypter les mots de passe
Groq : bibliothèque pour interagir avec l'API de Groq

Configuration de la page

st.set_page_config : définit les paramètres de la page, tels que le titre, l'icône, la disposition et les éléments du menu
Initialisation de la session

st.session_state : permet de stocker des informations de session, telles que le statut de connexion
Fonction de connexion

login : fonction pour vérifier les informations de connexion et authentifier l'utilisateur
les mots de passes sont créés dns un colab et bcrypt en plus du secret de streamlit
Page de connexion

login_page : page de connexion avec un formulaire pour saisir le nom d'utilisateur et le mot de passe
Fonction de génération de réponse

generate_response : fonction pour générer une réponse en fonction de l'input de l'utilisateur
Uniquement basé sur les instructions dans le code

Page de reformulation

page_reformulation : page pour reformuler les non-conformités avec un champ de saisie pour l'utilisateur et un bouton pour envoyer la requête
Fonction principale

main_app : fonction principale qui gère la navigation entre les différentes pages
Appel de la fonction principale

La fonction principale est appelée en fonction du statut de connexion de l'utilisateur
Redirection

Si l'utilisateur n'est pas connecté, il est redirigé vers la page de connexion
Si l'utilisateur est connecté, il est redirigé vers la page principale
Restart de l'application

Un bouton est disponible dans la sidebar pour redémarrer l'application
En résumé, ce code permet de créer une application web interactive avec une page de connexion, une page de reformulation de non-conformités et une fonction principale pour gérer la navigation entre les différentes pages.

Question sur les normes IFS v8
Ce document présente un script Python qui utilise Streamlit pour créer une application web interactive. L'application permet aux utilisateurs de poser des questions sur les normes IFS v8 en fournissant un contexte de documents spécifiques. Les utilisateurs doivent d'abord se connecter à l'application en utilisant un nom d'utilisateur et un mot de passe sécurisés. Une fois connectés, ils peuvent saisir leur question dans une zone de texte et recevoir une réponse générée par le modèle de langage Groq.

Fonctionnalités clés
Authentification sécurisée des utilisateurs avec bcrypt
Chargement de documents à partir d'URLs spécifiées
Découpage du texte en chunks avec un nombre maximum de tokens
Génération d'embeddings pour les chunks de texte à l'aide du modèle SentenceTransformer
Recherche de chunks pertinents pour la question de l'utilisateur en utilisant la similarité de cosinus
Génération de réponses à la question de l'utilisateur en utilisant le modèle de langage Groq
Interface utilisateur conviviale avec Streamlit
Comment utiliser
Installez les dépendances requises en exécutant pip install -r requirements.txt.
Configurez les informations d'identification de l'utilisateur et la clé API Groq dans les secrets de Streamlit.
Exécutez le script avec streamlit run app.py.
Accédez à l'application dans votre navigateur à l'adresse http://localhost:8501.
Connectez-vous à l'application en utilisant vos informations d'identification.
Saisissez votre question dans la zone de texte et cliquez sur "Envoyer" pour recevoir une réponse.
Configuration
MODEL_NAME: Nom du modèle d'embedding SentenceTransformer à utiliser.
MAX_CONTEXT_CHUNKS: Nombre maximum de chunks à inclure dans le contexte pour la génération de réponses.
MAX_TOKENS_PER_CHUNK: Nombre maximum de tokens par chunk de texte.
long_text_placeholder: Contenu textuel supplémentaire à ajouter aux documents chargés.
urls: Liste d'URLs à partir desquelles charger les documents.
Fonctions principales
login(username, password): Authentifie l'utilisateur avec bcrypt.
secure_page(): Affiche la page sécurisée pour les utilisateurs connectés.
get_groq_client(): Initialise et renvoie un client Groq avec la clé API.
load_documents(): Charge les documents à partir des URLs fournies.
get_embedding_model(): Charge le modèle d'embedding SentenceTransformer.
chunk_text(text, max_tokens): Découpe le texte en chunks avec un nombre maximum de tokens.
generate_embeddings(texts, model): Génère les embeddings pour une liste de textes.
search_relevant_chunks(question, chunks, embeddings, top_k): Recherche les chunks les plus pertinents pour la question.
generate_response(user_input, documents): Génère une réponse à la requête de l'utilisateur.
main(): Fonction principale de l'application Streamlit.
