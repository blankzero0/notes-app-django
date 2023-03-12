FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN ./manage.py migrate

EXPOSE 8000
CMD [ "./manage.py", "runserver", "0.0.0.0:8000" ]
