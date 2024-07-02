# Projet Django Multilingue

Ce projet utilise Django pour créer un site web multilingue avec les fonctionnalités suivantes : affichage d'une liste d'articles de blog, intégration d'un chatbot basé sur un modèle de langage, et implémentation de la recherche augmentée par intelligence artificielle (RAG).

## Prérequis

Assurez-vous d'avoir installé les éléments suivants sur votre système :

- Python (de préférence version 3.x)
- Django (version 3.x ou supérieure)
- Un navigateur web moderne

## Installation

1. **Clonez le repository :**

   ```
   git clone <URL_du_repository>
   cd nom_du_projet
   ```

2. **Créez et activez un environnement virtuel :**

   Utilisez `venv` ou `virtualenv` pour créer un environnement virtuel Python.

   ```
   python -m venv env
   source env/bin/activate  # Pour Linux/Mac
   env\Scripts\activate     # Pour Windows
   ```

3. **Installez les dépendances :**

   ```
   pip install -r requirements.txt
   ```

4. **Appliquez les migrations Django :**

   ```
   python manage.py migrate
   ```

## Exécution du serveur de développement

Pour démarrer le serveur de développement Django et visualiser votre application :

```
python manage.py runserver
```

Le serveur démarrera sur `http://127.0.0.1:8000/`. Ouvrez ce lien dans votre navigateur pour accéder au site web.

## Utilisation

### Navigation

- **Accueil :** Visitez la page d'accueil à l'adresse `http://127.0.0.1:8000/` pour voir la page principale du site.
- **Blog :** Accédez à la liste des articles de blog à l'adresse `http://127.0.0.1:8000/articles/`.
- **Chatbot :** Cliquez sur le lien "Chatbot" dans la barre de navigation pour utiliser le chatbot intégré.
- **Recherche RAG :** Utilisez le lien "RAG" pour accéder à la fonctionnalité de recherche augmentée.

### Langue

- Utilisez le menu déroulant "Language" pour changer la langue du site.

## Développement

Pour contribuer au projet ou le modifier :

1. Modifiez les fichiers dans le répertoire `nom_du_projet`.
2. Testez vos modifications localement avec `python manage.py runserver`.
3. Soumettez vos modifications via pull requests sur GitHub.

## Déploiement

Pour déployer ce projet sur un serveur en production :

1. Configurez les paramètres de production dans `settings.py`.
2. Utilisez un serveur web comme Nginx ou Apache avec uWSGI ou Gunicorn.
3. Utilisez un service comme Heroku, AWS, ou DigitalOcean pour le déploiement.

---

Assurez-vous d'adapter les noms des répertoires et les URLs aux spécificités de votre projet. Ce README fournit une base solide pour comprendre et exécuter votre projet Django multilingue.
