FROM inovvo/azkaban-base:3.32.1

RUN ln -s /azkaban/conf conf
WORKDIR /app/azkaban
RUN apt-get -yqq install python-pip python-dev libmysqlclient-dev && pip install MySQL-python && pip install jproperties
ADD importdb.py /app/azkaban/importdb.py

CMD python importdb.py
