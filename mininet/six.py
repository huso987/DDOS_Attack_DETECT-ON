from mininet.net import Mininet
from mininet.node import Host, Switch
from mininet.cli import CLI
from mininet.node import RemoteController
# Mininet'in topoloji oluşturma fonksiyonlarını içeren kütüphane
from mininet.topo import Topo

# IP adresleme ve ağ ayarları için kütüphane
from mininet.link import TCLink

class MyTopo(Topo):

    # Topolojinin yapısını tanımlayan fonksiyon
    def build(self):

        # Ana anahtar (switch) oluşturma
        s1 = self.addSwitch('s1')

        # İki adet sunucu (host) oluşturma
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Anahtar ve sunucuları bağlantıları
        self.addLink(h1, s1)
        self.addLink(h2, s1)

# Oluşturulan topolojiyi kullanmak için bir nesne oluşturma
topo = MyTopo()


net = Mininet(topo=topo, link=TCLink, controller=RemoteController, autoSetMacs=True, autoStaticArp=True)

# Ağdaki tüm cihazları başlatma
net.start()


# Mininet CLI'yi başlatma
CLI(net)

# Mininet ağını kapatma
net.stop()
