#!/bin/bash                                                                                                  
docker container run -it --rm --name service_essentials -v "/media/ProjetBI":/app/data/ -v "/media/ProjetBI":/app/fetch/ -v LOG:/app/log etl_essentials:v1
