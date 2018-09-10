FROM python:stretch
RUN pip install scipy
RUN pip install ikpy
RUN pip install redis

COPY . /kinematics
ENTRYPOINT [ "/kinematics/main.py" ]