#!/usr/bin/env python

import json
import subprocess
import argparse

# data to initialize the json file if it does not exist yet
data = {
        "aii": {
            "branch": "master",
            "prs": [335,328],
            "status": "",
            "toversion": "22.10.0-rc2"
        },
        "CAF": {
            "branch": "master",
            "prs": [],
            "status": "",
            "toversion": "22.10.0-rc2"
        },
        "CCM": {
            "branch": "master",
            "prs": [],
            "status": "",
            "toversion": "22.10.0-rc2"
        },
        "cdp-listend": {
            "branch": "master",
            "prs": [],
            "status": "",
            "toversion": "22.10.0-rc2"
        },
        "configuration-modules-core": {
            "branch": "master",
            "prs": [],
            "status": "",
            "toversion": "22.10.0-rc2"
        },
        "configuration-modules-grid": {
            "branch": "master",
            "prs": [],
            "status": "",
            "toversion": "22.10.0-rc2"
        },
        "LC": {
            "branch": "master",
            "prs": [],
            "status": "",
            "toversion": "22.10.0-rc2"
        },
        "ncm-cdispd": {
            "branch": "master",
            "prs": [],
            "status": "",
            "toversion": "22.10.0-rc2"
        },
        "ncm-ncd": {
            "branch": "master",
            "prs": [],
            "status": "",
            "toversion": "22.10.0-rc2"
        },
        "ncm-query": {
            "branch": "master",
            "prs": [],
            "status": "",
            "toversion": "22.10.0-rc2"
        },
        "ncm-lib-blockdevices": {
            "branch": "master",
            "prs": [],
            "status": "",
            "toversion": "22.10.0-rc2"
        }

}

# process arguments
parser = argparse.ArgumentParser()
parser.add_argument('--init', action='store_true')
parser.add_argument('--status', action='store_true')
args = parser.parse_args()

# initialize if asked to
if args.init:
    with open('tobuild.json', 'w') as f:
        json.dump(data, f)
    exit()

# display the status if asked to
if args.status:
    with open('tobuild.json', 'r') as f:
        status = json.load(f)
        for k,v in status.items():
            print(k)
            for kk,vv in v.items():
                linestat = "    " + kk + ":" + str(vv)
                print(linestat)
    exit()

# load json into a dict
repos = {}
with open('tobuild.json', 'r') as f:
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

# build the repos and update the statuses
for repo in repos.keys():
    if repos[repo]['status'] == 'done':
        continue
    cmd = "./builder.sh " + repo + " " + repos[repo]['branch'] + " " + repos[repo]['toversion']
    result = subprocess.Popen(cmd, shell=True)
    opt = result.communicate()[0]
    exitcode = result.returncode
    if exitcode == 0:
        repos[repo]['status'] = 'done'
    else:
        repos[repo]['status'] = 'failed'
with open('tobuild.json', 'w') as f:
    json.dump(repos, f)



