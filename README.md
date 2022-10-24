# Projet B3 analyse de données 

<details>
  <summary>--</summary>
  
  But du projet : 
  Le projet a pour but de récupérer et analyser un jeu de données inconnu.  
  Au travers du langage SQL et python, vous devrez nettoyer le jeu de données et effectuer une analyse de données.  
  Une restitution graphique sera faite dans l’outils power bi. 
  
  ## Partie 1 : Jeu de données 

  - Récupérer la VM sous VirtualBox  
  - Découvrir les données et vérifier leur intégrité. 
  - Nettoyer les erreurs et incohérences. 
  - Reconstituer le schéma de base de données. 

  

  ## Partie 2 : Prévision python 

  Créer un projet Python permettant de générer une prévision sur un jeu de données. 
  Le programme doit permettre de rendre paramétrable l’horizon de prévision et la fréquence des données. 
  Le programme doit permettre de générer en sorti une table SQL en sortie contenant : 

  - Les paramètres 
  - La saisonnalité 
  - Les dates 
  - Les valeurs 

  La prévision doit être faite pour chaque produit éligible.  

  ## Partie 4 : Power bi 

  Une fois la base de données nettoyée et les prévisions générées, les données seront importées dans Power Bi afin de générer un rapport. 

  Le rapport devra contenir au moins : 

  - 5 graphiques différents (histogramme, courbe …) 
  - 1 matrice de dimension 3 
  - 1 carte géographique de la répartition des clients 
  - 2 courbes comparant les données réelles avec les prévisions 
  - Colonnes calculées afin d’alimenter les filtres 
  - Mesures calculées de l’évolution par rapport à l’année précédente. 

  Le rendu final sera un livrable client contenant les différentes étapes du projet.  

  Le rapport power bi sera rendu sous format .pbix. 

</details>

## 1.1 Découvrir les données et vérifier leur intégrité. 
### Client
- Store client's data
- Client can have dept
- Two account type ( 1 or 2 `Type_de_compte`)


> `Code_Societe`: is always `1` (it can be the indentifier of the current company)
****
> `Code_Client`: Non-linear

> `Cle_Client`:

> `Nom`: Format(`CLIENT XXXXX`)

> `Secteur_Commercial_Libelle`: Linked to `Secteur_Commercial` 

> `Secteur_Commercial`: Linked to `Secteur_Commercial_Libelle` 

> `Situation_Client`: ENUM (Normal, A surveiller, Fermé, Bloqué sauf création commande, Bloqué sauf comptant, Bloqué)


### Representant
- `Profil_commissionnement` need to be trimmed (`01` -> `1`)

### Fournisseur
- `Nom_Representant` contains sometimes additional information like phone number or label or email. Those data should be in `Telephone` or `Email`
- `Categorie_Fournisseur` is always NULL
- `Localite` contains some value with quotes (ex: `""Los Villares""`)

### Ventes
- Missing names for col `?` and `??` 
- `?` seems to match with `Code_Depot`





# ==========================

## Table Client

### Questions a poser au client

Colonne "Dpt Vente" : Intéret particulier ?
Colonne "?" : A quoi sert cette colonne ?
Colonne "Secteur_commerciale" : Nous n'avons que 3 valeurs '001', '002', '003', prevoyez-vous d'en ajouter ?
Colonne "Objectif_CA_Client" : Toujours valeurs a 0 , pertinent ?
Colonne "Code_tarif_port" : Valeurs non harmonisé, a quoi sert cette colonne ?
Colonne "Code_ABC" : Champs vide, a quoi sert cette colonne 
Colonne "Type_de_compte" : Valeur a 1 et 2, a quoi sert cette colonne ?
Colonne "Commune" : Vide

### A faire

Colonne "Categorie_Client" : Normalisé le stockage des données, LOWERCASE, etc

## Table Depot

### Questions a poser au client-2

Ligne dupliqué execpté le "Code_depot" : Raison particuliére ?

### A faire-2

## Table DepVente

### Questions a poser au client-3

Table vraiment utile ? A quoi sert cette table ?

### A faire-3

-

## Table Fournisseur

### Questions a poser au client-4

Colonne "Mot_clé" : A quoi sert cette colonne ?
Colonne "Non Founisseur" : Est ce que le nom de la collone est toujours FOURNISSEUR+random num?
Colonne "Telephone" : Pour code_fournisseur 000000005528, format telephone non valide.
Colonne "Nom_Representant" : A été fusionné avec téléhone
Colonne "Categorie_Founrisseur" : Vide
Colonne "Reference" : A des lignes vide, a quoi correspond ce champs ?

### A faire-4

Regex exctraction numéro de télephone

## Table Produit

### Questions a poser au client-5

Colonne "Code_dpt_Vente_Article" : Valeur toujours a 1
Colonne "Code_lettrage_produit" : A quoi correspond cette colonne ?
Colonne "Code_ABC" : A quoi correspond cette colonne ?
Colonne "N_U_Vente_Dans_Stock" : A quoi correspond cette colonne ? ( Nombre d'unité de vente dans le stock ???)
Colonne "Code_Activite" : A quoi correspond cette colonne ?




----------------------------------------------------------------------------------------------------------------------------------------------------

# Table Ventes

On a 349908 entres au total.
IdFaitVente est correct et s'incremente correctement.
Code_Societe a une unique valeur "5A1"


### A faire-6









