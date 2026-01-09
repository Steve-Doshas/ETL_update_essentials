import os, re, io, sys
sys.path.append(os.path.abspath('..\\Dependencies\\'))
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Charger le fichier .env pour récupérer les variables d'environnement
load_dotenv()

###################################################################### GESTION DES PARAMETRES

# Récupérer le chemin de sauvegarde depuis les variables d'environnement
SAVE_PATH = os.getenv('SAVE_PATH')
FETCH_PATH = os.getenv('FETCH_PATH')

import os
import re
from pathlib import Path

source_file = "UR_Essentielles.xlsx"
filename = "UR_essentials.csv"  # Nom du fichier à utiliser pour la sauvegarde
# Charger le fichier CSV existant s'il existe, sinon mettre à None
file_path = Path(SAVE_PATH + filename)
source_file = Path(FETCH_PATH + source_file )


######################################################### VALIDATION DES CONNEXION AUX BASES
# Affichage de la date de lancement du service
NOW = datetime.now()
selected_sheet = str(NOW.year)

print('________________________________________________________________')
print(f'service lancé le {NOW}')

df_c = pd.read_excel(source_file)

def get_list(df, label):
    return df[df['Priorité']== label].acronyme.tolist()

def get_data(df, date:datetime):
    return {'date':date,
            'P1': get_list(df, 'P1'),
            'P2': get_list(df, 'P2'),
            'P3': get_list(df, 'P3'),
            'Standard': df[df['Priorité'].isna()].acronyme.tolist(),
            'Inactif': get_list(df,'Inactif')}

try:
    nowdate = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    row_df = pd.DataFrame([get_data(df_c, nowdate)])

    if file_path.exists():
        df = pd.read_csv(file_path, encoding='utf-8')
        df["date"] = pd.to_datetime(df["date"], errors='coerce')
        df_summary = df[df["date"].dt.strftime('%m-%d').isin(["12-31", "03-31", "06-30", "09-30"])]
        df_summary = pd.concat([row_df, df_summary]).reset_index(drop=True)
        df_summary.to_csv(file_path, index=False, encoding='utf-8')
    else:
        row_df.to_csv(file_path, encoding='utf-8')

    print(f"{filename} a été créé avec succès. Taille:  {os.path.getsize(file_path)/(1024 * 1024):.2f} Mo")

except Exception as e:
    print(f"Erreur lors de la mise à jour de   {file_path}: {e}")

