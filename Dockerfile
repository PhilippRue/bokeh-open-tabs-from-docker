FROM python:3.7

# Install discover section
ENV PYTHONPATH /app

# set workdir in container
WORKDIR /app

# copy files and directories
COPY test-app ./test-app

# install dependencies
RUN pip3 install -e test-app

# finally copy serve-app script 
COPY ./serve-app.sh /opt/

# start bokeh server
EXPOSE 5007
CMD ["/opt/serve-app.sh"]
