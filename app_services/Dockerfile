FROM python:3

RUN pip3 install --upgrade pip

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Default port for Flask applications
EXPOSE 5000

CMD ["python", "/usr/src/app/app.py"]
