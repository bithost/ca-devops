FROM python:3

WORKDIR /usr/src/app

COPY source/hello.py ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./hello.py" ]