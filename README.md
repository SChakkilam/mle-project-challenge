![phData Logo](img/phData_color_rgb.jpg "phData Logo")

# Machine Learning Engineer Candidate Project

### Task 1: Deploy the Basic Model

The model is deployed as a Flask web service. The external API has one method: predict(), where users can submit a JSON-formatted POST request containing the model-input . This will load and run the pickled model and send the predictions back in JSON format. At this point, I haven’t included any model validation/version control as part of the application. 

Code for flask application and the Docker file are in app_services folder. I've used a shell script to submit a curl command to test the flask api.

My initial test was with just the app.py (flask app) + another python script which would send a POST to the flask app and receive predictions back in JSON format.

However, yesterday, I played with Docker and was able to create and run a docker image on my local. I used the same curl command to submit a POST to the app and received predictions back.

This is currently only a desktop version of docker implementation. Below are a few points that I've noted from my research and learning for Docker services.

#### How to scale this application:
1. There seem to be several options to scale. Docker-compose, Docker-swarm and of course, many cloud solutions available, one that I'm aware of is Amazons ECS and Kubernetes as well.
2. The flask application itself, the way it is currently at, is for development purposes. To productionize this app, I could use Gunicorn or Nginx for scaling out and handling multiple threads/requests.
