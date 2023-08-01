## Step by Step Machine Learning project with best practice project structure.

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
model_trainer.py ==>. In model trainer, we apply different regression technique and ensemble technique then predict from the test data calculate the r2_score. Among the models, we extract the best model.<br>
