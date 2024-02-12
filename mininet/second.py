from mininet.net import Mininet
from mininet.cli import CLI

net = Mininet()

#create nodes
c0 = net.addController()
h0 = net.addHost('h0')
s0 = net.addSwitch('s0')
h1 = net.addHost('h1')

#create links between nodes

net.addLink(h0, s0)
net.addLink(h1, s0)

#configuration of ip 

h0.setIP('192.168.1.1', 24)
h1.setIP('192.168.1.2', 24)

net.start()
CLI(net)
net.stop()