Running the website locally
===================


Use these steps in your terminal window to run the GCE webapp version locally.

----------


Steps to run app:
--------------------

 1. Start Gcloud sql proxy in a separate terminal window:
     > **$ ./cloud_sql_proxy -instances="#project-id#:us-east4:solarpv-postgres"=tcp:5432 -credential_file="#path to json credential file#"**

 2. Set local environment variables (as per credential file)

 3. Start local environment (cd into webapp-google-container-engine) ($pip install -r requirements.txt if initiating virtualenv):
    > **$ source env/bin/activate**

 3. Update mysite/settings.py:
	> **Debug = true**

 4. Start a local web server
	> **$ python manage.py runserver**

 5. Browse to webpage:
	> **$ open http://127.0.0.1:8000/**

 

----------
Note: If not in group, email for credentials

