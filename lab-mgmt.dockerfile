# pull base image
FROM alpine:3.18

ARG ANSIBLE_CORE_VERSION=2.16.4
ARG ANSIBLE_VERSION=9.3.0
ARG ANSIBLE_LINT
ENV ANSIBLE_CORE_VERSION ${ANSIBLE_CORE_VERSION}
ENV ANSIBLE_VERSION ${ANSIBLE_VERSION}

RUN apk --no-cache add \
        sudo \
        python3\
        py3-pip \
        openssl \
        ca-certificates \
        sshpass \
        openssh-client \
        rsync \
        git && \
    apk --no-cache add --virtual build-dependencies \
        python3-dev \
        libffi-dev \
        musl-dev \
        gcc \
        build-base && \
    pip3 install --upgrade pip wheel && \
    pip3 install --upgrade cryptography cffi && \
    pip3 install ansible-core==${ANSIBLE_CORE_VERSION} && \
    pip3 install ansible==${ANSIBLE_VERSION} && \
    pip3 install jxmlease paramiko ncclient jmespath && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* && \
    rm -rf /root/.cache/pip

RUN mkdir /workdir && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

WORKDIR /workdir

CMD [ "ansible-playbook", "--version" ]