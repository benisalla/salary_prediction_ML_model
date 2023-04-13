# salary_prediction_ML_model
# Salary Prediction Machine Learning Project

This project is aimed at predicting the salary of an employee based on certain features such as experience, test score and interview score. It employs three different machine learning algorithms namely Linear Regression, KNN, and SVM. The implementation of these algorithms was done using Python and Colab notebook was used for scripting. After the development process was completed, the application was then deployed on the Render Platform, a cloud hosting platform. 

## Project Structure
- templates/
- Procfile
- README.md
- data/
    * hiring.csv
- main.py
- model/
    * model.py
    * modelKNN.pkl
    * modelLR.pkl
    * modelSVM.pkl
- requirements.txt

The `templates/` directory is where the HTML templates for the web application would be stored.

The `data/` directory is where the input data (`hiring.csv`) is stored.

The `model/` directory contains the code for the machine learning model (`model.py`) and the trained models (`modelKNN.pkl`, `modelLR.pkl`, `modelSVM.pkl`).

All other files such as `Procfile`, `README.md`, and `requirements.txt` should be placed in the root directory of the project.

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
