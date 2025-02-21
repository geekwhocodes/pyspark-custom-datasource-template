FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
  && apt-get -y install --no-install-recommends \
  openjdk-17-jre \
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64


# Set the working directory
WORKDIR /workspace

# Copy the scripts folder into the container
COPY scripts /workspace/scripts

COPY requirements.txt /workspace/requirements.txt


RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r /workspace/requirements.txt

# Ensure the scripts have execution permissions
RUN chmod +x /workspace/scripts/init-env.sh

# # Ensure the virtual environment is created
# RUN python -m venv /workspace/.venv

# # Ensure the activate script runs for bash shells
# RUN echo "source /workspace/.venv/bin/activate" >> ~/.bashrc





