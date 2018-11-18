FROM python:3.6


COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000


