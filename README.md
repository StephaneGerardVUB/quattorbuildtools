# Quattor Build Tools

To build the container image:

```podman build -t quattorbuild -f Dockerfile .```

Create a directory that will be shared between the host and the container. In this directory, do a ```git clone``` of this project.

To launch the container:

```podman run -it --user=<youruserid>:<yourgroupid> --userns=keep-id -v <shared_directory>:/home:z localhost/quattorbuild```


Inside the container:

* create a gpg key: ```gpg --gen-key```
* launch the gpg-agent in background: ```gpg-agent --daemon```
* run the releaser script: ```./releaser.sh 22.10.1 1```

## Night-builder

The goal of this sub-project is to build the releases in unattended mode, with a cronjob for example. As the gpg plugin will require the passphrase to unlock the private key, it can be fixed by creating the following settings.xml in the $HOME/.m2 directory:
```<settings>
  <profiles>
    <profile>
      <id>gpg</id>
      <properties>
        <gpg.executable>gpg2</gpg.executable>
        <gpg.passphrase>your_passphrase</gpg.passphrase>
      </properties>
    </profile>
  </profiles>
  <activeProfiles>
    <activeProfile>gpg</activeProfile>
  </activeProfiles>
</settings>
```
