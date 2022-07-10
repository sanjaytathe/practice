'''
1) what is GIT ??
:- Git is a distributed version control system for tracking the changes
   in source code during software development
:- A version control system keeps track of changes made in set of files
:- git allow you to see what changes where made in code and who changes the code
:-  It is a free and open-source version control system used to handle small to very large projects efficiently.
------------------------------------------------------------------------------------------------------------------------
2) what is git hub ??
:- GitHub is a for-profit company offering a cloud-based Git repository that helps
    developers store, manage, track and control changes to their code
:- GitHub is so user-friendly, though, that some people even use GitHub to manage other types of projects
------------------------------------------------------------------------------------------------------------------------
3) git config ??
:-  a convenience function that is used to set Git configuration values on a global or local project level
:- you can change name,email by git confi command
------------------------------------------------------------------------------------------------------------------------
4) what is repository ??
:- A repository contains all of your project's files and each file's revision history.
   You can discuss and manage your project's work within the repository
------------------------------------------------------------------------------------------------------------------------
5) what is SSH key   (Secure Shell) keys ??
:- ssh-keygen is a standard component of the Secure Shell protocol suite found on Unix,
   Unix-like and Microsoft Windows computer systems used to establish secure shell sessions
   between remote computers over insecure networks, through the use of various cryptographic techniques.
   :-SSH keys are a pair of public and private keys that are used to authenticate and establish an encrypted
    communication channel between a client and a remote machine over the internet.
------------------------------------------------------------------------------------------------------------------------
6) how to delete branch ??
 :- git branch -d feature (for deleting branch)
--- --------------------------------------------------------------------------------------------------------------------
7) how to create new branch ??
:- git branch feature<branch name> (to create branch )
------------------------------------------------------------------------------------------------------------------------
8) switching between the branch ??
:-  git checkout feature<branch name>( to shift the branch)
------------------------------------------------------------------------------------------------------------------------
9) how to merge branch ??
:- git merge feature1<branch name>
  all file will be seen in master branch
------------------------------------------------------------------------------------------------------------------------
 what is git branch ??
 :- A branch is a version of the repository that diverges from the main working project.
    It is a feature available in most modern version control systems.
------------------------------------------------------------------------------------------------------------------------
10) what is commit ? how to create a commit file ??
:- Adding commits keep track of our progress and changes as we work
:- a commit is an operation which sends the latest changes of the source
   code to the repository, making these changes part of the head revision of the repository.
:- git commit -m 'comment'
------------------------------------------------------------------------------------------------------------------------
11) what is pull ??
:- git pull download latest changes into local repository and it also automatically merge
   change in your working directory
------------------------------------------------------------------------------------------------------------------------
12) what is push ??
:- The git push command is used to upload local repository content to a remote repository.
:- git push add origin
------------------------------------------------------------------------------------------------------------------------
13)what is fetch ?
:- git fetch only download latest changes into local repository
:- it download fresh changes that other developer have push to the remote repository
:- we will have to merge manually at a later time using git merge
------------------------------------------------------------------------------------------------------------------------
14) what is repository??
:- repository is place where files and folder are stored

local repository:- Git local repository is the one on which we will make local changes,
                 typically this local repository is on our computer

remote repository :- some file stored in some remote location or server
------------------------------------------------------------------------------------------------------------------------
15)  What are GitHub's Features
Easy Project Management. ...
Increased Safety With Packages. ...
Effective Team Management. ...
Improved Code Writing. ...
Increased Code Safety. ...
Easy Code Hosting.
------------------------------------------------------------------------------------------------------------------------
16) what is git status ??
:- The git status command displays the state of the working directory and the staging area
:- git status
------------------------------------------------------------------------------------------------------------------------
17) what is git log??
:- The git log command displays all of the commits in a repository's history.
------------------------------------------------------------------------------------------------------------------------
18) how to push git file in github
1. Create a new GitHub Repo
2. Initialize Git in the project folder
3. Add the files to Git index.
4. Commit Added Files
5. Add new remote origin (in this case, GitHub)
git remote add origin git@github.com:sammy/my-new-project.git
6. Push to GitHub.
git remote -v  (for push address)
git push origin master
------------------------------------------------------------------------------------------------------------------------
19) how to count branch
:- git branch / git branch -r
------------------------------------------------------------------------------------------------------------------------
20) what is git ignore ? its purpose ?
:- The . gitignore file tells Git which files to ignore when committing your project to the GitHub repository
:- he git ignore file rule allows you to ignore a file you've committed in the past
:- It helps you keep your code repository clean by ignoring unwanted files
---------------------------------------------------------------------------------------------------------------------------
21) how to clone file from git hub ??
:- to make folder in desktop
   go to folder and open gitbash
   type git clone <copy paste ssh key>
   then copy all the file from repository
-------------------------------------------------------------------------------------------------------------------------
22) all command
1) how can you check git installed or not
:- git --version

2) git status (to check status)
3)git init (to make git folder)
4)touch demo(file_name).txt ( for create txt file)
5) git add demo(file_name).txt (for untrack to track/staged area)
6)start demo.txt (for open file) you can check status (git status)
if you modified in file the file will go to modified
7)git add demo(file_name).txt (for untrack to track/staged area)
8)at a time more than one file untrack to stage
:- git add .
9) commit file before push
:- git commit -m 'intial commit'
10) git log (show all commit )
11)if you want to change name
:- git config --global user.name sanjay
12)if you want to change email
:- git config --global user.email sgtathe1998@gmail.com
13)if you want to change username
:- git config --global user.username sanjay
14) if you want to check you name changed or not
:- git config --global user.name
:- same procedure for email and username
15) check your commit :- git log
16) git remote add origin (paste ssh path from site)
17) git remote -v  (for push address)
18) git push origin master (last command)
18) git checkout demo.txt ( for undo)
19) git restore file_name or delete file



1) git branch (to check branches)
2)git branch feature<branch name> (to create branch )
3) git checkout feature<branch name>( to shift the branch)
4)  git checkout -b feature1 (direct create and shift)
5) git branch -d feature (for deleting branch)
6) git checkout (for undo)
7) git checkout <file_name> (for undo file)
8) git checkout -f (for undo all file)
9) ls ( show all file )
10) git rm --cached <file_name> (stage to untracked)
11) git rm -f <file_name> (for delete file )
12) git merge <branch_name> (for merge file in master)
13) git clone <paste ssh key>
14) git push origin --delete feature1<file_name> ( delete from github )
15) git diff (show changes)
16) git diff --staged ( on staged )
17) git clone <copy paste ssh key> (copy all file from repository)




'''