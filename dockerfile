FROM ubuntu:latest

MAINTAINER Jack Owens "owensr@stifel.com"

WORKDIR .

RUN apt-get update -y

RUN apt-get install -y python3-pip python3.7

COPY . .

RUN mkdir -p $HOME/.config/pip/

COPY pip.conf $HOME/.config/pip/

RUN pip3 install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org -r requirements.txt

CMD [ "python3", "main.py" ]
