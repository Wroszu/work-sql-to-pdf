FROM python:3.10-alpine3.18

COPY main.py /app/
COPY sql_files /app/
COPY see-more-sprite.png /app/

WORKDIR /app

CMD ["python", "main.py"]