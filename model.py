import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

dataset = pd.read_csv('hiring.csv')

dataset['experience'].fillna(0, inplace=True)

dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

X = dataset.iloc[:, :3]


# Converting words to integer values
def convert_to_int(word):
    word_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'zero': 0, 0: 0}
    return word_dict[word]


X['experience'] = X['experience'].apply(lambda x: convert_to_int(x))

y = dataset.iloc[:, -1]

# Splitting Training and Test Set
# Since we have a very small dataset, we will train our model with all availabe data.


LR = LinearRegression()
supportVectorMachine = svm.SVC()
KNN = KNeighborsClassifier()

# Fitting model with trainig data
LR.fit(X.values, y.values)
KNN.fit(X.values, y.values)
supportVectorMachine.fit(X.values, y.values)

# Saving model to disk
pickle.dump(LR, open('modelLR.pkl', 'wb'))
pickle.dump(KNN, open('modelSVM.pkl', 'wb'))
pickle.dump(supportVectorMachine, open('modelKNN.pkl', 'wb'))

# Loading model to compare the results
modelLR = pickle.load(open('modelLR.pkl', 'rb'))
modelSVM = pickle.load(open('modelSVM.pkl', 'rb'))
modelKNN = pickle.load(open('modelKNN.pkl', 'rb'))
print(modelLR.predict([[2, 9, 6]]))
print(modelSVM.predict([[3, 4, 6]]))
print(modelKNN.predict([[3, 5, 2]]))
