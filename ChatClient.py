import socket

from signal import signal, SIGPIPE, SIG_DFL


signal(SIGPIPE,SIG_DFL)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Enable Broadcast
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Send broadcast message
    s.sendto(b'DISCOVER', ("255.255.255.255", 3333))

    # Receive response
    data, addr = s.recvfrom(1024)
    print(data, addr)