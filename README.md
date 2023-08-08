## Step by Step Machine Learning project with best practice project structure.
 <br>

mlproject<br>
├── app.py<br>
├── artifacts<br>
│   ├── data.csv<br>
│   ├── model.pkl<br>
│   ├── preprocessor.pkl<br>
│   ├── test.csv<br>
│   └── train.csv<br>
├── notebook<br>
│   ├── 1 . EDA STUDENT PERFORMANCE.ipynb<br>
│   ├── 2. MODEL TRAINING.ipynb<br>
├── README.md<br>
├── requirements.txt<br>
├── setup.py<br>
├── src<br>
│   ├── components<br>
│   │   ├── data_ingestion.py<br>
│   │   ├── data_transformation.py<br>
│   │   ├── model_trainer.py<br>
│   ├── exception.py<br>
│   ├── logger.py<br>
│   ├── pipeline<br>
│   │   ├── predict_pipeline.py<br>
│   │   ├── train_pipeline.py<br>
│   ├── utils.py<br>
└── templates<br>
    ├── home.html<br>
    └── index.html<br>

<br>

## Steps

Step 1: Github and Code Setup:<br>
New environment create,<br>
github repository creation,<br>
sync with local folder and github, <br>
mini project structure (setup.py),<br>
requirements.txt<br>

Step 2: Project Structure, Logging and Exception Handling:<br>
requirements.txt==>in this file we will keep all the libraries and dependencies<br><br>
setup.py==>setup.py is responsible for creaating my application aas a package in pypi. it creates a connection with requirements.txt to import packages.<br>
exception.py==>handles all exception using custom exception handling with error messaage<br>
logger.py==>logs all the information of success and exception.<br>
components ==> data ingestion, data transformation and model training.
pipeline==> predict pipeline, train pipeline.

Step 3: Exploratory data analysis and Model training in colab/jupyter notebook.<br>

Step 4: Data Ingestion:<br>
Data Ingestion is responsible for collecting data from various sources and divide the data into convenient format like train-test data by tranformation pipeline.<br>
data_ingestion.py==> In our case, we use dataset from local database(.csv file) and divide the data set into train set and test set, initiate the data transformation and model traianer <br>

Step 5: Data Transformation:<br>
Data Transfromation is responsible for feature transformation: creating pipeline for handling numerical data & categorical data and other necessary.<br>
data_transformation ==> In our case, we create a pipe line for categorical data transformation and one pipeline for numerical data transformation. Then combine the two pipeline and named as preprocessor. <br>

Step 6: Utils:<br>
It is a kind of helper where common functionalities are stored that entire project can use.<br>
utils.py ==>In our case, saving pickle function <br>
model evaluation function <br>

Step 7: Model Trainer:<br>
model_trainer.py ==>. In model trainer, I apply different regression technique and ensemble technique then predict from the test data calculate the r2_score.Later I applied hyperparatuning for better exploration. Among the models, I extract the best model.<br>

Step 8: Prdiction Pipeline: <br>
predict_pipeline ==> In this file, I created a web application which will be interacting with pickle files( to transform categorical and neumerical and predict with best model) with respect to input data that I given in the form.<br>
app.py ==> containing the route definitions and the logic for handling requests and generating appropriate responses  data transformation and prediction.<br>

Step 9: Model Deployment: <br>
Deployment in AWS Elastic beanstalk with continous delivery method.


