VAX-PLM — Digital Regulatory Twin (VAX-HIV-2030)
Overview

VAX-PLM is an interactive digital regulatory twin designed to model the complete Product Lifecycle Management (PLM) flow of a fictional vaccine: VAX-HIV-2030.

The application centralizes all regulatory components—requirements, documents, evidence, quality, IoT monitoring, lifecycle, audit trail, and submission—to provide a unified and traceable view of regulatory compliance aligned with EMA and ANSM expectations.

This project illustrates how a regulatory ecosystem can be organized, visualized, and navigated using a modern data application.

Objectives

Model a realistic regulatory workflow used in vaccine development.

Provide end-to-end traceability between:

Requirements

Documents

Evidence

Deliver a multi-view dashboard covering:

Quality and GMP aspects

Cold chain and IoT monitoring

Lifecycle stages (R&D to pharmacovigilance)

Archiving and audit trail

Regulatory submission pathways

Allow CSV import and automatic relational fusion using PLM-style mappings.

Present an intuitive, structured UX suitable for training and demonstration.

Main Features
1. Requirements – Documents – Evidence Mapping

Users can upload CSV files and automatically visualize the connections between:

Requirement and its associated document

Document and its evidence

Requirement and its evidence

The system merges and standardizes datasets to rebuild traceability matrices used in real validation dossiers.

2. Multi-Page Interactive Application

The application is organized into dedicated modules, each representing a key regulatory activity:

Requirements

Documents

Evidence

Regulatory Dashboard

Quality Control

IoT Monitoring (cold chain)

Lifecycle Management

Regulatory Submission

Secure Archiving

Audit Trail

3. Pharmaceutical Lifecycle Modeling

A complete lifecycle representation is included:

Fundamental Research

Preclinical Development

Clinical Development (Phases I–III)

Industrial Production (GMP)

Marketing Authorization Application

Commercialization and Distribution

Pharmacovigilance and Post-Market Surveillance

4. IoT Monitoring (Temperature / Cold Chain)

Simulates monitoring of temperature data for fridges, freezers, laboratories, and transport.
Useful to illustrate chain-of-custody, temperature excursions, stability and quality risk assessment.

5. Regulatory Submission Simulation

Summarizes the key deliverables and data packages required for EMA or ANSM submission, including validation, consistency, and completeness checks.

Project Structure
Pages/
  Documents.py
  Evidence.py
  IoT_Monitor.py
  Lifecycle_Management.py
  Quality_Control.py
  Regulatory_Dashboard.py
  Regulatory_Submission.py
  Requirements.py

streamlit_app.py
dataset.py
requirements.txt
README.md

streamlit_app.py

Main entry point. Handles dataset import, initial layout, navigation, and fusion logic.

Pages/*.py

Each file corresponds to a regulatory domain or dashboard section.

Technology Stack

Python 3

Streamlit

Pandas

Plotly or Matplotlib (depending on the page)

CSV datasets

GitHub Codespaces

Streamlit Cloud for deployment

Running Locally
pip install -r requirements.txt
streamlit run streamlit_app.py

Deployment

The application is deployed on Streamlit Cloud.
Once deployed, the public link should be added here:

<Insert your Streamlit Cloud URL here>

Value of the Project

This project demonstrates:

Understanding of pharmaceutical regulatory workflows

Ability to structure a PLM-like regulatory system

Development of a multi-page web dashboard

Data cleaning, merging and traceability reconstruction

Cold chain and quality monitoring concepts

Code organization and documentation

Deployment using Streamlit Cloud

It is a strong example of how data, software, and regulatory knowledge can be combined into a realistic and impactful demonstration project.

Author

Myriam Ait Said
Data & AI — PLM / Regulatory Systems

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
