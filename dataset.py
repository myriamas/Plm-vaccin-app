import pandas as pd

# I build here the master requirement table for the Digital Regulatory Twin
data_requirements = [
    {
        "Nom": "Traçabilité complète des données de sécurité en Phase I",
        "Type_element": "Exigence",
        "Phase": "Phase I",
        "Type_exigence": "Sécurité",
        "Description": "Toutes les données d'innocuité doivent être tracées, horodatées et documentées selon GCP.",
        "Statut": "Conforme",
        "Impact_AMM": "Critique",
        "Documents_lies": "Protocole clinique Phase I",
        "Preuves_liees": "CRF, base eCRF, listings de sécurité",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Gestion des données cliniques GCP",
        "Fiche_protocole": "VIH_VAX_P1_PROTOCOL.pdf",
    },
    {
        "Nom": "Sécurité long terme (24 mois)",
        "Type_element": "Exigence",
        "Phase": "Phase I–III",
        "Type_exigence": "Sécurité",
        "Description": "Surveillance sécurité des volontaires pendant au moins 24 mois après vaccination.",
        "Statut": "Conforme",
        "Impact_AMM": "Critique",
        "Documents_lies": "Rapport de sécurité longue durée (24 mois)",
        "Preuves_liees": "Base de PV, rapports périodiques",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Plan de pharmacovigilance VIH",
        "Fiche_protocole": "PV_PLAN_VIH.pdf",
    },
    {
        "Nom": "Stérilité des lots cliniques",
        "Type_element": "Exigence",
        "Phase": "Phase I",
        "Type_exigence": "Qualité",
        "Description": "Tous les lots cliniques doivent être testés et certifiés stériles.",
        "Statut": "Conforme",
        "Impact_AMM": "Modéré",
        "Documents_lies": "Certificat de stérilité du lot clinique",
        "Preuves_liees": "Rapports de stérilité CL-0001",
        "IoT": "Température chambre stérile",
        "Frequence": "En continu",
        "Certificat_etalonnage": "Certificat étalonnage incubateur",
        "Process_qualite": "Contrôle de stérilité GMP",
        "Fiche_protocole": "STERILITY_SOP.pdf",
    },
    {
        "Nom": "Validation analytique des méthodes ELISA/neutralisation VIH",
        "Type_element": "Exigence",
        "Phase": "Préclinique",
        "Type_exigence": "Qualité",
        "Description": "Méthodes analytiques validées (spécificité, sensibilité, répétabilité).",
        "Statut": "Non conforme",
        "Impact_AMM": "Modéré",
        "Documents_lies": "Qualification méthodes analytiques",
        "Preuves_liees": "Capture ELISA, rapports de validation",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "Certificat étalonnage lecteurs ELISA",
        "Process_qualite": "Validation de méthode selon ICH Q2",
        "Fiche_protocole": "ELISA_VALIDATION_REPORT.pdf",
    },
    {
        "Nom": "Stabilité 2–8°C sur 24 mois",
        "Type_element": "Exigence",
        "Phase": "AMM",
        "Type_exigence": "Qualité",
        "Description": "Démontrer la stabilité du vaccin à 2–8°C sur au moins 24 mois.",
        "Statut": "Non conforme",
        "Impact_AMM": "Critique",
        "Documents_lies": "Étude de stabilité 24 mois",
        "Preuves_liees": "Tableau stabilité 24 mois",
        "IoT": "Température frigos QC",
        "Frequence": "Quotidienne",
        "Certificat_etalonnage": "Certificats sondes de température",
        "Process_qualite": "Programme de stabilité ICH",
        "Fiche_protocole": "STABILITY_PROTOCOL_2_8C.pdf",
    },
    {
        "Nom": "Réponse immunitaire humorale (anticorps neutralisants)",
        "Type_element": "Exigence",
        "Phase": "Phase II",
        "Type_exigence": "Efficacité",
        "Description": "Mesure des anticorps neutralisants VIH au-dessus d'un seuil minimal d'immunogénicité.",
        "Statut": "Partiel",
        "Impact_AMM": "Critique",
        "Documents_lies": "Rapport immunogénicité Phase II",
        "Preuves_liees": "Courbes de neutralisation virale",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Plan d'analyse statistique ICH E9",
        "Fiche_protocole": "IMMUNO_P2_ANALYSIS_PLAN.pdf",
    },
    {
        "Nom": "Réponse immunitaire cellulaire CD4+/CD8+",
        "Type_element": "Exigence",
        "Phase": "Phase II",
        "Type_exigence": "Efficacité",
        "Description": "Quantification des lymphocytes CD4+/CD8+ activés (ELISpot/ICS validés).",
        "Statut": "Partiel",
        "Impact_AMM": "Modéré",
        "Documents_lies": "Rapport immunogénicité Phase II",
        "Preuves_liees": "Résultats ELISpot et cytométrie",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Contrôles de qualité de cytométrie",
        "Fiche_protocole": "CELLULAR_IMMUNO_SOP.pdf",
    },
    {
        "Nom": "Documentation complète GxP (préclinique → clinique → production)",
        "Type_element": "Exigence",
        "Phase": "Production",
        "Type_exigence": "Production",
        "Description": "Dossiers qualité, préclinique et production conformes aux standards GxP.",
        "Statut": "Partiel",
        "Impact_AMM": "Important",
        "Documents_lies": "Dossier CMC, rapports GxP",
        "Preuves_liees": "Audit trail, change control, CAPA",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Système qualité pharmaceutique (GMP)",
        "Fiche_protocole": "QMS_MANUAL_VAX_HIV.pdf",
    },
    {
        "Nom": "Conformité Directive 2001/83/CE et Règlement (CE) 726/2004",
        "Type_element": "Règlementation",
        "Phase": "AMM",
        "Type_exigence": "Réglementaire",
        "Description": "Respect du cadre communautaire des médicaments, procédure centralisée EMA et pharmacovigilance.",
        "Statut": "Conforme",
        "Impact_AMM": "Critique",
        "Documents_lies": "Dossier AMM complet (CTD Modules 1–5)",
        "Preuves_liees": "Décision EMA, avis Commission Européenne",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Processus AMM centralisée",
        "Fiche_protocole": "CTD_OVERVIEW_VAX_HIV.pdf",
    },
    {
        "Nom": "Archivage GxP 25 ans (PDF/A + signature + hash SHA-256)",
        "Type_element": "Exigence",
        "Phase": "Tout le cycle de vie",
        "Type_exigence": "PV",
        "Description": "Conserver l'ensemble des documents GxP au minimum 25 ans avec intégrité prouvée (PDF/A, signature qualifiée, SHA-256).",
        "Statut": "Partiel",
        "Impact_AMM": "Important",
        "Documents_lies": "Politique d'archivage VIH",
        "Preuves_liees": "Registre d'archives, métadonnées, checksums",
        "IoT": "",
        "Frequence": "Revue annuelle des archives",
        "Certificat_etalonnage": "",
        "Process_qualite": "Processus d'archivage sécurisé",
        "Fiche_protocole": "ARCHIVING_POLICY_VAX_HIV.pdf",
    },
]

