FROM inovvo/azkaban-base:3.32.1

WORKDIR /app/azkaban/azkaban-web-server/build/install/azkaban-web-server
RUN ln -s /azkaban/conf conf
RUN chmod +x bin/*.sh

EXPOSE 8443 8081
CMD bin/azkaban-web-start.sh && tail --pid=`cat currentpid` -f /dev/null
