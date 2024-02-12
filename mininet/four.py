from mininet.net import Mininet
from mininet.topolib import TreeTopo
from mininet.cli import CLI

Tree22 = TreeTopo(depth=2, fanout=2)
net = Mininet(topo=Tree22)

net.start()
CLI(net)
net.pingAll()
net.get('h1').cmd('ping -c 3 ' + net.get('h2').IP())
net.stop()