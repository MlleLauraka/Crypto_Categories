import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import f1_score as f1
from sklearn.model_selection import train_test_split
from math import sqrt
import time

def app():
	st.title('Risk Analysis: Attrition Prediction')

	# About
	expander_bar = st.expander("About")
	expander_bar.markdown("""
	* **Objectif:** This Algorithm predicts the Attrition(Churn) of a Client in the Banking Industry depending on the values selected. The results depend on the Dataset used as well as the ML Algoritm output.
	* **Python libraries:** Pandas, Streamlit, Scikit.Learn, Plotly.express
	* **Data source:** [Kaggle](https://www.kaggle.com/code/kmalit/bank-customer-churn-prediction/notebook).
	* **Credit:** Websites Plotly, Pandas, StackOverflow and Youtube Channel Data Professor : *[SATSifaction](https://www.youtube.com/watch?v=JwSS70SZdyM)*).
	* **Contact:** *[Laura Kouadio LindedIn](https://www.linkedin.com/in/laura-kouadio-083374131/)
	* **Code:** *[Laura Kouadio GitHub](https://github.com/MlleLauraka)*
	""")


	def run_status():
		latest_iteration = st.empty()
		bar = st.progress(0)
		for i in range(100):
			latest_iteration.text(f'Percent Complete {i+1}')
			bar.progress(i + 1)
			time.sleep(0.1)
			st.empty()

	st.subheader('Multi Model Predictions')

	# Getting the Data
	@st.cache #https://docs.streamlit.io/library/advanced-features/caching
	def load_data():
		df_data=pd.read_csv('Churn_Modelling.csv')
		df_data=df_data.drop(["RowNumber", "CustomerId", "Surname"],axis=1)
		return df_data

	df_data=load_data()
	st.dataframe(df_data)

	# Encoding categorical variables
	one_hot=pd.get_dummies(df_data[['Geography', 'Gender']])
	df_data_good = df_data.drop(columns=['Geography', 'Gender'],axis = 1)
	df_data1 = df_data_good.join(one_hot)

	# Sidebar Options:
	st.sidebar.subheader('Please Select your KYC Input')
	params={
	'Client number of Products' : st.sidebar.selectbox('NumOfProducts',(1,2,3,4)),
	'Client Tenure': st.sidebar.selectbox('Tenure',(0,1,2,3,4,5,6,7,8,9,10)),
	'Client Balance' : st.sidebar.slider('Balance',min(df_data1['Balance']), max(df_data1['Balance'])),
	'Client Estimated Salary' : st.sidebar.slider('EstimatedSalary',min(df_data1['EstimatedSalary']), max(df_data1['EstimatedSalary'])),
	'Client Credit Score' : st.sidebar.slider('CreditScore',350, max(df_data1['CreditScore'])),
	'Client Age' : st.sidebar.slider('Age',18,max(df_data1['Age'])),
	'Is Active Member': 1 if st.sidebar.checkbox('IsActiveMember') else 0,
	'Is Female': 1 if st.sidebar.checkbox('Gender_Female') else 0,
	'Is Male ': 1 if st.sidebar.checkbox('Gender_Male') else 0,
	'Is French': 1 if st.sidebar.checkbox('Geography_France') else 0,
	'Is German': 1 if st.sidebar.checkbox('Geography_Germany') else 0,
	'Is Spanish': 1 if st.sidebar.checkbox('Geography_Spain') else 0,
	'Has a Credit Card': 1 if st.sidebar.checkbox('HasCrCard') else 0,
	}
	#could have put .unique() if it was for categorical variable
	test_size=st.sidebar.slider('Pick Test Size', 0.05,0.5,0.25,step=0.05)

	# Creating the models
	@st.cache(allow_output_mutation=True)
	def get_models():
		y=df_data1['Exited']
		X=df_data1[['CreditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary','Geography_France','Geography_Germany','Geography_Spain','Gender_Female','Gender_Male']]
		X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, shuffle=True)
		models = [
					RandomForestClassifier(n_estimators=190,max_depth=35),
			   		DecisionTreeClassifier(max_depth=26),
			   		AdaBoostClassifier(n_estimators=60, learning_rate=1.2)
			 		]
		df_models = pd.DataFrame()
		temp = {}
		print(X_test)

		#interating all models
		for model in models:
			print(model)
			m = str(model)
			temp['Model'] = m[:m.index('(')]
			model.fit(X_train, y_train)
			temp['F1_Score'] = sqrt(f1(y_test, model.predict(X_test)))
			temp['Pred Value'] = model.predict(pd.DataFrame(params, index=[0]))[0]
			print('F1 score', temp['F1_Score'])
			df_models = df_models.append([temp])
		df_models.set_index('Model', inplace=True)
		pred_value = df_models['Pred Value'].iloc[[df_models['F1_Score'].argmax()]].values.astype(float)
		return pred_value, df_models

	def run_data():
		#run_status()
		df_models=get_models()[0][0]
		if df_models==1:
			A = " thinking about leaving."
		else:
			A= " not thinking about leaving."

		st.write('Given your parameters, the result is **{:.2f}**'.format(df_models)," Therefore, the client is" + A)


	def show_ML():
		df_models=get_models()[1]
		df_models
		st.write('**This diagram shows root mean sq error for all models**')
		st.bar_chart(df_models['F1_Price'])

	btn = st.sidebar.button("Predict")
	if btn:
		run_data()
	else:
		pass

	st.sidebar.subheader('Additional Information')

	if st.sidebar.checkbox('Show ML Models'):
		run_data()
		df_models=get_models()[1]
		df_models
		st.write('**This diagram shows the F1 Score for all models**')
		st.bar_chart(df_models['F1_Score'])
