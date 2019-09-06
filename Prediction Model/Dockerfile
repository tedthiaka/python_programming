FROM continuumio/anaconda3:4.4.0
MAINTAINER UNP, tedthiaka
RUN MKDIR app
COPY ./random_forest.pkl /app
EXPOSE 5000
WORKDIR /app
RUN pip install -r requirements.txt
CMD python RandomForestAPI.py