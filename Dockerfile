FROM python:3.9
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/

# pipは最新版にする
RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD python src/main.py
