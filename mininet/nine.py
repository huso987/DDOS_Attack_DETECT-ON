from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class SingleSwitchTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        #sunucu ve istemci
        for i in range(1, 10):
            h1 = self.addHost('h%s' % i)
            self.addLink(h1, s1)
        

        # Optionally connect server/client (h10) to s2
        h11 = self.addHost('h11')
        self.addLink(h11, s2)
topo = SingleSwitchTopo()
net = Mininet(topo=topo)


net.start()
CLI(net)
net.stop()