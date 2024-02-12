from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo
from mininet.cli import CLI

Single3 = SingleSwitchTopo(k=3)
net = Mininet(topo=Single3)
net.start()

# Mininet CLI'yi başlatma
CLI(net)
net.stop()