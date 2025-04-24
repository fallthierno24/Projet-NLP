# Classification de CV par Catégorie

## Description du Projet

**Un système intelligent qui catégorise automatiquement les CV (ex: "Développeur", "Data Scientist", "Marketing") en analysant leur contenu textuel.**

## Installation et exécution en local

### Prérequis
- Python 3.8+
- pip
- virtualenv (optionnel)
  
### Étapes d'installation

1. **Cloner le dépôt**
   ```sh
   https://github.com/fallthierno24/Projet-NLP.git
   cd Projet-NLP
   ```

2. **Créer un environnement virtuel (optionnel mais recommandé)**
   ```sh
   python -m venv cv_classification
   source cv_classification/bin/activate   # Pour Linux/Mac
   cv_classification\Scripts\activate      # Pour Windows
   ```

3. **Installer les dépendances**
   ```sh
   pip install -r docs/requirements.txt
   ```

4. **Lancer l'API flask**
   ```sh
   app.py
   ```

## 📂 Structure du projet 

Le projet est organisé comme suit :

```
projet_nlp/  
│  
├── modele/                 # Dossier des modèles de ML 
│   ├── static/           # Fichiers statique (CSS)  
│   └── templates/          # Pages html
│  
├── venv/                    # Environnement virtuel Python 
│  
├── app.py                   # Application principale Flask (backend)  
├── projet_nlp.ipynb         # Notebook d'analyse/entraînement  
├── tester.py                # Script de test du modèle  
├── exigences.txt           # Dépendances Python  
├── README.md                # Documentation du projet  
└── Documents          # Documents(Présentation PowerPoint)
│-- .gitignore                 # Fichier pour ignorer certains fichiers/dossiers dans Git

```

## Fonctionnalités
- **Prédiction automatique** de la catégorie d'un CV (ex: "Informatique", "Marketing", Data Science, etc.).
- Interface web simple avec formulaire de saisie.
- Affichage immédiat des résultats.

## Technologies utilisées
- **Backend** : Python + Flask
- **Frontend** : HTML/CSS
- **Machine Learning** : MultinomialNB


- **Lien vers l'application :**  https://projet-nlp.onrender.com/

