Updating the website on Google Container Engine
===================


Use theses steps in your terminal window to push a new version of the website/webapp to Google Container Engine.

----------


Steps to update app:
--------------------

 1. Gather all the static content locally into one folder
     > **$ python manage.py collectstatic**

 2. If there are updated static files: then upload this static content to the bucket
    > **$ gsutil rsync -R static/ gs://#project-id#/static**

 3. Update mysite/settings.py:
	> **Debug = False**

 4. Build a new Docker image
	> **$ docker build -t gcr.io/#project-id#/polls:#version# .**

 5. Push newly built Docker image to Google Container Registry:
	> **$ gcloud docker -- push gcr.io/#project-id#/#version#**

 5. Update pods with newly pushed image:
	> **$ kubectl set image deployment polls polls-app=gcr.io/#project-id/polls:#version# --record**

 6. Check status of update (it should take about 65 seconds to tear down old pods and spin up new ones):
	> **$ kubectl get pods**

 6. Delete old images to save space in cloud repository
	> **$ gcloud container images list-tags gcr.io/#project-id#/polls**
	> **$ gcloud container images delete gcr.io/#project-id#/polls:<version>**
 7. Replace #version# above with latest image version in the images list-tags step, incremented by one

 8. Replace #project-id# with emailed project-id

