FROM python:3.9.6
WORKDIR /app
ENV FLASK_ENV=development
ENV FLASK_APP=index.py
RUN apt-get update
COPY src/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "src/index.py"]