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

* Créer l'image de management des eqts :

        docker build -t lab-mgmt:latest . -f ../lab-mgmt.dockerfile

## 1) Lancement et accès à l'infrastructure

Lancement des containeurs

    containerlab deploy

Connexion SSH aux switchs:

    ssh admin@clab-lab_netconf-sw1

Lancement de playbooks

    docker exec clab-lab_netconf-lab-mgmt ansible-playbook get-version.yml

Lancement d'un script python

    docker exec clab-lab_netconf-lab-mgmt python ncclient_exemple.py

## 2) Découverte du protocole NETCONF

### 2.1) Configuration du protocole NETCONF sur sw1

:question: Affichez la configuration Netconf de sw1 en CLI

:question: Vérifier que l'interface de management NETCONF est bien opérationnelle

### 2.2) Ouverture d'une session NETCONF avec sw1 avec ssh

    ssh -s admin@clab-lab_netconf-sw1 -p 830 netconf

:question: Expliquez les paramètres utilisés (cf RFC 6242)

:question: quelle est le premier message reçu suite à l'établissement de la session NETCONF et à quoi sert-il ?

Un premier message est nécessaire d'envoyer à partir du client :

    <hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <capabilities>
        <capability>
        urn:ietf:params:netconf:base:1.0
        </capability>
    </capabilities>
    </hello>
    ]]>]]>

:question: A quoi sert ce message ?

### 2.3) Récupération de données

Voici un premier exemple de requête :

    <rpc message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <get-config>
        <source><running/></source>
    </get-config>
    </rpc>
    ]]>]]>

:question: Que permet de récupérer ce message ?

Les modèles YANG utilisables sur EOS sont disponibles ici : [YANG models](https://github.com/aristanetworks/yang/tree/master/EOS-4.30.2F/release/openconfig/models)

La RFC qui décrit les opérations et paramètres en NETCONF est ici : [RFC 6241](https://datatracker.ietf.org/doc/html/rfc6241)

Un outil utile pour explorer les modèles YANG openConfig : [OpenConfig schema path](https://openconfig.net/projects/models/paths/)

:question: Quelle est la requête pour récupérer la liste des utilisateurs ?

:question: Quelle est la requête pour récupérer la configuration de l'interface ethernet1 ?

:question: Quelle est la requête pour récupérer l'état opérationnel de l'interface ethernet1 ?

:question: Quelle est la requête pour récupérer l'état opérationnel de la session BGP 192.168.1.1 dans la GRT ?

### 2.4) Modification de configuration

:question: Quelle sont les requêtes nécessaire pour :

  * vérrouiller le datastore de configuration "candidate"
  * modifier la description de l'interface "Ethernet1"
  * récupérer la description de l'interface "Ethernet1" dans le datastore candidate
  * commit la modification
  * déverouiller le datastore de configuration "candidate"
  * récupérer la description de l'interface "Ethernet1" dans le datastore running

### 2.5) Utilisation de python

On utilise en générale l'accès netconf via un shell que pour du debug. L'interet de NETCONF est surtout pour des scripts ou outils d'automatisation.

:question: écrire en python un petit script qui va effectuer les actions suivantes :

1. récupérer la liste des interfaces avec leur statut et description
2. configuer une nouvelle interface "Ethernet2"
3. récupérer la liste des interfaces avec leur statut et description

La bibliothèque la plus utilisé en python pour faire du netconf est ncclient : [documentation](https://ncclient.readthedocs.io/en/latest/)



### 2.5) Utilisation d'ansible

:question: En utilisant les modules ansible.netcommon.netconf_*, 