df_master = pd.DataFrame(data_requirements)

# I add here the missing requirements (ADE and multi-variants)
missing_requirements = pd.DataFrame(
    [
        {
            "Nom": "Évaluation du risque d’ADE (Antibody-Dependent Enhancement)",
            "Type_element": "Exigence",
            "Phase": "Préclinique – Phase I",
            "Type_exigence": "Sécurité",
            "Description": (
                "Évaluer via études précliniques et analyses immunologiques le risque d’ADE "
                "(exacerbation de l’infection médiée par les anticorps) avant exposition humaine."
            ),
            "Impact_AMM": "Critique",
            "Statut": "Conforme",
            "Documents_lies": "PROTO_ADE_VIH_PCLIN_v1.pdf",
            "Preuves_liees": "RAPPORT_ADE_VIH_PCLIN_v1.pdf",
            "IoT": "",
            "Frequence": "",
            "Certificat_etalonnage": "",
            "Process_qualite": "Revue de sécurité immunologique préclinique",
            "Fiche_protocole": "VIH_ADE_PCLIN_PROT_v1",
        },
        {
            "Nom": "Évaluation de l’efficacité multi-variants VIH (clades A/B/C/D)",
            "Type_element": "Exigence",
            "Phase": "Préclinique – Phase II",
            "Type_exigence": "Efficacité",
            "Description": (
                "Démontrer la capacité du vaccin à neutraliser plusieurs variants VIH "
                "(clades A, B, C et D) conformément aux recommandations internationales."
            ),
            "Impact_AMM": "Modéré",
            "Statut": "Partiel",
            "Documents_lies": "PROTO_NEUTR_MULTI_CLADES_v1.pdf",
            "Preuves_liees": "RAPPORT_NEUTR_MULTI_CLADES_v1.pdf",
            "IoT": "",
            "Frequence": "",
            "Certificat_etalonnage": "",
            "Process_qualite": "Contrôle d’efficacité multi-variants en laboratoire",
            "Fiche_protocole": "VIH_MULTI_CLADES_PROT_v1",
        },
    ]
)

