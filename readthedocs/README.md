# readthedocs Workshop

# Sign Up
1. Navigate to https://readthedocs.org/accounts/signup/
2. Click 'Sign up with Github'.
3. You'll be prompted to authorise 'Read the Docs Community (.org)' for open source. Review the permissions here, then click 'Authorise readthedocs'.
4. Confirm your account info

# Configure this repository
1. Navigate to https://readthedocs.org/dashboard/import/manual/.
2. Under Project Details, populate the fields with the following values:
  - Name: ci-workshops
  - Repository URL: https://github.com/your_user/ci-workshops.git
  - Repository type: Git
3. Navigate to [Advanced > Admin Settings](https://readthedocs.org/dashboard/ci-workshops/advanced/)
4. Under Advanced Settings, configure the settings accordingly:
  - Install your project inside a virtualenv using setup.py install: **checked**
  - Requirements file: **/readthedocs/requirements.txt**
  - Default branch: **_this-branch-name_**
  