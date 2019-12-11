from sys import argv

if __name__=="__main__":
    n_instances = int(argv[1])
    print("""
version: '3'
services:
  dns-a: 
    image: cytopia/bind:latest
    networks:
      app_net:
        ipv4_address: 172.16.238.10
    volumes: 
      - ./docker-entrypoint.sh:/docker-entrypoint.sh
    environment: 
      - DNS_FORWARDER=127.0.0.11 # Forward to docker's own DNS server
      - ALLOW_RECURSION=any
  dns-b: 
    image: cytopia/bind:latest
    networks:
      app_net:
        ipv4_address: 172.16.238.11
    volumes: 
      - ./docker-entrypoint.sh:/docker-entrypoint.sh
    environment: 
      - DNS_FORWARDER=127.0.0.11 # Forward to docker's own DNS server
      - ALLOW_RECURSION=any
  dns-c: 
    image: cytopia/bind:latest
    networks:
      app_net:
        ipv4_address: 172.16.238.12
    volumes: 
      - ./docker-entrypoint.sh:/docker-entrypoint.sh
    environment: 
      - DNS_FORWARDER=127.0.0.11 # Forward to docker's own DNS server
      - ALLOW_RECURSION=any
""")
    for i in range(n_instances):
        print("""
  app-{i}:
    image: app
    environment: 
      - N_INSTANCES={n_instances}
    networks:
      - app_net
    volumes: 
     - ./resolv.conf:/etc/resolv.conf
""".format(i=i, n_instances=n_instances))
    print("""
networks:
  app_net:
    driver: bridge
    ipam:
      driver: default
      config:
      - subnet: 172.16.238.0/20
""")

  