df_master = pd.concat([df_master, missing_requirements], ignore_index=True)

# I also build small helper tables for RFLP, lifecycle, IVV, archiving and audit trail

data_rflp = [
    {
        "Pilier": "Sécurité",
        "Exigences_clefs": "Evaluer le risque d'ADE, sécurité long terme, tolérance clinique.",
    },
    {
        "Pilier": "Qualité",
        "Exigences_clefs": "Contrôle de stérilité, validation des tests VIH, stabilité 24 mois.",
    },
    {
        "Pilier": "Efficacité",
        "Exigences_clefs": "Immunité humorale et cellulaire complètes, tests multi-variants, corrélats de protection.",
    },
    {
        "Pilier": "Production",
        "Exigences_clefs": "Règles GMP, process robuste, traçabilité complète des lots.",
    },
]

df_rflp = pd.DataFrame(data_rflp)

# Lifecycle for the vaccine project (aligned with the "Cycle de vie" document)
data_lifecycle = [
    {
        "Ordre": 1,
        "Étape": "Recherche fondamentale",
        "Objectif": "Identifier une cible biologique et comprendre le mécanisme immunitaire.",
        "Principales_activités": "Études en laboratoire, caractérisation de l'antigène, choix du type de vaccin.",
        "Livrables": (
            "Hypothèses scientifiques, preuves de concept in vitro, caractérisation de l'antigène, "
            "publications et brevets éventuels."
        ),
        "Normes": "GLP",
    },
    {
        "Ordre": 2,
        "Étape": "Développement préclinique",
        "Objectif": "Tester le vaccin avant toute exposition à l'Homme.",
        "Principales_activités": (
            "Études in vitro sur cellules, études in vivo sur modèles animaux, "
            "évaluation immunogénicité / toxicité / stabilité, préparation du dossier pour passer en clinique."
        ),
        "Livrables": (
            "Rapport préclinique complet, données immunogénicité et toxicité, "
            "stratégie de développement clinique et plan des essais."
        ),
        "Normes": "GLP",
    },
    {
        "Ordre": 3,
        "Étape": "Développement clinique (Phases I–III)",
        "Objectif": "Évaluer la sécurité, déterminer la dose optimale et démontrer l'efficacité chez l'Homme.",
        "Principales_activités": (
            "Phase I : sécurité et tolérance (10–100 volontaires). "
            "Phase II : dose optimale et premières preuves d'efficacité (100–1 000). "
            "Phase III : preuve statistique d'efficacité et profil bénéfice / risque (1 000–50 000)."
        ),
        "Livrables": (
            "Rapports de tolérance, résultats d'efficacité, analyses statistiques, "
            "synthèse bénéfice / risque globale."
        ),
        "Normes": "GCP, Règlement (UE) 536/2014",
    },
    {
        "Ordre": 4,
        "Étape": "Production industrielle",
        "Objectif": "Fabriquer le vaccin à grande échelle sous conditions GMP.",
        "Principales_activités": (
            "Culture cellulaire ou microbienne, purification des antigènes, formulation, "
            "conditionnement et contrôles des lots."
        ),
        "Livrables": (
            "Validation du procédé de fabrication, SOP qualité, contrôles analytiques et microbiologiques, "
            "dossiers de lots et données de stabilité."
        ),
        "Normes": "GMP, Directive (UE) 2017/1572",
    },
    {
        "Ordre": 5,
        "Étape": "Demande d'AMM",
        "Objectif": "Démontrer que le vaccin est efficace, sûr et de qualité contrôlée.",
        "Principales_activités": (
            "Constitution et dépôt du dossier CTD complet, réponses aux questions des autorités, "
            "mise à jour du dossier en fonction des échanges EMA/ANSM."
        ),
        "Livrables": (
            "Dossier AMM (préclinique, clinique, CMC), plan de gestion des risques, "
            "RCP, étiquetage et notices, décision d'AMM."
        ),
        "Normes": "EMA, ANSM, Directive 2001/83/EC",
    },
    {
        "Ordre": 6,
        "Étape": "Commercialisation et distribution",
        "Objectif": "Assurer une distribution et une administration sûres du vaccin.",
        "Principales_activités": (
            "Gestion de la chaîne du froid, logistique vers sites de vaccination, "
            "traçabilité des lots, administration aux patients."
        ),
        "Livrables": (
            "Validation de la chaîne du froid, certificats de conformité, documentation logistique, "
            "protocoles d'administration, enregistrement des doses administrées."
        ),
        "Normes": "GDP, Directive 2001/83/EC",
    },
    {
        "Ordre": 7,
        "Étape": "Pharmacovigilance et suivi post-AMM",
        "Objectif": "Surveiller en continu la sécurité et l'efficacité après la mise sur le marché.",
        "Principales_activités": (
            "Collecte et analyse des effets indésirables, études post-AMM (Phase IV), "
            "mise à jour du profil bénéfice / risque, adaptations éventuelles du vaccin."
        ),
        "Livrables": (
            "Déclarations d'effets indésirables, rapports périodiques, rapports d'études post-AMM, "
            "mises à jour du plan de gestion des risques."
        ),
        "Normes": "ANSM et cadres de pharmacovigilance associés",
    },
]

