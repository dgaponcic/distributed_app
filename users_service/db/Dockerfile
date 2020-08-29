# FROM python:3-alpine
FROM python@sha256:696cb177491ab1c3cb01891d54948771b7d20fddbd7b8a20f7c6ce9bc2f2bce6

COPY . /db
RUN pip install -r /db/requirements.txt
CMD python /db/db.py
