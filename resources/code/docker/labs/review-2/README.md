### Problem

---

how do you produce a Docker image without a Dockerfile?

You’re going to start with an image on Docker Hub: diamol/ch03-lab. That image has a file at the path /diamol/ch03.txt. You need to update that text file and add your name at the end. Then produce your own image with your changed file. You’re not allowed to use a Dockerfile.

### One Solution

---
**STEP 1: Run the image in interactive mode**

docker container run -it --name ch03-lab diamol/ch03-lab

**STEP 2: update ch03.txt**

echo Pascal >> ch03.txt

**STEP 3: Create the image from diamol/ch03-lab**

docker container commit ch03-lab ch03-lab-pas

**STEP 4: Connect to the new image in interactive mode**

docker container run -it --name ch03-lab-pas ch03-lab-pas
