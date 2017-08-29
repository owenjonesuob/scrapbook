# Add the repo to be merged as a remote of the parent project
git remote add banescpl https://github.com/owenjonesuob/BANEScarparkinglite.git

# Use --prefix to specify a filepath for where to bring the subprojcet in
git subtree add --prefix=r/BANEScarparkinglite/ banescpl master

# Later maybe you've made changes to the subproject which you want to bring into
# the overarching project too. So, from the PARENT project:
git subtree push --prefix=r/BANEScarparkinglite/ banescpl dev-branch