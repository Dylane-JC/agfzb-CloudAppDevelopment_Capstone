FROM python:3.9

#ENV PYTHONBUFFERED 1
#ENV PYTHONWRITEBYTECODE 1
ENV APP=/dealership

# Install the requirements
COPY requirements.txt $APP

#install and update python
RUN pip install --upgrade pip
RUN apt-get update \
        && apt-get install -y netcat
RUN pip install gunicorn==20.0.4 
RUN pip install Pillow==8.0.1
RUN pip install requests-2.27.1
RUN pip install Django==4.0.3


# Change the workdir.
WORKDIR server


# Copy the rest of the files
COPY . dealership

EXPOSE 8000

RUN chmod +x /
ENTRYPOINT ["entrypoint.sh"]

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangobackend.wsgi"]