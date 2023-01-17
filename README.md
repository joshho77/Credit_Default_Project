### LHL Final Project | By Josh Ho
# **Credit Eligibility Model Using Supervised Learning**

## **Introduction**
Banks are large contributors to the economy, having immense monetary influence on how countries, governments, societies, and individuals’ function and develop. By providing credit to borrowers in search of a capital, borrowers are able to start businesses, purchase homes, pay for school tuition, go on dream vacations and fund other important life decisions.

But before approving credit, banks and lenders require understanding their clients needs and analyzing their financial background in order to decide whether offering credit will be beneficial to both parties, or harmful. This is where creating a credit scoring model can be developed to optimize and support this process.

Outputs received from model can be used to help inform creditors and borrowers alike on whether they should opt to lend or borrow money respectively.

_Topics: Data Science, Business, Modeling, Machine Learning, Classification Task, Finance, Banking_

---

## **Goal**
- Develop a credit scoring algorithm that can predict the probability of a borrower defaulting on a line of credit within 2 years 
- Deploy model to cloud with a graphical user interface to make model available for user predictions, and business decision making

--- 

## **Description**
- Classification task involving creating a model that will output the whether a borrower will default on a line of credit, detailing their eligiblity for future loans and credit
- Uses data on past borrowers mapped to several features pertaining to relevant financial information, as well as a target variable (whether the borrower has missed a credit payment past 90 days)

### **Tech Stack**
- Python (Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, XGBoost, Flask)
- Docker
- AWS
- VS Code
- GitHub
 
---

## **Project Workflow**
1.	**Data Collection** - Collect and load dataset from Kaggle competition ('GiveMeSomeCredit').

2.	**Data Preprocessing** - Familiarize self with dataset and perform data cleaning processes such as: imputing nulls, handling outliers, removing duplicates, and renaming and dropping certain columns.

3.	**Exploratory Data Analysis** - Perform EDA on cleaned data, visualizing data to allow for further investigation and highlighting of key trends and insights derived from analysis. 

4.	**Feature Engineering** - Extract and engineer new features to improve quality of results when inputting data into model testing.

5.	**Model Building** - Train-test-split cleaned data, scale data accordingly and feed data into multiple classifiers to calculate model baselines.

6.	**Model Pipeline** - Create pipeline with multiple classifiers and varying hyperparameters to determine which model will be the most effective for specific classification task.

7.	**Model Evaluation & Tuning** - Optimize pipeline with multiple classifiers and respective hyperparameters using grid search, outputting best classifier and parameters, best pipeline, and best score, and if they outperform model baselines. 

8.	**Model Deployment** - Build Docker image with project files to containerize pipeline, deploy optimized pipeline to cloud using Flask and AWS EC2 instance for user access and live predictions. 

9.	**Version Control** - Push files to GitHub for version control and file persistance via online repository.



