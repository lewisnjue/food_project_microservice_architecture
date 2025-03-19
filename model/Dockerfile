FROM python:3.10.16-slim-bullseye


WORKDIR /app 

COPY main.py /app 
COPY food_model.onnx /app 
COPY requirements.txt /app 
COPY preprocessing.py /app 
COPY label.pkl /app 
COPY entrypoint.sh /app 

RUN chmod +x entrypoint.sh 


EXPOSE 8080

CMD [ "./entrypoint.sh" ]
