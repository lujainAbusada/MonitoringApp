FROM python:3.6.8 

# Copy the requirements file to the image.  This file contains the names of all needed packages for the program to run 
COPY ./requirements.txt /app/requirements.txt

# Switch working directory
WORKDIR /app

# Install the dependencies and packages from  the requirements file
RUN pip install -r requirements.txt 

# Copy files from the local file to the image
COPY ./ /app

# Run Flask/python program
ENTRYPOINT [ "python3" ]

CMD ["FlaskApp.py" ]
