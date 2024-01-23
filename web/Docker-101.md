# Docker 101

The best reference for understanding how Docker and its commands works is
[Docker Documentation](https://docs.docker.com/engine/reference/builder/).
It will always be up-to-date. Below, we do our best in explaining the
essential commands as briefly as possible.

## Docker Basic Commands:

* Command to get information about docker setup on your machine
  ```shell
  docker info
  ```
* List of docker containers stopped and running can be found using
  ```shell
  docker ps -a
  ```
* List the built docker images
    ```shell
    docker images
    ```
* Remove containers using
  ```shell
  sudo docker rm <Container Name>
  ```
* To run docker container use
  ```shell
  docker run -h CONTAINER1 -i -t debian /bin/bash
  docker run -h CONTAINER2 -i -t ubuntu /bin/bash
  ```
  Here, `-h` is used to specify a container name,
  `-t` to start with tty, and `-i` means interactive.
  They can be combined on one flag listing `-it`.
  Note: second times will be quick because of caching.
* Docker with networking
  ```shell
  docker run -h CONTAINER1 -it --net="bridge" debian /bin/bash
  ```
* When the containers are not running and when you're done,
  kill them using
  ```shell
  docker rm `docker ps --no-trunc -aq`
  ```
* Rename using
  ```shell
  docker rename name_v0 name_v1
  ```
* Start a container using
  ```shell
  docker start <container name>
  ```
* Stop a container using
  ```shell
  docker stop <container name>
  ```

## Creating Images

* Create a Dockerfile. The name is case-sensitive, and it has to be
  `Dockerfile`.

  ```shell
  vim Dockerfile
  ```
* FROM command specifies the base image you are going to use build
  your dockerfile and your new image. It is an existing image,
  like ubuntu, alpine, debian, etc.
  ```dockerfile
  FROM debian
  ```
* CMD command specifies all the commands you need to run
  ```dockerfile
  CMD echo hello world
  ```
* Build the image with folder name ("." in this case)
  ```shell
  docker build .
  ```
* Output
  ```shell
  Sending build context to Docker daemon 2.048kB  
  Step 1/2 : FROM alpine  
  latest: Pulling from library/alpine  
  ff3a5c916c92: Pull complete  
  Digest: sha256:7df6db5aa61ae9480f52f0b3a06a140ab98d427f86d8d5de0bedab9b8df6b1c0  
  Status: Downloaded newer image for alpine:latest  
  ---> 3fd9065eaf02  
  Step 2/2 : CMD ["echo hello world"]  
  ---> Running in 48cd3d25065d  
  Removing intermediate container 48cd3d25065d  
  ---> e2e741ea5f6f  
  Successfully built e2e741ea5f6f  
  ```
* Run the image using the image ID ("e2e741ea5f6f" in this case)
  and a test name of your choice
  ```shell
  docker run --name <test name> e2e741ea5f6f
  ```
* List images using
  ```shell
  sudo docker images
  ```
* Remove images using
  ```shell
  docker rmi <Image ID>
  ```