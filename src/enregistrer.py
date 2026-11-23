from pathlib import Path

import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Récupérer l'identifiant du meilleur run
run_id = Path("modeles/run_id.txt").read_text().strip()

# Enregistrer le modèle dans le registre MLflow
nom_modele = "classifieur-vins"
modele_uri = f"runs:/{run_id}/modele"

modele_enregistre = mlflow.register_model(
    model_uri=modele_uri,
    name=nom_modele
)

# Attribuer l'alias champion à la version enregistrée
client = MlflowClient()
client.set_registered_model_alias(
    name=nom_modele,
    alias="champion",
    version=modele_enregistre.version
)

print(f"Modèle enregistré : {nom_modele}")
print(f"Version : {modele_enregistre.version}")
print("Alias attribué : champion")