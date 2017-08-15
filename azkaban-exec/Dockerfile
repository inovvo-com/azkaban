FROM inovvo/azkaban-base:3.32.1

WORKDIR /app/azkaban/azkaban-exec-server/build/install/azkaban-exec-server 
RUN ln -s /azkaban/conf conf
RUN mkdir plugins && mkdir plugins/jobtypes && echo 'execute.as.user=false' > plugins/jobtypes/commonprivate.properties
RUN chmod +x bin/*.sh

EXPOSE 12321
CMD bin/azkaban-executor-start.sh && tail --pid=`cat currentpid` -f /dev/null
