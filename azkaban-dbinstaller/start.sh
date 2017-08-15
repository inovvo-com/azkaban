docker run --rm --name azkaban-dbinstaller -i -t -v /datadock/app/azkaban/conf/:/azkaban/conf -e MYSQL_ROOT_PASSWORD=my-secret-pw inovvo/azkaban-dbinstaller:3.32.1
