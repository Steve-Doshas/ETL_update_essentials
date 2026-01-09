![Mon Image](https://github.com/Steve-Doshas/BI/blob/main/Liseret%20Inserm%20T.png)

# Service : 
|-----------|-----------|
|-----------|-----------|
| **Nom** |**ETL_update_essentials**| 
| *Périodicité d’exécution*   | A 3h55 UTC. Tous les jours de la semaine|
| *Description* |Ce service automatise la création et mise à jour d'un fichier csv de référence contenant les informations essentielles et actualisées des unités de recherche classées par priorité.
| *Version* | **1.0** |
| *Code* | update_essentials.py|
| *Log du service* |service_essentials$(date +'%Y-%m-%d').log|

# Sources :

|BD|Tables|
|-----------|-----------|
|Fichier Excel|UR_Essentielles.xlsx|

# Sorties :

## Fichier : essentials

|Nom | **UR_essentials.csv**|
|-----------|-----------|
|Chemin | Défini par la variable d'environnement SAVE_PATH|
|Type de fichiers| csv utf-8-sig|
|Récurrence| Données quotidiennes avec conservation des données trimestrielles (31/03, 30/06, 30/09, 31/12)|

|Données|Description|Comment|
|-----------|-----------|-----------|
|date| Date d'extraction des données| Format datetime, réinitialisée à 00:00:00|
|P1| Liste des acronymes d'unités priorité P1| Unités avec priorité = 'P1'|
|P2| Liste des acronymes d'unités priorité P2| Unités avec priorité = 'P2'|
|P3| Liste des acronymes d'unités priorité P3| Unités avec priorité = 'P3'|
|Standard| Liste des acronymes d'unités sans priorité| Unités avec priorité = NaN|
|Inactif| Liste des acronymes d'unités inactives| Unités avec priorité = 'Inactif'|
