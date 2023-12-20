# CapstoneProject-1

# HR-Attrition-ML-Project
Project Title: Capstone 1 Project: A Supervised Machine Learning Project
Brief Description: The HR Employee Attrition Application is designed to solve a Classification problem.


## Project Overview
Goals: Determine an employee at a higher risk of leaving the company.

## Data Source
Data Source: The source is from Kaggle: https://www.kaggle.com/datasets/whenamancodes/hr-employee-attrition 

## Objectives: 
* The task focus is to build an HR Employee Attrition Application which includes the best predictive model.
* When deployed and the HR Employee Apps service is called, the model can identify which employees are at a higher risk of leaving the company.
* This could help in taking some proactive measures to retain valuable employees.

## Environment Setup 

* <b> Unix: </b> WSL Ubuntu system
* <b> Pipenv: </b> 
* <b> Docker: </b>
* <b> AWS: </b>
## Highlight key features, technologies, and tools used.

## Notebook (attrition-Logistic_v2.ipynb) with
* Data preparation and data cleaning
* EDA, feature importance analysis
* Model selection process and parameter tuning
## Script train.py
* Training the final model
* Saving it to a file (e.g. pickle) 
## Script attrition_serving.py
* Loading the model
* Serving it via a web service (with Flask)
## Files with dependencies
* Pipenv and Pipenv.lock if you use Pipenv
# Dockerfile for running the service


