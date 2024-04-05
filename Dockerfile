FROM python:3.10

WORKDIR /code
COPY . /code

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install necessary packages and Chrome
RUN apt-get -q update && apt-get install wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

CMD ["behave"]