import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor

st.write("""
# Boston House Price Prediction App
App for predicting **Boston House Prices**
""")
st.write('---')

# Loads the Boston House Price Dataset
boston = datasets.load_boston()
X = pd.DataFrame(boston["data"], columns=boston["feature_names"])
Y = pd.DataFrame(boston["target"], columns=["MEDV"])

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    # print(X.CRIM.mean())
    CRIM = st.sidebar.slider('CRIM', int(X.CRIM.min()), int(X.CRIM.max()), int(X.CRIM.mean()))
    ZN = st.sidebar.slider('ZN', int(X.ZN.min()), int(X.ZN.max()), int(X.ZN.mean()))
    INDUS = st.sidebar.slider('INDUS', int(X.INDUS.min()), int(X.INDUS.max()), int(X.INDUS.mean()))
    CHAS = st.sidebar.slider('CHAS', int(X.CHAS.min()), int(X.CHAS.max()), int(X.CHAS.mean()))
    # NOX = st.sidebar.slider('NOX', int(X.NOX.min()), int(X.NOX.max()), int(X.NOX.mean()))
    RM = st.sidebar.slider('RM', int(X.RM.min()), int(X.RM.max()), int(X.RM.mean()))
    AGE = st.sidebar.slider('AGE', int(X.AGE.min()), int(X.AGE.max()), int(X.AGE.mean()))
    DIS = st.sidebar.slider('DIS', int(X.DIS.min()), int(X.DIS.max()), int(X.DIS.mean()))
    RAD = st.sidebar.slider('RAD', int(X.RAD.min()), int(X.RAD.max()), int(X.RAD.mean()))
    TAX = st.sidebar.slider('TAX', int(X.TAX.min()), int(X.TAX.max()), int(X.TAX.mean()))
    PTRATIO = st.sidebar.slider('PTRATIO', int(X.PTRATIO.min()), int(X.PTRATIO.max()), int(X.PTRATIO.mean()))
    B = st.sidebar.slider('B', int(X.B.min()), int(X.B.max()), int(X.B.mean()))
    LSTAT = st.sidebar.slider('LSTAT', int(X.LSTAT.min()), int(X.LSTAT.max()), int(X.LSTAT.mean()))
    data = {'CRIM': CRIM,
            'ZN': ZN,
            'INDUS': INDUS,
            'CHAS': CHAS,
            'NOX': 0,
            'RM': RM,
            'AGE': AGE,
            'DIS': DIS,
            'RAD': RAD,
            'TAX': TAX,
            'PTRATIO': PTRATIO,
            'B': B,
            'LSTAT': LSTAT}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

# Build Regression Model
model = RandomForestRegressor()
model.fit(X, Y)
# Apply Model to Make Prediction
prediction = model.predict(df)

st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')

# Using SHAP to explain tree output
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

st.header('Feature Importance')
plt.title('Feature importance based on SHAP values')
shap.summary_plot(shap_values, X)
st.pyplot(plt.gcf(), bbox_inches='tight')
st.write('---')

plt.title('Feature importance based on SHAP values (Bar)')
shap.summary_plot(shap_values, X, plot_type="bar")
st.pyplot(plt.gcf(), bbox_inches='tight')