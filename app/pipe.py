# Import modules
import pandas as pd
import pickle as pkl
from xgboost import XGBClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# Load data
credit = pd.read_csv('../data/credit_c.csv')

# Create train and test sets
X = credit.iloc[:,0:-1]
y = credit.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Set pipeline parameters
scaler = MinMaxScaler()
clf = XGBClassifier(colsample_bytree= 0.8, gamma= 5, 
                    max_depth= 3, min_child_weight= 1, 
                    subsample= 1.0)

# Create pipeline
pipe = Pipeline(steps=[
                ('scaler', scaler),
                ('classifier', clf) 
                ])

# Fit pipeline
pipe.fit(X_train, y_train)

# Save pipe to disk
pkl.dump(pipe, open('../app/pipe.pkl','wb'))

# Load pipe from disk
pipe = pkl.load(open('../app/pipe.pkl', 'rb'))

# Predict test data with pipeline
y_pred = pipe.predict(X_test)
predictions = [round(value) for value in y_pred]
print(predictions[0:50])
pipe