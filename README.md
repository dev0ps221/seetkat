# SEET-KAT Network Scanner

SEET-KAT est un outil de balayage de réseau simple mais puissant écrit en Python. Il utilise la bibliothèque Scapy pour envoyer des requêtes ARP sur le réseau et collecter les réponses.

## Installation

1. Clonez le dépôt:

\```bash
git clone https://github.com/yourusername/seet-kat.git
cd seet-kat
\```

2. Installez les dépendances:

Pour les versions non-Mac:

\```bash
pip install -r requirements.txt
\```

Pour la version Mac:

\```bash
pip install -r macguirequirements.txt
\```

## Utilisation

### Script en ligne de commande

Exécutez le script `seetkat.py`:

\```bash
python seetkat.py
\```

### Interface graphique (Tkinter)

Exécutez le script `seetkatgui.py`:

\```bash
python seetkatgui.py
\```

### Interface graphique (PyQt5, pour macOS)

Exécutez le script `seetkatguimac.py`:

\```bash
python seetkatguimac.py
\```

Dans les versions avec interface graphique, entrez l'adresse IP cible ou la plage d'adresses IP (par exemple, "192.168.1.1/24") dans le champ de texte et cliquez sur "Start Network Scan". Les résultats seront affichés dans la zone de texte en dessous.

## Licence

Ce projet est sous licence Open Source. 
