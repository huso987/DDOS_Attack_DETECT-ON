from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class DualSwitchTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Hosts connected to s1
        for i in range(1, 6):
            h = self.addHost('h%s' % i)
            self.addLink(h, s1)

        # Hosts connected to s2
        for i in range(6, 11):
            h = self.addHost('h%s' % i)
            self.addLink(h, s2)

        # Connect switches
        self.addLink(s1, s2)

topo = DualSwitchTopo()
net = Mininet(topo=topo, controller=None)

# Add Floodlight controller
net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

net.start()
CLI(net)
net.stop()
