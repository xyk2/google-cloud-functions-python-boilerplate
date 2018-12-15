# Boilerplate for HTTP Google Cloud Functions Python 3.7 runtime

A simple main.py and associated supporting code to help smooth local development with HTTP triggered functions.

Files listed in `.gcloudignore` are ignored when deploying to GCF through the `gcloud` command line (see [documentation](https://cloud.google.com/sdk/gcloud/reference/topic/gcloudignore)).


Cloud Functions passes the Flask request object to your function, along with additional paths in the URL. For example, a HTTP Function as follows:

`https://asia-northeast1-project-225512.cloudfunctions.net/function-1` 

could also be called with additional parameters like this: 

`https://asia-northeast1-project-225512.cloudfunctions.net/function-1/more/parameters/in/url` (accessed with request.path). 

This can be helpful in certain functions that require GET and caching setups that don't cache by query strings.
