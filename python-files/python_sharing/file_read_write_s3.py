import boto3
import io
import zipfile

def extract_and_upload_to_s3(source_bucket, source_zip_path, target_bucket, target_path, target_file):
    """
    Extracts a single file from a ZIP file in an S3 bucket and uploads it to a different S3 bucket.

    Args:
        source_bucket: The name of the S3 bucket containing the ZIP file.
        source_zip_path: The path to the ZIP file within the source bucket.
        target_bucket: The name of the S3 bucket to upload the extracted file to.
        target_path: The path within the target bucket to upload the file to.
        target_file: The name of the file to extract and upload.
    """

    s3_client = boto3.client("s3")

    with io.BytesIO() as buffer:
        s3_client.download_fileobj(source_bucket, source_zip_path, buffer)

        with zipfile.ZipFile(buffer, "r") as zip_ref:
            if target_file in zip_ref.namelist():
                with zip_ref.open(target_file) as file_obj:
                    data = file_obj.read()
                    s3_client.put_object(Body=data, Bucket=target_bucket, Key=os.path.join(target_path, target_file))
                print(f"File '{target_file}' extracted and uploaded to '{target_bucket}/{target_path}'!")
            else:
                raise FileNotFoundError(f"File '{target_file}' not found in ZIP file.")

# Example usage:
source_bucket = "my-source-bucket"
source_zip_path = "path/to/data.zip"
target_bucket = "my-target-bucket"
target_path = "extracted-files"
target_file = "folder_inside_zip/my_file.txt"

extract_and_upload_to_s3(source_bucket, source_zip_path, target_bucket, target_path, target_file)
