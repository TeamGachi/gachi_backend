# Gachi 
You can share your photos , schedules with your friends without handwork.  
AI based service to classify your picture within many photo clusters.  
## Stack 
* Django
* Celery
* RestFrameWork
* Docker
* Docker Compose
* Nginx
## Architecture 
* app
  * Django application 
* data
  * This directory would mount on your container inside volume
* nginx
  * web-server which will provide `reverse proxy` and `load balancing`
## Pre-requirments
* Docker
* Docker compose 
## Deployment 
this back-end could be deploy by `docker` and `docker-compose` in single-node.  
You could deploy it by `pip` and your own python >= 3.11 interpreter but not recommended. 
1. `git clone git@github.com:TeamGachi/gachi_backend.git`
2.  move to directory root
3.  (optional) nginx configuration has been doen in my `docker hub` but if you want your own config , then config via `mount` opiont in `yaml`
4.  (optional) if your not `x86_64/linux` then `docker compose build`
5.  `docker compose up -d`
