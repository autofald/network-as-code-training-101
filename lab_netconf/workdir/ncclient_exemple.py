from ncclient import manager


INTERFACE_CONFIG='''
<interfaces>
    <interface>
        <name>{intf_name}</name>
    </interface>
</interfaces>
'''

INTERFACES_CONFIG='''
<interfaces>
    <interface>
    </interface>
</interfaces>
'''

NS = {None: 'http://openconfig.net/yang/interfaces'}

# Create a netconf session manager
with manager.connect(
        host="clab-lab_netconf-sw1",
        port="830",
        timeout=30,
        username="admin",
        password="admin",
        hostkey_verify=False
    ) as eos:

    # Get and print one interface description
    intf_config = eos.get_config(source="running", filter=("subtree", INTERFACE_CONFIG.format(intf_name="Ethernet1")))
    intf_name = intf_config.data.find(".//interfaces/interface/config/name", namespaces=NS).text
    intf_description = intf_config.data.find(".//interfaces/interface/config/description", namespaces=NS).text
    print(f"{intf_name} - {intf_description}")

    # Get and print all the interfaces descriptions
    intfs_config = eos.get_config(source="running", filter=("subtree", INTERFACES_CONFIG))
    for intf in intfs_config.data.find(".//interfaces", namespaces=NS):
        name = intf.find(".//config/name", namespaces=NS).text
        description = intf.find(".//config/description", namespaces=NS)
        print(f"{name} - {getattr(description, 'text', 'Empty')}")