![phData Logo](img/phData_color_rgb.jpg "phData Logo")

# Machine Learning Engineer Candidate Project

### Task 1: Deploy the Basic Model

The model is deployed as a Flask web service. The external API has one method: predict(), where users can submit a JSON-formatted POST request containing the model-input . This will load and run the pickled model and send the predictions back in JSON format. At this point, I haven’t included any model validation/version control as part of the application. 

Code for flask application and the Docker file are in app_services folder. I've used a shell script to submit a curl command to test the flask api.

My initial test was with just the app.py (flask app) + another python script which would send a POST to the flask app and receive predictions back in JSON format.

#### how to scale the flask app for production deployment:

The flask application itself, the way it is currently at, is for development purposes. To productionize this app, I could use Gunicorn or Nginx for scaling out and handling multiple threads/requests.


#### Fun with Docker: 

Yesterday, I played with Docker and was able to create and run a docker image on my local. I used the same curl command to submit a POST to the app and received predictions back.

Below are the steps I followed to create and run the docker.
1. Built docker image using the command below which used the Dockerfile and requirements for pip installation in the directory. 

   `docker build -t flaskapp:latest .`
2. Run the docker image created above which initates the flask app

   `docker run -p 5000:5000 flaskapp:latest`

Note: I have used pip for environment creation, as it was more straight-forward compared to conda. I have tried conda with some hiccups and respecting time for submission of this project, I've added it to my to-do list to play with it in the near future. 

** This is currently only a desktop version of docker implementation. 

#### How to scale this docker application:
1. There seem to be several options to scale. Docker-compose, Docker-swarm, Kubernetes and of course, many cloud solutions such as Amazon's ECS.

