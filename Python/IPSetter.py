import wmi


def set_static_ip(ip, gateway, dns_servers, subnet_mask=['255.255.255.0']):
    nic_config = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    nic = nic_config[2]

    nic.EnableStatic(IPAddress=ip, SubnetMask=subnet_mask)
    nic.SetGateways(DefaultIPGateway=gateway)
    nic.SetDNSServerSearchOrder(DNSServerSearchOrder=dns_servers)

    print(nic)


def set_dynamic_ip():
    nic_config = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    nic = nic_config[2]

    nic.EnableDHCP()

if __name__ == '__main__':
    ip = ['10.156.146.155']
    gateway = ['10.156.146.1']
    dns_servers = ['210.111.226.7', '210.111.226.8']

    # set_static_ip(ip, gateway, dns_servers)
    set_dynamic_ip()