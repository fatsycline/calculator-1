# Hackbright2
Functions &amp; Conditionals

intro@HB:~/intro_class$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   calculator.py

no changes added to commit (use "git add" and/or "git commit -a")
intro@HB:~/intro_class$ git add calculator.py 
intro@HB:~/intro_class$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   calculator.py

intro@HB:~/intro_class$ git commit -m "initial commit"
[master 8be5a14] initial commit
 1 file changed, 32 insertions(+), 12 deletions(-)
 rewrite calculator.py (85%)
intro@HB:~/intro_class$ git remote add origin git remote add origin https://github.com/adinasinger/calculator.git
usage: git remote add [<options>] <name> <url>

    -f, --fetch           fetch the remote branches
    --tags                import all tags and associated objects when fetching
                          or do not fetch any tag at all (--no-tags)
    -t, --track <branch>  branch(es) to track
    -m, --master <branch>
                          master branch
    --mirror[=<push|fetch>]
                          set up remote as a mirror to push to or fetch from

intro@HB:~/intro_class$ git commit -m "initial commit"On branch master
nothing to commit, working directory clean
intro@HB:~/intro_class$ git remote add origin https://github.com/adinasinger/calculator.git
fatal: remote origin already exists.
intro@HB:~/intro_class$ rm -rf .git/
intro@HB:~/intro_class$ git init
Initialized empty Git repository in /home/intro/intro_class/.git/
intro@HB:~/intro_class$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	Functions.py
	README.md
	calculator.py
	conditionals.py

nothing added to commit but untracked files present (use "git add" to track)
intro@HB:~/intro_class$ git add.
git: 'add.' is not a git command. See 'git --help'.

Did you mean this?
	add
intro@HB:~/intro_class$ git add .
intro@HB:~/intro_class$ git commit -m "initial comm it"
[master (root-commit) 77397a4] initial comm it
 4 files changed, 93 insertions(+)
 create mode 100644 Functions.py
 create mode 100644 README.md
 create mode 100644 calculator.py
 create mode 100644 conditionals.py
intro@HB:~/intro_class$ git remote add origin https://github.com/adinasinger/calculator.git
intro@HB:~/intro_class$ git push -u origin master
Username for 'https://github.com': adinasinger
Password for 'https://adinasinger@github.com': 
Counting objects: 6, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.03 KiB | 0 bytes/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/adinasinger/calculator.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
intro@HB:~/intro_class$ 
