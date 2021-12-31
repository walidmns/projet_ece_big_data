# projet_ece_big_data

Notre projet a pour objectif de récupérer les prix des sites amazon de différents pays et ainsi trouver le meilleur prix. Pour cela nous avons utiliser un bot amazon.

# Prérequis

Pour utiliser notre application vous devez installer docker et minikube. Dans le dossier source nous pourrons retrouver les fichiers de configurations de notre page web ainsi que notre script python qui permet de récupérer les prix des site amazon de différents pays. Nous pourrons également retrouver dans le dossier k8s les configurations de notre minikube.

# Utilisation de notre application

Récupérer le fichier .zip de mon git. Ensuite allez dans le dossier k8s et exécuter les commandes suivantes :

    - kubectl apply -f service.yaml

    - kubectl apply -f deployment.yaml
        
    - minikube tunnel

# Auteur

 - Marwan LAAMOURI
 - Boran KOYUNCU
 - Arvind SAMY
 - Walid MANSOURI
