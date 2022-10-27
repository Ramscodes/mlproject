# mlproject
My first ML project 

To start the machine learning project we need the following requirements

Software and Account Requirement:=>
```````````````````````````````````

1.[Github Account](https://github.com/) 
2.Heroku Account
3.VS Code IDE
4.GIT cli 

Creating the conda environment 
``````````````````````````````
->conda create -p venv python==3.7 -y
->conda activate venv\

Installing requirements 
````````````````````````
->pip install -r requirements.txt

Building Docker Image
```````````````````````````````
->docker build -t <image_name>:<tagname> .
Note :- image name should be in lower case 

Listing docker images 
````````````````````````````````````
-> docker images

To run docker image 
````````````
->docker run -p 5000:5000 -e PORT=5000 <IMAGE_ID>

To check running containers 
``````````````````````
-> docker ps 

To stop running containers
`````````````````````````
-> docker stop <container_id>



