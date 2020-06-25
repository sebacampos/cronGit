# cronGit
Python script to automatically make changes and git add/commit/push.

Triggered via crontab & runned within virtualenv (with dependencies)

## Script will do:
1. Make changes: Add new line in txt file
1. Git auto add/commit/push

### Requirements
1. pip:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
2. virtualenv, according to your installed python version: 

Python 2.7x: `pip install virtualenv`

Python 3x: `pip3 install virtualenv`

or simply: `python -m pip install virtualenv`


### Setup:
1. Meet requirements
1. Clone repo
1. Create virtualenv with `virtualenv cronGitEnv`
1. Activate env: `source cronGitEnv/bin/activate` 
1. Install dependencies inside the virtualenv `(cronGitEnv) pip install Gitpython`
1. Setup crontab with `crontab -e`
1. Press `i` to edit
1. Paste the following to activate the env & run the python script at minute 0 every 4hs. (*Check path to match with your local path*)
```
SHELL=/bin/bash
0 */4 * * * cd projects/cronGit/cronGitEnv && source bin/activate && cd .. && python index.py
```

### Credits
Forked from [ospiegel91/cronGit](https://github.com/ospiegel91/cronGit)

[Medium](https://medium.com/@ospiegel51191/how-i-used-cron-to-automatically-simulate-git-activity-13651fd0ca12)
