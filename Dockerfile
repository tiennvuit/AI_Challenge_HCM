FROM python:3.7


# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1


# install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt install -y ffmpeg

# install dependencies
RUN pip install --upgrade pip

RUN chmod 744 -R .


# set work directory
WORKDIR /home

# copy project
COPY . .

# install project requirements
RUN pip install -r requirements.txt


# Run app.py when the container launches
CMD ["script.sh"]