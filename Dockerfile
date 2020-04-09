#reference: https://github.com/masroorhasan/docker-pyspark

FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Install OpenJDK 8
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

# Install PySpark and Numpy
RUN \
    pip install -r requirements.txt

# Define working directory
COPY . /app
WORKDIR /app

# Define default command
CMD ["bash"]