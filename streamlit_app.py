import streamlit as st
from dataset import (
    df_master,
    df_rflp,
    df_lifecycle,
    df_lifecycle_rflp,
    df_rflp_lifecycle,
    df_archiving,
    df_audit_trail,
)

import pandas as pd

# ----- App config -----
st.set_page_config(
    page_title="VAX-PLM – Jumeau réglementaire VIH",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----- Pages list -----
PAGES = [
    "Accueil",
    "Vue d'ensemble",
    "Exigence détaillée",
    "Tableau des exigences",
    "Documents",
    "Preuves",
    "Qualité",
    "IoT / Température",
    "Cycle de vie",
    "RFLP / Architecture",
    "RFLP-IVV – Synthèse",
    "Fonctionnel / Architecture",
    "Méthodologie IVV",
    "Archivage sécurisé",
    "Change control / Audit trail",
    "Soumission réglementaire",
]


# ----- Session state init -----
if "page" not in st.session_state:
    st.session_state["page"] = "Accueil"

if "selected_requirement" not in st.session_state:
    st.session_state["selected_requirement"] = None


# ----- Helpers -----
def color_statut(val: str) -> str:
    if val == "Conforme":
        return "background-color: #C8F7C5"
    if val == "Partiel":
        return "background-color: #F9E79F"
    if val == "Non conforme":
        return "background-color: #F5B7B1"
    return ""


def go_to(target: str) -> None:
    st.session_state["page"] = target
    st.rerun()


# ----- Sidebar : contexte uniquement, plus de menu radio -----
st.sidebar.title("VAX-PLM – Jumeau réglementaire")
st.sidebar.write("Projet vaccin VIH – VAX-HIV-2030")
st.sidebar.markdown(
    "Jumeau réglementaire du vaccin fictif VAX-HIV-2030 : exigences, "
    "documents, preuves, qualité, IoT, archivage et soumission EMA/ANSM."
)

# ----- Barre de navigation horizontale -----

# CSS pour transformer le radio en onglets propres
st.markdown(
    """
    <style>
    div[data-baseweb="radios"] {
        display: flex;
        gap: 0.5rem;
        margin: 0.5rem 0 1.5rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #e0e0e0;
        flex-wrap: wrap;
    }
    div[data-baseweb="radio"] input {
        display: none;
    }
    div[data-baseweb="radio"] > label {
        border-radius: 999px;
        padding: 0.3rem 0.9rem;
        border: 1px solid #d0d0d0;
        background-color: #f7f7f7;
        font-size: 0.9rem;
        cursor: pointer;
        white-space: nowrap;
    }
    div[data-baseweb="radio"] > label:hover {
        border-color: #0f62fe;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

nav_choice = st.radio(
    "Navigation principale",
    PAGES,
    index=PAGES.index(st.session_state["page"]),
    horizontal=True,
    label_visibility="collapsed",
)

if nav_choice != st.session_state["page"]:
    st.session_state["page"] = nav_choice

page = st.session_state["page"]


# ===========================
# ACCUEIL
# ===========================
if page == "Accueil":
    st.title("VAX-PLM – Jumeau Réglementaire du vaccin VIH")

    st.markdown(
        """
        Cette application rassemble l'ensemble du travail sur le vaccin fictif **VAX-HIV-2030** :
        exigences, documents, preuves, qualité, IoT, archivage, cycle de vie et soumission EMA/ANSM.
        """
    )

    st.markdown("### Points d'entrée principaux")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Vue globale")
        st.write("Etat de conformité des exigences et filtres par phase / type d'exigence.")
        if st.button("Ouvrir la vue d'ensemble", use_container_width=True):
            go_to("Vue d'ensemble")

        st.subheader("Lien Exigence → PLM")
        st.write("Fiche détaillée qui relie une exigence à ses documents, preuves, IoT, certificats.")
        if st.button("Ouvrir l'exigence détaillée", use_container_width=True):
            go_to("Exigence détaillée")

    with col2:
        st.subheader("Qualité")
        st.write("Stérilité, stabilité 2–8°C, validation analytique des tests VIH.")
        if st.button("Ouvrir la vue Qualité", use_container_width=True):
            go_to("Qualité")

        st.subheader("IoT / Température")
        st.write("Exemple de relevés température pour frigos et zones contrôlées.")
        if st.button("Ouvrir la vue IoT / Température", use_container_width=True):
            go_to("IoT / Température")

    with col3:
        st.subheader("Cycle de vie et RFLP")
        st.write("Vue du cycle de vie complet et synthèse Sécurité / Qualité / Efficacité / Production.")
        if st.button("Ouvrir le cycle de vie", use_container_width=True):
            go_to("Cycle de vie")
        if st.button("Ouvrir la vue RFLP / Architecture", use_container_width=True):
            go_to("RFLP / Architecture")

        st.subheader("Archivage et audit")
        st.write("Politique d'archivage 25 ans et exemple de change control / audit trail.")
        if st.button("Ouvrir l'archivage sécurisé", use_container_width=True):
            go_to("Archivage sécurisé")


# ===========================
# VUE D'ENSEMBLE
# ===========================
elif page == "Vue d'ensemble":
    st.title("Vue d'ensemble des exigences réglementaires")

    col_filters, col_table = st.columns([1, 3])

    with col_filters:
        phase = st.multiselect("Phase clinique / projet", df_master["Phase"].unique())
        type_req = st.multiselect("Type d'exigence", df_master["Type_exigence"].unique())
        statut = st.multiselect("Statut de conformité", df_master["Statut"].unique())

        df = df_master.copy()

        if phase:
            df = df[df["Phase"].isin(phase)]
        if type_req:
            df = df[df["Type_exigence"].isin(type_req)]
        if statut:
            df = df[df["Statut"].isin(statut)]

        st.markdown("**Nombre d'exigences affichées :** " + str(len(df)))

    with col_table:
        df_view = df[["Nom", "Phase", "Type_exigence", "Impact_AMM", "Statut"]].reset_index(drop=True)
        styled = df_view.style.applymap(color_statut, subset=["Statut"])
        st.dataframe(styled, use_container_width=True, hide_index=True)

    st.markdown("### Explorer une exigence en détail")
    if len(df) > 0:
        nom_sel = st.selectbox(
            "Je sélectionne une exigence à détailler :", df_view["Nom"].tolist()
        )
        if st.button("Ouvrir la fiche détaillée depuis la vue d'ensemble"):
            st.session_state["selected_requirement"] = nom_sel
            go_to("Exigence détaillée")


# ===========================
# EXIGENCE DETAILLEE
# ===========================
elif page == "Exigence détaillée":
    st.title("Exigence détaillée – Exigence → Documents → Preuves")

    options = df_master["Nom"].tolist()
    if st.session_state["selected_requirement"] in options:
        default_index = options.index(st.session_state["selected_requirement"])
    else:
        default_index = 0

    choix = st.selectbox(
        "Je sélectionne une exigence :", options, index=default_index
    )
    st.session_state["selected_requirement"] = choix

    ligne = df_master[df_master["Nom"] == choix].iloc[0]

    col_meta, col_docs = st.columns(2)

    with col_meta:
        st.subheader("Résumé de l'exigence")
        st.write(f"**Nom :** {ligne['Nom']}")
        st.write(f"**Phase :** {ligne['Phase']}")
        st.write(f"**Type d'exigence :** {ligne['Type_exigence']}")
        st.write(f"**Impact sur l'AMM :** {ligne['Impact_AMM']}")
        st.write(f"**Statut :** {ligne['Statut']}")
        st.write("**Description :**")
        st.write(ligne["Description"])

    with col_docs:
        st.subheader("Liens PLM associés")
        st.write(f"**Document(s) lié(s) :** {ligne['Documents_lies']}")
        st.write(f"**Preuve(s) liée(s) :** {ligne['Preuves_liees']}")
        if ligne["IoT"]:
            st.write(f"**IoT / mesure associée :** {ligne['IoT']} ({ligne['Frequence']})")
        if ligne["Certificat_etalonnage"]:
            st.write(f"**Certificat d'étalonnage :** {ligne['Certificat_etalonnage']}")
        st.write(f"**Processus qualité :** {ligne['Process_qualite']}")
        st.write(f"**Référence de fiche / protocole :** {ligne['Fiche_protocole']}")


# ===========================
# TABLEAU DES EXIGENCES
# ===========================
elif page == "Tableau des exigences":
    st.title("Tableau complet des exigences")

    df_view = df_master[
        [
            "Nom",
            "Type_element",
            "Phase",
            "Type_exigence",
            "Description",
            "Impact_AMM",
            "Statut",
        ]
    ].reset_index(drop=True)

    st.dataframe(df_view, use_container_width=True, hide_index=True)

    nom_sel = st.selectbox(
        "Voir la fiche détaillée d'une exigence :", df_view["Nom"].tolist()
    )
    if st.button("Ouvrir la fiche détaillée depuis le tableau des exigences"):
        st.session_state["selected_requirement"] = nom_sel
        go_to("Exigence détaillée")


# ===========================
# DOCUMENTS
# ===========================
elif page == "Documents":
    st.title("Documents liés aux exigences")

    docs = df_master[
        ["Nom", "Documents_lies", "Fiche_protocole", "Phase", "Type_exigence", "Statut"]
    ].reset_index(drop=True)

    st.dataframe(docs, use_container_width=True, hide_index=True)

    nom_sel = st.selectbox(
        "Voir la fiche détaillée à partir d'un document :", docs["Nom"].tolist()
    )
    if st.button("Ouvrir la fiche détaillée depuis Documents"):
        st.session_state["selected_requirement"] = nom_sel
        go_to("Exigence détaillée")


# ===========================
# PREUVES
# ===========================
elif page == "Preuves":
    st.title("Preuves associées aux exigences")

    evid = df_master[
        ["Nom", "Preuves_liees", "Impact_AMM", "Type_exigence", "Phase", "Statut"]
    ].reset_index(drop=True)

    st.dataframe(evid, use_container_width=True, hide_index=True)

    nom_sel = st.selectbox(
        "Voir la fiche détaillée à partir d'une preuve :", evid["Nom"].tolist()
    )
    if st.button("Ouvrir la fiche détaillée depuis Preuves"):
        st.session_state["selected_requirement"] = nom_sel
        go_to("Exigence détaillée")


# ===========================
# QUALITE
# ===========================
elif page == "Qualité":
    st.title("Vue Qualité (stérilité, stabilité, méthodes analytiques)")

    quality = df_master[df_master["Type_exigence"] == "Qualité"].copy()

    df_summary = quality[["Nom", "Phase", "Statut", "Process_qualite"]].reset_index(drop=True)
    st.subheader("Synthèse Qualité")
    st.dataframe(df_summary, use_container_width=True, hide_index=True)

    with st.expander("Afficher le détail complet Qualité (toutes les colonnes)"):
        df_full = quality[
            [
                "Nom",
                "Description",
                "Phase",
                "Statut",
                "Impact_AMM",
                "Process_qualite",
                "Certificat_etalonnage",
            ]
        ].reset_index(drop=True)
        st.dataframe(df_full, use_container_width=True, hide_index=True)

    nom_sel = st.selectbox(
        "Voir la fiche détaillée d'une exigence qualité :", df_summary["Nom"].tolist()
    )
    if st.button("Ouvrir la fiche détaillée depuis Qualité"):
        st.session_state["selected_requirement"] = nom_sel
        go_to("Exigence détaillée")


# ===========================
# IOT / TEMPERATURE
# ===========================
elif page == "IoT / Température":
    st.title("IoT / Température – chaîne du froid et salles contrôlées")

    data_iot = {
        "Capteur": ["Frigo clinique 01", "Frigo QC 02", "Salle de stockage"],
        "Localisation": ["Site clinique A", "Laboratoire QC", "Entrepôt GMP"],
        "Température": ["7.2°C", "6.8°C", "20.5°C"],
        "Fréquence mesure": ["Toutes les 10 min", "Toutes les 10 min", "Toutes les 60 min"],
        "Statut alerte": ["OK", "OK", "Hors spécification"],
    }

    df_iot = pd.DataFrame(data_iot).reset_index(drop=True)
    st.dataframe(df_iot, use_container_width=True, hide_index=True)


# ===========================
# CYCLE DE VIE
# ===========================
elif page == "Cycle de vie":
    st.title("Cycle de vie du vaccin – VAX-HIV-2030")

    st.markdown(
        "Le cycle de vie est structuré en sept étapes, de la recherche fondamentale "
        "jusqu'à la pharmacovigilance post-AMM."
    )

    df_steps = df_lifecycle.sort_values("Ordre")
    cols = st.columns([1, 1, 1, 1, 1, 1, 1])

    for col, (_, row) in zip(cols, df_steps.iterrows()):
        with col:
            st.markdown(
                f"""
                <div style="
                    min-height: 180px;
                    display: flex;
                    flex-direction: column;
                ">
                    <strong>{row['Ordre']}. {row['Étape']}</strong>
                    <div style="margin-top: 6px; font-size: 14px;">
                        {row['Objectif']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")

    for _, row in df_steps.iterrows():
        with st.expander(f"{row['Ordre']}. {row['Étape']}"):
            st.write(f"**Objectif :** {row['Objectif']}")
            st.write("**Principales activités :**")
            st.write(row["Principales_activités"])
            st.write("**Livrables clés :**")
            st.write(row["Livrables"])
            st.write(f"**Normes / référentiels :** {row['Normes']}")


# ===========================
# RFLP / ARCHITECTURE
# ===========================
elif page == "RFLP / Architecture":
    st.title("RFLP – Sécurité / Qualité / Efficacité / Production")

    st.markdown(
        """
        Cette vue est organisée autour des exigences,
        puis une architecture logique du vaccin VIH.
        """
    )

    # --- Un peu de CSS pour les cartes colorées façon maquette ---
    st.markdown(
        """
        <style>
        .rflp-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            grid-gap: 1.2rem;
            margin-top: 1.5rem;
            margin-bottom: 1.5rem;
        }
        .rflp-card {
            padding: 1.2rem 1.4rem;
            border-radius: 16px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
            font-size: 0.95rem;
        }
        .rflp-sec { background-color: #ffe5e5; }   /* Sécurité */
        .rflp-qual { background-color: #fff0c2; }  /* Qualité */
        .rflp-effi { background-color: #e4f9e8; }  /* Efficacité */
        .rflp-prod { background-color: #e3f0ff; }  /* Production */

        .rflp-center {
            display: flex;
            justify-content: center;
            margin-bottom: 0.8rem;
        }
        .rflp-center-badge {
            padding: 0.4rem 1.2rem;
            border-radius: 999px;
            border: 1px solid #d0d0d0;
            background-color: #ffffff;
            font-weight: 600;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- Bandeau central "Exigences" ---
    st.markdown(
        """
        <div class="rflp-center">
            <div class="rflp-center-badge">Exigences</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- 4 cartes RFLP inspirées du PDF ---
    st.markdown('<div class="rflp-grid">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="rflp-card rflp-sec">
            <strong>Sécurité</strong>
            <ul>
                <li>Évaluer le risque d’ADE</li>
                <li>Sécurité à long terme</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="rflp-card rflp-qual">
            <strong>Qualité</strong>
            <ul>
                <li>Contrôle de stérilité</li>
                <li>Validation des tests</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="rflp-card rflp-effi">
            <strong>Efficacité</strong>
            <ul>
                <li>Immunité complète</li>
                <li>Test sur plusieurs variants</li>
                <li>Corrélats de protection</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="rflp-card rflp-prod">
            <strong>Production</strong>
            <ul>
                <li>Règles GMP</li>
                <li>Processus solide</li>
                <li>Traçabilité complète</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Architecture logique du vaccin")

    # --- Schéma logique façon bloc-diagramme ---
    graph_code = """
    digraph G {
        rankdir=LR;
        nodesep=0.6;
        ranksep=0.8;
        size="14,3!";
        ratio=fill;

        node [
            shape=box,
            style="rounded,filled",
            fillcolor="#f5f5f5",
            fontsize=14,
            width=3,
            height=1
        ];

        Besoins   [label="Besoins médicaux\nRéférentiels FDA/EMA"];
        RD        [label="R&D\nPréclinique / Design"];
        Clinique  [label="Clinique\nEssais I–III"];
        Qualite   [label="Qualité / Production\nCMC, GMP, Libération"];
        Reg       [label="Réglementaire\nCTD, AMM"];
        PostAMM   [label="Post-AMM\nPV, archivage, change control"];

        Besoins -> RD -> Clinique -> Qualite -> Reg -> PostAMM;
    }
    """
    st.graphviz_chart(graph_code)


    st.markdown(
        """
        Cette vue montre comment les blocs fonctionnels (antigène, vecteur, adjuvant, injection)
        mènent à une **réponse immunitaire contrôlée** avec un **contrôle qualité** en bout de chaîne.
        """
    )

# ===========================
# RFLP-IVV – SYNTHESE
# ===========================
elif page == "RFLP-IVV – Synthèse":
    st.title("RFLP-IVV – Synthèse du jumeau réglementaire")

    st.markdown(
        """
        Cette vue reprend la logique du rapport de hackathon :  
        **RFLP** pour structurer *Sécurité, Qualité, Efficacité, Production* et  
        **IVV** pour montrer comment ces exigences vivent sur tout le cycle de vie.
        """
    )

    col_left, col_right = st.columns([1, 2])

    with col_left:
        st.subheader("Piliers RFLP")
        st.dataframe(
            df_rflp.reset_index(drop=True),
            use_container_width=True,
            hide_index=True,
        )

    with col_right:
        st.subheader("Cycle de vie en 8 étapes (vue PLM)")
        st.dataframe(
            df_lifecycle_rflp.sort_values("Ordre").reset_index(drop=True),
            use_container_width=True,
            hide_index=True,
        )

    st.markdown("### Matrice Exigences (RFLP) × Cycle de vie (8 étapes)")
    st.write(
        "Cette matrice montre, pour chaque pilier, comment les exigences s'expriment à chaque étape du cycle de vie."
    )
    st.dataframe(
        df_rflp_lifecycle.reset_index(drop=True),
        use_container_width=True,
        hide_index=True,
    )


# ===========================
# FONCTIONNEL / ARCHITECTURE
# ===========================
elif page == "Fonctionnel / Architecture":
    st.title("Vue fonctionnelle et architecture logique du vaccin VIH")

    col_func, col_arch = st.columns(2)

    with col_func:
        st.subheader("Analyse fonctionnelle du vaccin")
        st.markdown(
            """
            - Répondre à un **besoin médical** (prévention VIH)  
            - Garantir la **sécurité** des volontaires et des patients  
            - Assurer la **qualité pharmaceutique** du produit  
            - Obtenir et maintenir l’**AMM**  
            - Assurer une **production industrielle** robuste et traçable  
            - Gérer la **pharmacovigilance** et la fin de vie du produit
            """
        )

    with col_arch:
        st.subheader("Architecture logique")
        st.markdown(
            """
            1. **Données d’entrée** : besoins médicaux, référentiels FDA/EMA, standards GxP  
            2. **Bloc R&D** : préclinique, design produit, dossiers scientifiques  
            3. **Bloc Clinique** : essais I–III, données de sécurité et d’efficacité  
            4. **Bloc Qualité / Production** : CMC, GMP, libération lots, chaîne du froid  
            5. **Bloc Réglementaire** : CTD, AMM, interactions autorités  
            6. **Bloc Post-AMM** : PV, suivi efficacité réelle, archivage et change control
            """
        )

        st.subheader("Schéma logique rapide")
        graph_code = """
        digraph G {
            rankdir=LR;
            node [shape=box, style=rounded];

            Entree      [label="Besoins médicaux\\nRéférentiels FDA/EMA"];
            RD          [label="R&D\\nPréclinique / Design"];
            Clinique    [label="Clinique\\nEssais I–III"];
            QualiteProd [label="Qualité / Production\\nCMC, GMP, Libération"];
            Reglement   [label="Réglementaire\\nCTD, AMM"];
            PostAMM     [label="Post-AMM\\nPV, archivage, change control"];

            Entree -> RD -> Clinique -> QualiteProd -> Reglement -> PostAMM;
        }
        """
        st.graphviz_chart(graph_code)

# ===========================
# METHODOLOGIE IVV
# ===========================
elif page == "Méthodologie IVV":
    st.title("Méthodologie IVV – Intégration, Vérification, Validation")

    st.markdown(
        """
        - Intégration : relier exigences, change control, jumeau réglementaire et archivage  
          avec des identifiants communs et des rôles clairs.  
        - Vérification : vérifier les règles GxP (Annexe 11, 21 CFR Part 11, intégrité des données) :  
          audit trail, droits d'accès, cohérence des statuts.  
        - Validation : rejouer des scénarios complets (Exigence → Changement → Document mis à jour  
          → Preuve archivée) et montrer le résultat dans ce jumeau numérique.
        """
    )


# ===========================
# ARCHIVAGE SECURISE
# ===========================
elif page == "Archivage sécurisé":
    st.title("Politique d'archivage sécurisé – VIH")

    st.dataframe(df_archiving.reset_index(drop=True), use_container_width=True, hide_index=True)

    st.markdown(
        """
        Je garde aussi :
        - Versioning et audit trail pour tous les documents GxP  
        - Métadonnées complètes (ID, version, date, statut, hash)  
        - Capacité à retrouver une preuve en quelques secondes lors d'une inspection
        """
    )


# ===========================
# CHANGE CONTROL / AUDIT TRAIL
# ===========================
elif page == "Change control / Audit trail":
    st.title("Change control et audit trail – exemple de scénario")

    st.write("Exemple de changement réglementaire sur le vaccin VIH et impact sur le PLM.")
    st.dataframe(
        df_audit_trail.reset_index(drop=True),
        use_container_width=True,
        hide_index=True,
    )


# ===========================
# SOUMISSION REGLEMENTAIRE
# ===========================
elif page == "Soumission réglementaire":
    st.title("Soumission réglementaire – EMA / ANSM")

    st.markdown(
        """
        - Procédure centralisée EMA (Règlement (CE) 726/2004)  
        - Code communautaire des médicaments (Directive 2001/83/EC)  
        - Dossier CTD complet : qualité, sécurité, efficacité  
        - Étapes nationales France (ANSM, HAS) et mise en place de la pharmacovigilance  
        - Le jumeau réglementaire sert à montrer où se trouvent les documents et preuves
          associés à chaque exigence, en quelques clics.
        """
    )
