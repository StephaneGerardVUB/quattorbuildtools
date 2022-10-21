# Quattor Build Tools

To build the container image:

```podman build -t quattorbuild -f Dockerfile .```

Create a directory that will be shared between the host and the container. In this directory, do a ```git clone of this project.

To launch the container:

```podman run -it --user=<youruserid>:<yourgroupid> --userns=keep-id -v <shared_directory>:/home:z localhost/quattorbuild```


Inside the container:

* create a gpg key: ```gpg --gen-key```
* launch the gpg-agent in background: ```gpg-agent --daemon```
* run the releaser script: ```./releaser.sh 22.10.1 1```
