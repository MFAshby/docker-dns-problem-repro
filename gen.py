from sys import argv

if __name__=="__main__":
    n_instances = int(argv[1])
    print("""
version: '3'
networks:
  app_net:
    driver: macvlan
services:
""")
    for i in range(n_instances):
        print("""
  app-{i}:
    image: app
    networks: 
     - app_net
    environment: 
      - N_INSTANCES={n_instances}
""".format(i=i, n_instances=n_instances))

  
