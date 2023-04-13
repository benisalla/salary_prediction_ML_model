# salary_prediction_ML_model
# Salary Prediction Machine Learning Project

This project is aimed at predicting the salary of an employee based on certain features such as experience, test score and interview score. It employs three different machine learning algorithms namely Linear Regression, KNN, and SVM. The implementation of these algorithms was done using Python and Colab notebook was used for scripting. After the development process was completed, the application was then deployed on the Render Platform, a cloud hosting platform. 

## Project Structure

- **Data:** This directory contains the dataset that was used for training the machine learning models. The file type is a CSV file.

- **Notebooks:** This directory contains the Jupyter Notebooks that were used for feature engineering, model selection, training, and model evaluation.

- **app.py:** This file contains the web application that was developed using Flask to deploy the machine learning models. 

- **model.pkl:** This file contains the trained model that was used to generate the predictions on the web application.

- **requirements.txt:** Specifies the required Python packages to be installed before deploying the application.

## Usage

To predict salaries using the web application, simply follow the link provided below:

https://salary-prediction-ml-project.onrender.com/

Once the webpage has fully been loaded, you can then enter the relevant employee data such as job title, experience, and education level. After submitting the form, the webpage will display the predicted salary based on the chosen machine learning algorithm.

## Deployment

To deploy the application on Render, the following steps were taken:

1. A Git repository was created for the project
2. The code was pushed to the Git repository
3. The Render CLI was installed and initialized
4. A new Render service was created with the following specifications:
    - Dockerfile path: `Dockerfile`
    - Build command: `pip install -r requirements.txt && python app.py`
    - Start command: `python app.py`
5. The Render service was then deployed and the web application became available on the provided URL.

## Conclusion

In conclusion, this machine learning project successfully trained and evaluated three machine learning algorithms to predict the salaries of employees based on their experience, job title, and education level. The web application provides a user-friendly interface for easy interaction with the various models. Deploying the application on Render allowed for easier management and distribution of the application.
