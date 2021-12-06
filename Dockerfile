# Pull image Python 3.6 since app was developed using python 3.6
FROM python:3.6


# Install OS Modules
RUN apt update -y && \
    apt install telnet -y && \
    rm -rf /var/lib/apt/lists/*


# Copy source code to container
RUN mkdir -p /data-copier #creeating folder in docker custom image to hold app files
COPY app /data-copier/app/
COPY condarequirements.txt /data-copier/
COPY piprequirements.txt /data-copier/

# Mount data source to container
RUN pip install -r /data-copier/piprequirements.txt