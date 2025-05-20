FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    curl \
    ca-certificates \
    libssl-dev \
    libffi-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    xz-utils \
    tk-dev \
    libncursesw5-dev \
    libgdbm-dev \
    libnss3-dev \
    liblzma-dev \
    make \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python 3.13 from source
ENV PYTHON_VERSION=3.13.0
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar -xzf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    cd .. && rm -rf Python-${PYTHON_VERSION}*

# Install Miniconda
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH
RUN curl -sSLO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_DIR && \
    rm Miniconda3-latest-Linux-x86_64.sh

# Set environment shell
SHELL ["bash", "-c"]

# Copy environment file and app source
WORKDIR /app
COPY . /app

# Create conda environment from the YAML file
RUN conda env create -f python_3_13_environment.yml && \
    conda clean -afy

# Activate env for all future commands
ENV PATH=$CONDA_DIR/envs/pyenv/bin:$PATH

# Default command to run tests
CMD ["conda", "run", "--name", "py313", "pytest"]