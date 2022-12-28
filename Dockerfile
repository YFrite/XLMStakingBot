FROM python:3.7-slim

WORKDIR /xlm_staking

COPY . /xlm_staking

RUN pip3 install -r requirements.txt

CMD ["make", "run"]
