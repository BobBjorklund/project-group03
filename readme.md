How to install our report:
clone the repo
open a terminal in the root of the repo
run "sh install.sh"
this will drop and then create a Postgres database named "goats"
it will then create the necessary tables, import the data, and manipulate it into useful views
it will activate a virtual environment from which to launch the django server (virtual environment only works on linux machines or vms)
it will then launch the django website, and open firefox to display the landing page.
