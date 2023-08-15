import socket
import threading
import subprocess
from queue import Queue

# Functions to check if a port is open on a given host
def scan_port(target_host, port):
    try:
        #Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Set a timout to avoid blocking for too long
        client_socket.settimeout(1)
        #Connect to the target host and port
        result = client_socket.connect_ex((target_host, port))
        #If the connections is successful, the port is open
        if result == 0:
            print(f"Port {port} is open on {target_host}")
        #Close the socket
        client_socket.close()
    except Exception as e:
        pass

# Function to check if host reponds to ICMP ping
def ping_host(target_host):
    try:
        subprocess.check_output(['ping', '-c', '1', target_host], stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
# Function to use threading to scan ports onmultiple hosts
def scan_network(target_prefix, ports, num_threads=10):
    target_queue = Queue()
    for host in range(1, 255):
        target_host = f"{target_prefix}.{host}"
        target_queue.put(target_host)

    def worker():
        while not target_queue.empty():
            target_host = target_queue.get()
            if ping_host(target_host):
                for port in ports:
                    scan_port(target_host, port)
            else:
                print(f"Host {target_host} is silent (does not resond to ping).")
            target_queue.task_done()

    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        thread.daemon = True
        thread.start()
    
    target_queue.join()

if __name__ == '__main__':
    # Enter the IP prefix you want to scan eg. '192.168.1.1'
    target_prefix = input('Enter the IP prefix you want to scan (eg. "192.168.1.1"): ')
    # Enter list of ports to scan
    ports = [80, 443, 22, 21, 3389, 8080] # Add more ports if needed

    print(f'Scanning {len(ports)} ports on the network {target_prefix}.x...')
    scan_network(target_prefix, ports)