# zenodo_upload_cli
Upload files to Zenodo via CLI.

Uploading large files via the web interface of Zenodo often fails due to timeouts and if these large files are sitting on an HPC with faster internet connection than say, eduroam, uploading via the CLI is the way to go. 
I whipped up this procedure to do it directly from the CLI of any internet connected device. Bonus: no failed uploads, much faster uploads!

Step 1) Get an access token from Zenodo: https://zenodo.org/account/settings/applications/tokens/new/

Step 2) Create a new deposition or a draft update for an existing deposition.

Step 3) Get the deposition ID from the address bar in your browser. For example: 13908086 

Step 4) Using curl with your access token and deposition ID, retrieve the bucketID where the files are physically located on Zenodo.
`curl https://zenodo.org/api/deposit/depositions/<YOURDEPOSITIONID>?access_token=<YOURACCESSTOKENHERE>`

Step 5) This will retrieve a ton of metadata in a json file, the bucket_id is in `links`
```"links": {"self": "https://zenodo.org/api/deposit/depositions/13908086", "html": "https://zenodo.org/deposit/13908086", "badge": "https://zenodo.org/badge/doi/.svg", "files": "https://zenodo.org/api/deposit/depositions/13908086/files", "bucket": "https://zenodo.org/api/files/<YOURBUCKETID>"```

Step 6) Armed with bucket ID, access_token and this repo, run 

`git clone git@github.com:bordin89/zenodo_upload_cli.git`
`cd zenodo_upload_cli`
`python3 -m venv venv`
`source venv/bin/activate`
`pip install --upgrade pip wheel`
`pip install -r requirements.txt`
`python3 upload_to_zenodo.py --file <YOURFILETOUPLOAD> --access_token <YOURACCESSTOKEN> --bucket_url https://zenodo.org/api/files/<YOURBUCKETID`

If you obtain
`File uploaded successfully.` 
followed by metadata, your upload was successful and it's safe to refresh your Zenodo webpage. Your file will be listed in the deposition.






