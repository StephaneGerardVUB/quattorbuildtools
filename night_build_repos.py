#!/usr/bin/env python

import json
import subprocess
import argparse
from time import time

# This script works together with a json file that contains a dictionary
# where each key is the name of the Quattor repositories, and the corresponding
# value is again a dict that specifies the branch and the PRs to be applied during
# the maven-build process. The key 'toversion' gives the version string of the
# the release you want to build.

# data to initialize the json file if it does not exist yet
repolist = ['aii', 'CAF', 'CCM', 'cdp-listend', 'configuration-modules-core',
            'configuration-modules-grid', 'LC', 'ncm-cdispd', 'ncm-ncd',
            'ncm-query', 'ncm-lib-blockdevices']
branch_def = 'master'
prs_def = []
toversion_def = '22.10.0-rc2'
data = {}
for repo in repolist:
    data[repo] = {}
    data[repo]['branch'] = branch_def
    data[repo]['prs'] = prs_def
    data[repo]['toversion'] = toversion_def

# generate a timestamp
ts = str(int(time()))

# create the empty logfile for output of build processes
logfilename = 'build_' + ts + '.log'
with open(logfilename, 'w'): pass

# process arguments
parser = argparse.ArgumentParser()
parser.add_argument('--init', action='store_true')
args = parser.parse_args()

# initialize if asked to
if args.init:
    with open('tobuild.json', 'w') as f:
        json.dump(data, f)
    exit()

# load json into a dict
repos = {}
try:
    f = open('tobuild.json', 'r')
except IOError:
    print('Cannot open tobuild.json. Use this command with --init flag to create this file.')
    exit(1)
else:
    repos = json.load(f)

# update of the lists of PRs
for repo in repos.keys():
    prs_str = ''
    prs = repos[repo]['prs']
    for pr in prs:
        prs_str = prs_str + str(pr) + ' '
    with open(repo, 'w') as f:
        prs_str = prs_str[:-1]
        f.write(prs_str)

# build the repos
with open(logfilename, 'a') as f:
    for repo in repos.keys():
        f.write("\n" + repo + "\n\n")
        cmd = "./builder.sh " + repo + " " + repos[repo]['branch'] + " " + repos[repo]['toversion']
        result = subprocess.Popen(cmd, shell=True)
        opt = result.communicate()[0]
        if opt:
            f.write(opt + "\n\n")
        exitcode = result.returncode
        if exitcode == 0:
            f.write('DONE')
        else:
            f.write('FAILED')
