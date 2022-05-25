# SENDER

import socket

group = '224.1.1.1'
port = 5003

# 2-hop restriction in network
ttl = 2

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_MULTICAST_TTL,
                ttl)
mensagem = (input('Digite uma mensagem: '))
sock.sendto(mensagem.encode(), (group, port))

