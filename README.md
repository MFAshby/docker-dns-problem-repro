Reproduction for a potential problem with large docker-compose files
You need python3, docker, and docker-compose installed locally

Run `./test.sh N` where N is the number of services to be defined 
in the docker-compose file.

Expect to see this work up to a particular number, then services 
might start to encounter DNS lookup errors trying to talk to each 
other (each service makes an http call to every other service)
