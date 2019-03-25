FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . .
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
