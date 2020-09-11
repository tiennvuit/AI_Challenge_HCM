# Base image
FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04 

RUN apt-get update && \
    apt-get install -y ffmpeg

RUN apt-get install -y git \
    software-properties-common \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt update && \
    apt install python3.6 -y && \
    apt install python3-distutils -y && \
    apt install python3.6-dev -y && \
    apt install build-essential -y && \
    apt-get install python3-pip -y && \
    apt update && apt install -y libsm6 libxext6 && \
    apt-get install -y libxrender-dev

COPY . /home/aic_team082/

RUN cd /home/aic_team082 \
    && pip3 install -r requirements.txt

WORKDIR /home/aic_team082

RUN git clone https://github.com/facebookresearch/detectron2.git && \
    python3 -m pip install -e detectron2