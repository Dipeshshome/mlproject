## Step by Step Machine Learning project with best practice project structure.

Step 1: Github and Code Setup:
New environment create,
github repository creation,
sync with local folder and github, 
mini project structure (setup.py),
requirements.txt

Step 2: Project Structure, Logging and Exception Handling:
requirements.txt==>in this file we will keep all the libraries and dependencies
setup.py==>setup.py is responsible for creaating my application aas a package in pypi. it creates a connection with requirements.txt to import packages.
exception.py==>handles all exception using custom exception handling with error messaage
logger.py==>logs all the information of success and exception.

Step 3: Exploratory data analysis and Model training in colab/jupyter notebook.

Step 4: Data Ingestion:
Data Ingestion is responsible for collecting data from various sources and divide the data into convenient fromat like train-test data by tranformation pipeline.
In our case, we use dataset from local database(.csv file) and divide the data set into train set and test set using transformation. finally from data ingestion file we will get train data and test data for furture exploration.

Step 5: Data Transformation:
Data Transfromation is responsible for feature transformation: creating pipeline for handling numerical data & categorical data and other necessary.
In our case, we create a pipe line for categorical data transformation and one pipeline for numerical data transformation. Then combine the two pipeline and named as preprocessor. 

Step 6: Utils:
It is a kind of helper where common functionalities are stored that entire project can use.












