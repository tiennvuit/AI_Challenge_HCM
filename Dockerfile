FROM ubuntu:18.04


# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y python3-pip \
    && apt install -y ffmpeg

# install dependencies
RUN pip3 install --upgrade pip


# set work directory
WORKDIR /home/aic_team082/

# copy project
COPY . .

# install project requirements
RUN pip3 install -r requirements.txt \
    && pip3 install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.6/index.html


# Run app.py when the container launches
CMD ["./run.sh"]