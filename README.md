# DTSA-5506-Tesla-Global-Deliveries

A data science project for analyzing Tesla's global deliveries.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modeling
│   └── raw            <- The original, immutable data dump
├── docs               <- A default mkdocs project; see mkdocs.org for details
├── models             <- Trained and serialized models, model predictions, or model summaries
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         dtsa_5506_tesla_global_deliveries and configuration for tools like black
├── references         <- Data dictionaries, manuals, and all other explanatory materials
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
├── setup.cfg          <- Configuration file for flake8 and other tools
└── src                <- Source code for use in this project
    ├── __init__.py    <- Makes src a Python module
    ├── config.py      <- Store useful variables and configuration
    ├── dataset.py     <- Scripts to download or generate data
    ├── features.py    <- Scripts to turn raw data into features for modeling
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py <- Code to run model inference with trained models
    │   └── train.py   <- Code to train models
    └── plots.py       <- Code to create visualizations
```

--------

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/korkridake/DTSA-5506-Tesla-Global-Deliveries.git
cd DTSA-5506-Tesla-Global-Deliveries
```

2. Install dependencies:
```bash
make requirements
```

Or manually:
```bash
pip install -r requirements.txt
```

### Usage

- **Make Dataset**: Process raw data into cleaned data
  ```bash
  make data
  ```

- **Build Features**: Generate features from processed data
  ```bash
  make features
  ```

- **Train Model**: Train machine learning models
  ```bash
  make train
  ```

- **Make Predictions**: Run predictions with trained models
  ```bash
  make predict
  ```

- **Clean**: Remove compiled Python files
  ```bash
  make clean
  ```

- **Lint**: Check code style
  ```bash
  make lint
  ```

## Project Structure

This project follows the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) project structure, which provides a logical, reasonably standardized, and flexible project structure for doing and sharing data science work.

## License

See the [LICENSE](LICENSE) file for details.