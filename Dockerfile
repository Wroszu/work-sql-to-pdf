FROM python:3.10-alpine3.18

RUN apk add --no-cache build-base libffi-dev jpeg-dev zlib-dev

RUN pip install pandas==2.1.1
RUN pip install numpy==1.26.0
RUN pip install reportlab==3.6.8

COPY main.py /app/
COPY sql_files /app/
COPY sql_files/sqlite-sakila.db /app/sql_files/ 
COPY see-more-sprite.png /app/

WORKDIR /app

CMD ["python", "main.py"]