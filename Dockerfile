FROM ubuntu:18.04


# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update \
    #&& apt-get install -y build-essential \
    && apt-get install -y python3-pip \
    && apt install -y ffmpeg

# install git
RUN apt-get install -y git 

# install dependencies
RUN pip3 install --upgrade pip setuptools


# set work directory
WORKDIR /home/aic_team082/

# copy project
COPY . .

# install project requirements
RUN pip3 install -r requirements.txt

RUN git clone https://github.com/facebookresearch/detectron2.git && \
    python3 -m pip install -e detectron2

# Run app.py when the container launches
#CMD ["./run.sh"]