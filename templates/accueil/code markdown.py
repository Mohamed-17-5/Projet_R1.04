# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 08:49:48 2025

@author: admin
"""

import csv
import webbrowser

# Ouvrir le fichier "extrait.txt"
with open("fichier_à_traiter.txt", "r") as fichier:
    ipsr = []
    ipde = []
    longueur = []
    flag = []
    seq = []
    heure = []

    flagcounterP = 0
    flagcounterS = 0
    flagcounter = 0
    framecounter = 0
    requestcounter = 0
    replycounter = 0
    seqcounter = 0
    ackcounter = 0
    wincounter = 0

    for ligne in fichier:
        split = ligne.split(" ")

        if "IP" in ligne:
            framecounter += 1

            if "[P.]" in ligne:
                flag.append("[P.]")
                flagcounterP += 1
            elif "[.]" in ligne:
                flag.append("[.]")
                flagcounter += 1
            elif "[S]" in ligne:
                flag.append("[S]")
                flagcounterS += 1

            if "seq" in ligne:
                seqcounter += 1
                seq.append(split[8])

            if "win" in ligne:
                wincounter += 1

            if "ack" in ligne:
                ackcounter += 1

            ipsr.append(split[2])
            ipde.append(split[4])
            heure.append(split[0])

            if "length" in ligne:
                split = ligne.split(" ")
                longueur.append(split[-2] if "HTTP" in ligne else split[-1])

            if "ICMP" in ligne:
                if "request" in ligne:
                    requestcounter += 1
                elif "reply" in ligne:
                    replycounter += 1

# Ajouter une vérification pour éviter la division par zéro
globalreqrepcounter = replycounter + requestcounter
if globalreqrepcounter != 0:
    req = requestcounter / globalreqrepcounter
    rep = replycounter / globalreqrepcounter
else:
    req = rep = 0

globalflagcounter = flagcounter + flagcounterP + flagcounterS
P = flagcounterP / globalflagcounter
S = flagcounterS / globalflagcounter
A = flagcounter / globalflagcounter

flagcounter = [flagcounter]
flagcounterP = [flagcounterP]
flagcounterS = [flagcounterS]
framecounter = [framecounter]
requestcounter = [requestcounter]
replycounter = [replycounter]
seqcounter = [seqcounter]
ackcounter = [ackcounter]
wincounter = [wincounter]

# Contenu de la page Markdown
markdown_content = f'''
# Traitement des données

## Seydina Mohamed Badji - Projet SAE 15

Sur cette page web, nous vous avons  les informations et données pertinentes trouvées dans le fichier à traiter.

### Nombre total de trames échangées
{framecounter[0]}

### Drapeaux (Flags)
- Nombre de flags [P] (PUSH): {flagcounterP[0]}
- Nombre de flags [S] (SYN): {flagcounterS[0]}
- Nombre de flag [.] (ACK): {flagcounter[0]}

![Histogramme des drapeaux](histogramme_drapeaux.png)

### Nombre de requêtes et réponses
- Request: {requestcounter[0]}
- Reply: {replycounter[0]}

![Histogramme des requêtes et réponses](histogramme_requetes_reponses.png)

### Statistiques entre seq, win et ack
- Nombre de seq: {seqcounter[0]}
- Nombre de win: {wincounter[0]}
- Nombre de ack: {ackcounter[0]}
'''

# Ouvrir un fichier CSV pour les données extraites du fichier texte non traité
with open('donnees.csv', 'w', newline='') as fichiercsv:
    writer = csv.writer(fichiercsv)
    writer.writerow(['Heure', 'IP source', 'IP destination', 'Flag', 'Seq', 'Length'])
    writer.writerows(zip(heure, ipsr, ipde, flag, seq, longueur))

# Ouvrir un fichier CSV pour les statistiques générales
with open('Stats.csv', 'w', newline='') as fichier2:
    writer = csv.writer(fichier2)
    writer.writerow(['Flag[P] (PUSH)', 'Flag[S] (SYN)', 'Flag[.] (ACK)', 'Nombre total de trames',
                     'Nombre de request', 'Nombre de reply', 'Nombre de sequence', 'Nombre de acknowledg', 'Nombre de window'])
    writer.writerows(zip(flagcounterP, flagcounterS, flagcounter, framecounter, requestcounter, replycounter, seqcounter, ackcounter, wincounter))

# Créer un fichier Markdown
with open("data.md", "w") as markdown_file:
    markdown_file.write(markdown_content)
    print("Page Markdown créée avec succès.")