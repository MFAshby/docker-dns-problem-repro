FROM python:3-slim
COPY app.py app.py
ENV N_INSTANCES 10
CMD python app.py $N_INSTANCES
