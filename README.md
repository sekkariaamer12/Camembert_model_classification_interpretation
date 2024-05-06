# Camembert_model_classification_interpretation

Ce projet s’inscrit dans le cadre du diagnostic des modèles de Deep Learning à l’interprétabilité et la compréhension des capacités de modèles IA.
Les méthodes d’interprétabilité mises en place dans ce projet ont pour cadre applicatif les modèles de classification de texte. 



Pour cela on a mis en place un modèle de classification des tweets selon 4 classes : : "l’énergie nucléaire", "la diminution de l’utilisation de l’avion", "la décroissance" et "la diminution de la consommation de viande". , chacun d’entre eux engendrant un débat sur leur impact environnemental respectif.


L’objectif est d’avoir une estimation des concepts que le modèle réussit à discriminer, et d’identifier des biais liés aux données qui résultent de corrélations
entre les étiquettes de classes et certains mots présentes dans l’ensemble d’apprentissage et non pertinentes du point de vue de l’objectif sémantique de classification. Pour cela, ce projet adapte une technique d’intégration de gradient afin de quantifier l’influence qu’ont les différents mots dans la décision du classifieur, pour cela nous avons utilisé la bibliothèque Captum.

# Modèle de classification des tweets Camemebert :

Le modèle CamemBERT (transformer) est une architecture pré-entraînée similaire à celle de BERT et spécifiquement conçue pour le traitement du langage naturel français. Il a été appris sur le corpus OSCAR par les équipes de l’Institut National de Recherche informatique et Automatique (INRIA) et Meta. Martin et al. (2019)

Afin d'adapter notre modèle sur notre tache de classification (Transfert Learning)  on a ajouté un bloc de classification et puis on a entrainé notre modèle avec les données d'entrainement, l'évaluation avec les données d'évaluation et enfin on a testé notre modèle avec les données test en utilisant la matrice de confusion et les métriques d'évaluation suivantes : Accuracy, Recall et F1-score.

# Interprétation du modèle Camembert par Captum : 
Captum est une bibliothèque Python développée par Facebook AI Research qui facilite l’interprétabilité des modèles d’apprentissage automatique construits
avec PyTorch. Elle fournit des outils et des techniques permettant d’attribuer l’importance ou la contribution des différentes caractéristiques d’entrée à la sortie
d’un modèle en utilisant la méthode du gradient intégré. Dans le contexte de la classification en utilisant CamemBERT, le score d’attribution des jetons représente
une évaluation de l’importance relative de chaque jeton dans la prédiction du modèle. Cela permet de comprendre quels mots ou phrases ont une influence sur
la décision finale de notre modèle et d’expliquer ses prédictions.
