# FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04


# # This prevents Python from writing out pyc files
# ENV PYTHONDONTWRITEBYTECODE 1

# # install system dependencies
# RUN apt-get update \
#     #&& apt-get install -y build-essential \
#     && apt-get install -y python3-pip \
#     && apt install -y ffmpeg

# # install git
# RUN apt-get install -y git 

# # install dependencies
# RUN pip3 install --upgrade pip setuptools


# # set work directory
# WORKDIR /home/aic_team082/

# # copy project
# COPY . .

# # install project requirements
# RUN pip3 install -r requirements.txt

# RUN git clone https://github.com/facebookresearch/detectron2.git && \
#     python3 -m pip install -e detectron2

# # Run app.py when the container launches
# #CMD ["./run.sh"]

#FROM nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04 
FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04 

# RUN apt-get update && apt-get install -y \
#     curl \
#     ca-certificates \
#     sudo \
#     git \
#     bzip2 \
#     libx11-6 \
#     && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y ffmpeg

#RUN #apt-get install -y --fix-missing \
    #build-essential \
    #cmake \
    #gfortran \
RUN apt-get install -y git \
    # wget \
    # curl \
    #graphicsmagick \
    #libgraphicsmagick1-dev \
    #libatlas-base-dev \
    #libavcodec-dev \
    #libavformat-dev \
    #libgtk2.0-dev \
    #libjpeg-dev \
    #liblapack-dev \
    #libswscale-dev \
    #pkg-config \
    #python3-dev \
    # python3-numpy \
    software-properties-common \
    # zip \
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
    # && pip3 install --upgrade pip setuptools \
    && pip3 install -r requirements.txt

WORKDIR /home/aic_team082

RUN git clone https://github.com/facebookresearch/detectron2.git && \
    python3 -m pip install -e detectron2

#ENV FORCE_CUDA="1"
# This will by default build detectron2 for all common cuda architectures and take a lot more time,
# because inside docker build, there is no way to tell which architecture will be used.
#ARG TORCH_CUDA_ARCH_LIST="Kepler;Kepler+Tesla;Maxwell;Maxwell+Tegra;Pascal;Volta;Turing"
#ENV TORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST}"

#RUN ./run.sh