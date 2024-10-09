import click
import requests
import os

@click.command()
@click.option('--file', 'filepath', required=True, help='Path to the file to upload.')
@click.option('--access_token', 'access_token', required=True, help='Access token for the Zenodo API.')
@click.option('--bucket_url', 'bucket_url', required=True, help='Bucket URL for the upload.')
def upload_file(filepath, access_token, bucket_url):
    """Upload a file to Zenodo using streaming to handle large files efficiently."""
    try:
        # Ensure the file is opened in binary mode
        with open(filepath, "rb") as fp:
            # Prepare the headers and parameters for the request
            headers = {'Accept': 'application/json'}
            params = {'access_token': access_token}
            # Extract the filename to use in the PUT request URL
            filename = os.path.basename(filepath)

            # Perform the streaming upload
            response = requests.put(f"{bucket_url}/{filename}", data=fp, headers=headers, params=params)

            # Check for successful status codes
            if 200 <= response.status_code < 300:
                click.echo("File uploaded successfully.")
                click.echo(response.json())
            else:
                click.echo(f"Error uploading file: {response.text}")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    upload_file()
