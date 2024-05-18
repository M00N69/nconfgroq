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
