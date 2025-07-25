FROM python:3.10
WORKDIR /project
COPY . /project
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

