FROM python:3.7

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1


# install system dependencies
RUN apt-get update \
    && apt-get install build-essential \
    && apt install ffmpeg

# install dependencies
RUN pip install --upgrade pip


# set work directory
WORKDIR /home

# copy project
COPY . .

# install project requirements
RUN pip install -r requirements.txt


# Run app.py when the container launches
CMD [ "python","script.py","--data","data"] 