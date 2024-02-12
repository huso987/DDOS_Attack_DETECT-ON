from mininet.net import Mininet
from mininet.topo import LinearTopo
from mininet.cli import CLI

Linear4 = LinearTopo(k=4)
net = Mininet(topo=Linear4)
net.start()

# Mininet CLI'yi başlatma
CLI(net)
net.stop()