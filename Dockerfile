FROM python:3
RUN apt update && apt install -y dnsutils
COPY app.py app.py
ENV N_INSTANCES 10
CMD python app.py $N_INSTANCES
