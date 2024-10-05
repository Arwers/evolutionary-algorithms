FROM python:3-slim
WORKDIR /evolutionary-algorithm
COPY . /evolutionary-algorithm
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./App/index.py