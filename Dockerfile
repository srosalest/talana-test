FROM python:3
WORKDIR /talana
COPY code/ /talana/code
COPY requirements.txt /talana/

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get upgrade -y \
    && pip install --root-user-action=ignore --upgrade pip \
    && pip install --root-user-action=ignore -r requirements.txt

CMD [ "sleep", "inf" ]