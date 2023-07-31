## Step by Step Machine Learning project with best practice project structure.

Step 1: Github and Code Setup:<br>
New environment create,<br>
github repository creation,<br>
sync with local folder and github, <br>
mini project structure (setup.py),<br>
requirements.txt<br>

Step 2: Project Structure, Logging and Exception Handling:<br>
requirements.txt==>in this file we will keep all the libraries and dependencies<br>
setup.py==>setup.py is responsible for creaating my application aas a package in pypi. it creates a connection with requirements.txt to import packages.<br>
exception.py==>handles all exception using custom exception handling with error messaage<br>
logger.py==>logs all the information of success and exception.<br>

Step 3: Exploratory data analysis and Model training in colab/jupyter notebook.<br>

Step 4: Data Ingestion:<br>
Data Ingestion is responsible for collecting data from various sources and divide the data into convenient fromat like train-test data by tranformation pipeline.<br>
In our case, we use dataset from local database(.csv file) and divide the data set into train set and test set using transformation. <br>finally from data ingestion file we will get train data and test data for furture exploration.<br>

Step 5: Data Transformation:<br>
Data Transfromation is responsible for feature transformation: creating pipeline for handling numerical data & categorical data and other necessary.<br>
In our case, we create a pipe line for categorical data transformation and one pipeline for numerical data transformation. Then combine <br>the two pipeline and named as preprocessor. <br>

Step 6: Utils:
It is a kind of helper where common functionalities are stored that entire project can use.<br>












