FROM python:3.9.6

WORKDIR /app

ENV FLASK_APP=server.py

RUN apt-get update

RUN pip install python-dotenv

COPY src/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3030

CMD ["python", "src/server.py" ,"run" ,"--host=0.0.0.0"]
