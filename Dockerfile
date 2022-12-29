FROM python:3.8-slim

WORKDIR /xlm_staking

COPY . /xlm_staking

RUN apt-get -y update --fix-missing
RUN apt-get -y install apt-utils
RUN apt-get -y dist-upgrade
RUN apt-get -y install gcc make

RUN apt-get -y clean

RUN pip3 install -r requirements.txt

CMD ["make", "run"]
