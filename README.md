# Telco Classification Project by Rajvinder Kaur Dadiala
<a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-013243.svg?logo=python&logoColor=white"></a>
<a href="#"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="NumPy" src="https://img.shields.io/badge/Numpy-2a4d69.svg?logo=numpy&logoColor=white"></a>
<a href="#"><img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-8DF9C1.svg?logo=matplotlib&logoColor=white"></a>
<a href="#"><img alt="seaborn" src="https://img.shields.io/badge/seaborn-65A9A8.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="plotly" src="https://img.shields.io/badge/plotly-adcbe3.svg?logo=plotly&logoColor=white"></a>
<a href="#"><img alt="sklearn" src="https://img.shields.io/badge/sklearn-4b86b4.svg?logo=scikitlearn&logoColor=white"></a>
<a href="#"><img alt="SciPy" src="https://img.shields.io/badge/SciPy-1560bd.svg?logo=scipy&logoColor=white"></a>

**Customer churn** is one of the most important metrics for a growing business to evaluate. It's easier to save an existing customer before they leave than to convice them to come back. Understanding and preventing customer churn is critical to company's 

**long-term success**.

In this project, we will use statistical testing to analyze the key factors of customers who are more likely to churn, develop a classification model to predict churn based on those factors, and provide recommendations for retaining customers as well as predictions of churn for a list of customers (delivered via csv).

## Business Goals
- Find drivers for customer churn at Telco. Why are customers churning?

- Construct a ML classification model that accurately predicts customer churn.

- Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?

## Initial Questions
- Which variables are associated with churn?

- Are average monthly charges higher for customers who churn?

- Are tenure shorter for customer who churn?

- Are additional services independent with churn?

## Data Dictionary
**Variable** |    **Value**    | **Meaning**
---|---|---
*Contract Type* | 1) Month-to-month 2) One year 3) Two year| This indicates what type of contract the customer has
*Internet Service Type* | 1) DSL 2) Fiber Optic 3) None | This indicates what type of internet service the customer has, if any
*Payment Type* | 1) Bank transfer 2) Credit card 3) Electronic check 4) Mailed check | This tells us how is the customer paying for the service
*Monthly Charges* | Float number | This tells us how much is the customer paying each month
*Teunure* | Integer ranging from 0-72 | This shows how long (months) does the customer stay with the company
*Online Bakcup* | 1) Yes 2) No 3) No internet service | This indicates if the customer has online backup service
*Online Security* | 1) Yes 2) No 3) No internet service | This indicates if the customer has online security service
*Tech Support*| 1) Yes 2) No 3) No internet service | This indicates if the customer has tech support service
*Device Protection* | 1) Yes 2) No 3) No internet service | This indicates if the customer has device protection service
*Streaming TV* | 1) Yes 2) No 3) No internet service | This indicates if the customer has streaming tv service
*Streaming Movies* | 1) Yes 2) No 3) No internet service | This indicates if the customer has streaming movies service
