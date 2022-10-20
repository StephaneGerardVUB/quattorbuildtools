#!/bin/bash


gpg-agent --daemon
gpg --yes --sign releaser.sh
git config --global user.email "stephane.gerard@vub.be"
git config --global user.name "Stephane GERARD"

