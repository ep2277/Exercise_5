import socket
import threading

from signal import signal, SIGPIPE, SIG_DFL

#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)



#https://de.wikipedia.org/wiki/Broadcast
def udpBroadcast(port):  #port = 3333

    signal(SIGPIPE,SIG_DFL)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   as s:
        # Enable broadcast option
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # Sending the broadcast message (Discover bzw. "Discovery-Phase")
        s.sendto(b'DISCOVER', ("255.255.255.255", port))

        # Receive response
        data, address = s.recvfrom(1024)
    #    print(f'Daten: {data}  Addresse: {address}') #in diesem Falle war das die 172.17.0.49:3454
        print(f'Daten: {data}')
        print(f'Addresse: {address}')
        address = data.decode().split(":")
        port = int(address[1])
        ipAddress = address[0].split(" ")[1]
        print(f'IP-Adresse: {ipAddress}')
        print(f'Port: {port}')
        return ipAddress, port

def anmelden(benutzername,ipadresse, port):
    TCP_IP = ipadresse
    TCP_PORT = port
    BUFFER_SIZE = 1024
    DATA = b'CONNECT ' + benutzername.encode()

    # Wir erzeugen einen neuen Stream Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wir stellen eine Verbindung zum Server her
    sock.connect((TCP_IP, TCP_PORT))

    # Wir senden Daten zum Server
    sock.send(DATA)
    print("Gesendete Daten: ", DATA)

    # Wir empfangen Daten vom Server
    buffer = sock.recv(BUFFER_SIZE)
    print("Empfangene Daten: ", buffer)

    # Wir geben alle Ressourcen wieder frei
    sock.close()

def main():
    ipaddress, port = udpBroadcast(3333)
    anmelden('Test\r\n', ipaddress, port)



main()