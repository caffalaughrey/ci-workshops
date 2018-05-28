# Travis CI Workshop

The purpose of the workshop is to get a working build of this sample repository up and running.
Ideally, you'll be able to apply this to any project!

## Sign up
1. To begin, navigate to [Travis](https://travis-ci.org/) and click 'Sign in with GitHub'.
2. Enter your Github credentials.
3. You'll be prompted to authorise Travis for open source. Review the permissions here, then click
'Authorise travis-ci'.
4. You'll land on a page listing your repositories.  Toggle 'ci-workshops' on this page.

## Add .travis.yml
1. Fork this repository.
2. Create a branch called `travis-ci-workshop`
3. From a terminal, run `git clone -b travis-ci-workshop https://github.com/<your user>/ci-workshops.git`
4. In your new local `ci-workshops` directory, create a new file called `.travis.yml`
5. Edit `.travis.yml`.  Since this is a Python project, use the
[Travis documentation](https://docs.travis-ci.com/user/languages/python/) to prepare this file.
6. Add your files, commit, and push this branch.
7. Navigate to https://travis-ci.org/ &lt;your user&gt;/ci-workshops, sit back, and wait for your build to complete. If it
fails, troubleshoot and repeat steps 6-7!  You can troubleshoot by clicking into a failed job like
[this one](https://travis-ci.org/caffalaughrey/ci-workshops/jobs/384779290), then inspecting the logs.

## Extra credit
Add a shield to this README file showing the build status!
