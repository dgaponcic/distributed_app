FROM python:3-alpine
COPY . /proxy
RUN pip install -r /proxy/requirements.txt
CMD python /proxy/proxy.py
