FROM python:3.6
COPY . ./code
RUN pip install -r code/requirements.txt
