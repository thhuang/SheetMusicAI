ARG CUDA="9.0"
ARG CUDNN="7"

FROM nvidia/cuda:${CUDA}-cudnn${CUDNN}-devel-ubuntu16.04

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install basics
RUN apt-get update -y \
    && apt-get install -y apt-utils git curl ca-certificates bzip2 cmake tree htop bmon iotop g++ \
    && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev

# Install Miniconda
RUN curl -so /miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && chmod +x /miniconda.sh \
    && /miniconda.sh -b -p /miniconda \
    && rm /miniconda.sh

ENV PATH=/miniconda/bin:$PATH

# Create a Python 3.6 environment
RUN /miniconda/bin/conda install -y conda-build \
    && /miniconda/bin/conda create -y --name py36 python=3.6.7 \
    && /miniconda/bin/conda clean -ya

ENV CONDA_DEFAULT_ENV=py36
ENV CONDA_PREFIX=/miniconda/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

RUN conda install -y ipython
RUN pip install ninja yacs cython matplotlib opencv-python

# Install PyTorch 1.0 Nightly and OpenCV
RUN conda install -y pytorch-nightly -c pytorch \
    && conda clean -ya

# Install TorchVision master
RUN git clone https://github.com/pytorch/vision.git \
    && cd vision \
    && python setup.py install

# Install pycocotools
RUN git clone https://github.com/cocodataset/cocoapi.git \
    && cd cocoapi/PythonAPI \
    && python setup.py build_ext install

# Install PyTorch Detection
RUN git clone https://github.com/facebookresearch/maskrcnn-benchmark.git \
    && cd maskrcnn-benchmark \
    && python setup.py build develop

# Networking
RUN apt-get update && apt-get install -y \
    openssh-server \
    iputils-ping \
    net-tools

RUN mkdir /var/run/sshd
RUN echo 'root:12345678' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
CMD ["/usr/sbin/sshd", "-D"]

# Setup Workspace
WORKDIR /app

