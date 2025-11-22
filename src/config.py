"""
Configuration file for project settings and paths.
"""

from pathlib import Path

# Project root directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Data directories
DATA_DIR = PROJECT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

# Model directories
MODELS_DIR = PROJECT_DIR / "models"

# Reports directories
REPORTS_DIR = PROJECT_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Documentation directory
DOCS_DIR = PROJECT_DIR / "docs"

# References directory
REFERENCES_DIR = PROJECT_DIR / "references"
