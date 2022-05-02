FROM python:latest

WORKDIR /user/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "sensors.py"]
