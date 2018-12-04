FROM alpine:3.8

RUN apk --no-cache add \
        chromium \
        chromium-chromedriver \
        python3

COPY requirements.txt /
RUN pip3 install --no-cache-dir  -r requirements.txt

COPY test.py /

CMD ["python3", "test.py"]
