FROM continuumio/anaconda3:4.4.0
MAINTAINER UNP, tedthiaka
RUN MKDIR app
COPY ./Model /app
EXPOSE 5000
WORKDIR /app
RUN pip install -r requirements.txt
CMD python RandomForestAPI.py