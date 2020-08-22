FROM python:3-alpine
COPY . /api_gateway
RUN pip install -r /api_gateway/requirements.txt
CMD python /api_gateway/gateway.py
