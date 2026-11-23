"""Porte de qualité : comparer le nouveau modèle au champion."""

import json
import sys

SEUIL_ABSOLU = 0.90

with open("metriques.json") as f:
    nouveau = json.load(f)

with open("metriques_champion.json") as f:
    champion = json.load(f)

print(
    f"cv_mean nouveau = {nouveau['cv_mean']:.3f} | "
    f"champion = {champion['cv_mean']:.3f}"
)

if nouveau["cv_mean"] < SEUIL_ABSOLU:
    sys.exit(
        f"REFUS : {nouveau['cv_mean']:.3f} "
        f"< seuil absolu {SEUIL_ABSOLU}"
    )

if nouveau["cv_mean"] < champion["cv_mean"] - 0.005:
    sys.exit("REFUS : moins bon que le champion, il reste en production")

print("ACCEPTÉ : le nouveau modèle peut être déployé")