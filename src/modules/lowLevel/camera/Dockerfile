FROM jjanzic/docker-python3-opencv:latest

WORKDIR /user/app

COPY . .

# RUN pip3 install --upgrade pip setuptools wheel

ENV READTHEDOCS True

RUN pip install picamera
RUN pip3 install -r requirements.txt

VOLUME ["/data"]

CMD ["python3", "camera.py"]