df_lifecycle = pd.DataFrame(data_lifecycle)
# Lifecycle in 8 steps used in the RFLP-IVV view (Hackathon report)
data_lifecycle_rflp = [
    {
        "Ordre": 1,
        "Étape": "Opportunité",
        "Objectif": "Identifier le besoin médical, le marché et le cadre réglementaire.",
        "Exemples": "Épidémiologie VIH, analyse marché, exigences FDA/EMA initiales.",
    },
    {
        "Ordre": 2,
        "Étape": "Concept",
        "Objectif": "Définir la plateforme vaccinale et les grandes exigences précliniques.",
        "Exemples": "Choix plateforme (ARN, vecteur viral), exigences de sécurité et d’immunogénicité préclinique.",
    },
    {
        "Ordre": 3,
        "Étape": "Design",
        "Objectif": "Concevoir la formulation, la BOM et l’analyse de risques.",
        "Exemples": "Formulation, structure de produit, analyse de risques (FMEA) et exigences de contrôle qualité.",
    },
    {
        "Ordre": 4,
        "Étape": "Ingénierie de fabrication",
        "Objectif": "Préparer le MBOM, le process industriel et la conformité GMP.",
        "Exemples": "MBOM, définition des procédés, qualification équipements, exigences GMP.",
    },
    {
        "Ordre": 5,
        "Étape": "Validation",
        "Objectif": "Valider cliniquement et industriellement le vaccin.",
        "Exemples": "Essais cliniques, validation de procédés, qualification de nettoyage, lots de validation.",
    },
    {
        "Ordre": 6,
        "Étape": "Production",
        "Objectif": "Assurer la fabrication GMP, la libération des lots et la chaîne du froid.",
        "Exemples": "Dossiers de lots, libération QA, suivi chaîne du froid, traçabilité.",
    },
    {
        "Ordre": 7,
        "Étape": "Usage",
        "Objectif": "Gérer la distribution, la pharmacovigilance et la traçabilité terrain.",
        "Exemples": "Distribution, PV, suivi des lots injectés, gestion des incidents qualité.",
    },
    {
        "Ordre": 8,
        "Étape": "Fin de vie",
        "Objectif": "Gérer les déchets, le recyclage et les mises à jour produit.",
        "Exemples": "Élimination déchets, retrait de lots, mise à jour de formulation ou RCP.",
    },
]

