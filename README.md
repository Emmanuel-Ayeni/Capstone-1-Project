# CapstoneProject-1

# HR-Attrition-ML-Project
Project Title: Capstone 1 Project: A Supervised Machine Learning Project
Brief Description: The HR Employee Attrition Application is designed to solve a Classification problem.


## Project Overview
Goals: Determine an employee at a higher risk of leaving the company.
Data Sources: The source is from Kaggle: https://www.kaggle.com/datasets/whenamancodes/hr-employee-attrition 

## Objectives: 
* The task focus is to build an HR Employee Attrition Application which includes the best predictive model.
* When deployed and the HR Employee Apps service is called, the model can identify which employees are at a higher risk of leaving the company.
* This could help in taking some proactive measures to retain valuable employees.

## Environment Setup 

* <b> Unix: </b> WSL Ubuntu system
* H
I've included instructions for reproducing your work.

Highlight key features, technologies, and tools used.
Project Structure:

For a project, your repository/folder should contain the following:
**************************************************************************************************************************
## README.md with
* Description of the problem
* Instructions on how to run the project
## Data
* You should either commit the dataset you used or have clear instructions on how to download the dataset
## Notebook (suggested name - notebook.ipynb) with
* Data preparation and data cleaning
* EDA, feature importance analysis
* Model selection process and parameter tuning
## Script train.py (suggested name)
* Training the final model
* Saving it to a file (e.g. pickle) or saving it with specialized software (BentoML)
## Script predict.py (suggested name)
* Loading the model
* Serving it via a web service (with Flask or specialized software - BentoML, KServe, etc)
## Files with dependencies
* Pipenv and Pipenv.lock if you use Pipenv
* bentofile.yaml if you use BentoML
* or equivalents: conda environment file, requirements.txt or pyproject.toml
# Dockerfile for running the service
# Deployment
* URL to the service you deployed or
* Video or image of how you interact with the deployed service

