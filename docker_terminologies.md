Problem: Different environments lead to different behavior.
Solution: This is where docker comes into the picture.
Docker packages everything the application needs into one unit. Therefore, anyone who runs that image gets the same environment.

## Container vs Virtual Machine:

### Virtual Machine: 
- Every VM contains a complete separate operating system.
- It offers a strong isolation however it also results in Slow startup, high memory usage, slower response.

### Docker Container:
- Containers share the host OS kernel, so they are much lighter.
- It also results in less memory usage, startup in seconds and easy to distribute.

### Docker Image
- An image is a blueprint which contains instructions to create a container.
- One image can create many containers.

### Docker Engine
- A docker engine is a software that builds images, starts containers, stops containers, manages networking and storage etc.

