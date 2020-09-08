FROM microsoft/mssql-server-windows-developer
COPY sc .
ENV ACCEPT_EULA Y
ENV sa_password @Toyotainnova5
RUN sqlcmd -i one.sql
RUN sqlcmd -i two.sql
RUN sqlcmd -i three.sql


 