# disaster_tweets

Pendant une catastrophe, les réseaux sociaux mélangent des messages qui la signalent vraiment et des messages qui emploient les mêmes mots dans un autre sens (par exemple « on fire » pour dire « en forme »). Ce projet utilise le traitement automatique du langage (NLTK) et le machine learning (scikit-learn, XGBoost) pour classer des tweets en deux catégories : parle d'une catastrophe réelle (1) ou non (0).

Les données viennent de la compétition Kaggle [Natural Language Processing with Disaster Tweets](https://www.kaggle.com/competitions/nlp-getting-started).

## Contenu

- `viz_eye_emergency.ipynb` : exploration et visualisation des données (doublons, longueur des tweets, localisation, nuages de mots).
- `ML_eye_emergency.ipynb` : nettoyage du texte, vectorisation TF-IDF, entraînement et comparaison de 5 modèles (SVM, arbre de décision, forêt aléatoire, régression logistique, XGBoost), puis prédictions sur le jeu de test.
- `veille_nlp.ipynb` : notes de veille sur le NLP (sans code).
- `fonctions.py` : fonction de nettoyage du texte utilisée par le notebook ML.
- `stopwords.txt` : liste de mots vides utilisée pour les nuages de mots.

Les sorties (tableaux et graphiques) sont enregistrées dans les notebooks : GitHub les affiche sans rien exécuter.

## Données

Les données de la compétition ne sont pas redistribuées dans ce dépôt (voir le règlement de la compétition). Pour les obtenir :

1. Télécharger `train.csv` et `test.csv` depuis l'onglet « Data » de la compétition (il faut un compte Kaggle et accepter le règlement).
2. Les renommer en `train_tweets.csv` et `test_tweets.csv`.
3. Les placer à la racine du projet, à côté des notebooks.

## Installation et exécution

Testé avec Python 3.12 et 3.14.

```
python -m venv .venv
.venv\Scripts\activate          (Windows)
source .venv/bin/activate       (macOS / Linux)
pip install -r requirements.txt
```

Pour ouvrir les notebooks, utiliser VS Code avec l'extension Jupyter, ou `pip install jupyterlab` puis `jupyter lab`. Ensuite, lancer « Run All ». Au premier lancement, le notebook ML télécharge les ressources NLTK nécessaires.

## Résultats

En validation, la régression logistique et le SVM obtiennent environ 80 à 81 % d'accuracy. Le détail est dans la conclusion du notebook ML.

## Auteurs

Projet réalisé par brusadelli-luca et sadio-amina. Code écrit en 2023 ; revue et corrections de 2026 faites avec Claude.
