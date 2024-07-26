FROM tomcat:9.0-jdk11-openjdk
COPY server.xml /usr/local/tomcat/conf/server.xml
ENTRYPOINT ["catalina.sh", "run"]
