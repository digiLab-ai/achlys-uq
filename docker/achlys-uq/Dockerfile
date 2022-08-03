FROM achlys-ubuntu

RUN cd /opt && \
    git clone https://github.com/digiLab-ai/achlys-uq.git
    
RUN cd /opt/achlys-uq/scripts && \
    cat bashrc >> /root/.bashrc

RUN apt-get update && \
    apt-get install -y inotify-tools
