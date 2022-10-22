FROM debian
RUN apt update
RUN apt install python3 python3-pip -y

RUN pip3 install django

RUN django-admin startproject main


ENTRYPOINT [ "python3","/main/manage.py" ]
