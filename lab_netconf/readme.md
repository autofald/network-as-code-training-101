# Lab NETCONF


## Pré-requis :

* Installer Docker engine :

    [Documentation d'installation de Docker](https://docs.docker.com/engine/install/ubuntu/)

    Testé avec Docker version 25.0.3

* Installer containerlab



* Récupérer l'image SR-LINUX :

        docker pull ghcr.io/nokia/srlinux:23.10.2

## 1) Lancement et accès à l'infrastructure

Lancement des containeurs

    containerlab deploy

Connexion en CLI aux OS sr-linux :

    ssh admin@clab-lab_netconf-sw1
    ssh admin@clab-lab_netconf-sw2

## 2) Découverte du protocole NETCONF

### 2.2) Afficher la configuration du protocole NETCONF sur sw1

### 2.2) Ouvrir une session NETCONF avec sw1 avec ssh

    ssh -s admin@clab-lab_netconf-sw1 -p 830 netconf