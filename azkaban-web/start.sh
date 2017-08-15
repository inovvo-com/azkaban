docker run --rm --name azkaban-web -p 8081:8081 -p 8443:8443  -v /datadock/app/azkaban/conf/:/azkaban/conf -d inovvo/azkaban-web:3.32.1
