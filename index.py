from git import Repo

working_tree_dir = '/Users/seba/projects/cronGit'
file = "autoGitActivity/activityTracker.txt"
repo = Repo(working_tree_dir)

ssh_cmd = 'ssh -i ~/.ssh/id_dsa'

def gitActivities(repo):
    with repo.git.custom_environment(GIT_SSH_COMMAND=ssh_cmd):
        files = repo.git.diff(None, name_only=True)
        if len(files):
            repo.git.add(A=True)
            repo.git.commit('-m', 'add line & auto push')
            repo.git.push('origin', 'master') 


def alterFile(file):
    with open(file, "a") as f:
        f.write("new line\n")


alterFile(file)
gitActivities(repo)