df_lifecycle_rflp = pd.DataFrame(data_lifecycle_rflp)
# Matrix linking the 4 pillars (Sécurité, Qualité, Efficacité, Production)
# with the 8 lifecycle steps from the Hackathon report
data_rflp_lifecycle = [
    {
        "Pilier": "Sécurité",
        "Opportunité": "Identifier contraintes de sécurité VIH et attentes autorités.",
        "Concept": "Définir exigences de sécurité préclinique et clinique.",
        "Design": "Intégrer sécurité dans l’analyse de risques produit.",
        "Ingénierie de fabrication": "Prendre en compte sécurité opérateurs / biosécurité.",
        "Validation": "Monitorer effets indésirables, profil bénéfice/risque.",
        "Production": "Assurer qualité des lots et gestion des déviations impactant la sécurité.",
        "Usage": "Pharmacovigilance, signal detection, CAPA sécurité.",
        "Fin de vie": "Gestion de retrait de lots, adaptation du produit.",
    },
    {
        "Pilier": "Qualité",
        "Opportunité": "Identifier référentiels qualité applicables (ICH, GMP).",
        "Concept": "Définir exigences de qualité pour la plateforme vaccinale.",
        "Design": "Concevoir CQ, spécifications, plan de stabilité.",
        "Ingénierie de fabrication": "Définir process, contrôles en cours de fabrication.",
        "Validation": "Valider méthodes analytiques et procédés.",
        "Production": "Contrôles de routine, libération QA, chaîne du froid.",
        "Usage": "Suivi stabilité sur le terrain, gestion OOS/OOT.",
        "Fin de vie": "Archivage qualité, retour d’expérience, mise à jour des specs.",
    },
    {
        "Pilier": "Efficacité",
        "Opportunité": "Définir besoin en efficacité (variants, charge virale, immunité).",
        "Concept": "Spécifier corrélats de protection et endpoints d’efficacité.",
        "Design": "Intégrer efficacité dans design d’essais cliniques.",
        "Ingénierie de fabrication": "Assurer que le process préserve l’antigénicité.",
        "Validation": "Démontrer efficacité clinique (Phases II/III).",
        "Production": "Maintenir consistance de l’efficacité entre lots.",
        "Usage": "Suivi efficacité en vie réelle, études post-AMM.",
        "Fin de vie": "Décision d’adapter ou retirer le produit selon efficacité.",
    },
    {
        "Pilier": "Production",
        "Opportunité": "Évaluer capacité industrielle, sites, partenaires.",
        "Concept": "Choisir technologies de production et supply chain.",
        "Design": "Concevoir BOM, MBOM, lignes pilotes.",
        "Ingénierie de fabrication": "Industrialiser le process, qualification d’équipements.",
        "Validation": "Valider capacité et robustesse industrielle.",
        "Production": "Fabrication GMP, libération, supply chain.",
        "Usage": "Approvisionnement continu, gestion pénuries.",
        "Fin de vie": "Arrêt de production, transition vers nouveau produit.",
    },
]

df_rflp_lifecycle = pd.DataFrame(data_rflp_lifecycle)

data_archiving = [
    {
        "Aspect": "Durée",
        "Détail": "Conservation minimale 25 ans, jusqu'à 30 ans pour documents critiques.",
    },
    {
        "Aspect": "Formats",
        "Détail": "PDF/A et XML comme formats pérennes pour les documents réglementaires.",
    },
    {
        "Aspect": "Sécurisation",
        "Détail": "Signature numérique qualifiée, hashing SHA-256, stockage WORM.",
    },
    {
        "Aspect": "Traçabilité",
        "Détail": "Métadonnées complètes, ID document, version, statut, checksum.",
    },
]

df_archiving = pd.DataFrame(data_archiving)

data_audit_trail = [
    {
        "Qui": "Clinical QA",
        "Quoi": "Change control sur protocole Phase II",
        "Quand": "2025-10-12 09:32",
        "Pourquoi": "Mise à jour guidance EMA VIH 2025",
        "Livrables_impactes": "Protocole Phase II, plan d'analyse, formulaire consentement",
    },
    {
        "Qui": "Regulatory Affairs",
        "Quoi": "Mise à jour section Module 1 CTD",
        "Quand": "2025-11-03 14:08",
        "Pourquoi": "Ajout nouvelle Référence Directive 2001/83/CE consolidée",
        "Livrables_impactes": "Dossier AMM, annexes locales France",
    },
    {
        "Qui": "QA Release",
        "Quoi": "CAPA sur déviation stabilité 2–8°C",
        "Quand": "2025-11-20 16:45",
        "Pourquoi": "Excursion de température détectée sur frigo clinique",
        "Livrables_impactes": "Rapport de stabilité, enregistrements IoT, plan d'action CAPA",
    },
]

df_audit_trail = pd.DataFrame(data_audit_trail)
