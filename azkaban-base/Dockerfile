FROM java:8

RUN apt-get update -yqq \
    && apt-get install -yqq \
    git 

WORKDIR /app/

RUN git clone https://github.com/azkaban/azkaban.git
WORKDIR /app/azkaban
RUN git checkout 3.32.1
RUN bash gradlew build installDist -x test
