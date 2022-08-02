FROM achlys-ubuntu

RUN cd /opt &&
    git clone https://github.com/digiLab-ai/achlys-uq.git

RUN pip3 install pandas
    
RUN cd /opt/achlys-uq/achlys-uq &&
    cat bashrc >> /root/.bashrc
