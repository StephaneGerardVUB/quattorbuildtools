# Quattor Build Tools

To build the container image:

```podman build -t quattorbuild -f Dockerfile .```

To launch the container:

```podman run -it --user=<youruserid>:<yourgroupid> --userns=keep-id -v <a_directory_on_the_host>:/home:z localhost/quattorbuild```


Inside the container:

* create a gpg key
* launch the gpg-agent in background: ```gpg-agent --daemon```
