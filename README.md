# Life Insurance Policy Lapse Prediction

## Project Overview

The **Life Insurance Policy Lapse Prediction** project uses machine learning to predict whether a life insurance policyholder is likely to lapse their policy. It analyzes customer demographics, policy details, premium payment behavior, and customer engagement to identify potential lapse risks.

The project includes a Streamlit web application that allows users to enter policyholder information and obtain a prediction using a trained machine learning model.

## Objectives

- Predict the likelihood of life insurance policy lapse.
- Identify customers who may be at risk of discontinuing their policies.
- Analyze important factors associated with policy lapse.
- Provide an interactive interface for generating predictions.
- Support proactive customer retention strategies.

## Features

- Interactive Streamlit web interface.
- Machine learning-based lapse prediction.
- Pre-trained model loading using Joblib.
- Data processing using Pandas.
- Prediction using customer and policy-related features.
- Results displayed through the web application.

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Data Processing:** Pandas
- **Machine Learning:** Scikit-learn (if used to train the model)
- **Model Serialization:** Joblib
- **Development Tools:** VS Code, Jupyter Notebook

## Project Structure

```text
life-insurance-policy-lapse-prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── life_insurance_lapse_final_model.pkl
├── demo_dataset_Life_Insurance_Policy_Lapse.csv
└── notebook.ipynb
```

*Note: The filenames above are examples. Keep only the files that actually exist in your project, and use your actual filenames.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL](https://github.com/Kaustubh1203/ML_project.git
```

Navigate to the project directory:

```bash
cd ML_project
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## How It Works

1. The application loads the pre-trained machine learning model and its associated preprocessing components.
2. The user provides the required policyholder information.
3. The application prepares the input features expected by the model.
4. The model generates a prediction.
5. The application displays the predicted lapse outcome.

## Dataset

The project uses a life insurance policy dataset containing customer, policy, premium payment, and engagement-related information.

Only use datasets that are permitted to be shared publicly. Do not upload confidential customer information.

## Potential Business Benefits

- Early identification of high-risk policyholders.
- More targeted customer retention campaigns.
- Improved customer engagement.
- Better-informed policy retention decisions.

## Future Enhancements

- Add model performance metrics and evaluation visualizations.
- Improve explainability using feature importance or SHAP.
- Develop customer risk dashboards and reporting.
- Deploy the application to a cloud hosting platform.
- Integrate secure database storage and customer retention workflows.

## Disclaimer

This project is intended for educational and analytical purposes. Predictions are estimates and should not be used as the sole basis for insurance or financial decisions.

## Author

**Kaustubh Awagan**

