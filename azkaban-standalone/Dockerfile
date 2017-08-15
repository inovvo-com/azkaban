FROM inovvo/azkaban-base:3.32.1

WORKDIR /app/azkaban/azkaban-solo-server/build/install/azkaban-solo-server
RUN chmod +x bin/*.sh

EXPOSE 8443 8081 5005
CMD bin/azkaban-solo-start.sh && tail --pid=`cat currentpid` -f /dev/null

