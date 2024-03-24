# Lab NETCONF


## Pré-requis :

* Installer Docker engine :

    [Documentation d'installation de Docker](https://docs.docker.com/engine/install/ubuntu/)

    Testé avec Docker version 25.0.3

* Installer containerlab

        [Documentation d'installation de Containerlab](https://containerlab.dev/install/#__tabbed_1_1)

* Récupérer l'image SR-LINUX :

        docker pull ghcr.io/nokia/srlinux:23.10.2

* Ajouter l'image cEOS :

        docker import cEOS64-lab-4.30.5M.tar.xz ceos:4.30.5M

* Récupérer l'image gNMIc :

        docker pull ghcr.io/openconfig/gnmic:0.36.2

## 1) Lancement et accès à l'infrastructure

Lancement des containeurs

    containerlab deploy

Connexion SSH aux switchs:

    ssh admin@clab-lab_netconf-sw1

Lancement de la CLI gNMIc

    docker run --network host --rm ghcr.io/openconfig/gnmic -a clab-lab_netconf-sw1:6030 --insecure -u admin -p admin capabilities

## 2) Découverte du protocole gNMI

### 2.1) Configuration du protocole gNMI sur sw1
