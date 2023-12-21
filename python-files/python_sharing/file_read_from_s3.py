import boto3
import io

def extract_from_s3(bucket_name, zip_filename, target_file, extract_dir="."):
  """
  Extracts a single file from a ZIP file in an S3 bucket.

  Args:
    bucket_name: The name of the S3 bucket containing the ZIP file.
    zip_filename: The filename of the ZIP file in the bucket.
    target_file: The name of the file to extract.
    extract_dir: The directory to extract the file to (default: current directory).

  Raises:
    FileNotFoundError: If the ZIP file or target file is not found.
  """

  # Create S3 client
  s3_client = boto3.client("s3")

  # Get object info
  try:
    head_object = s3_client.head_object(Bucket=bucket_name, Key=zip_filename)
  except ClientError as e:
    if e.response["Error"]["Code"] == "404 NotFound":
      raise FileNotFoundError(f"File '{zip_filename}' not found in S3 bucket '{bucket_name}'.")
    else:
      raise e

  # Check if target file exists within the ZIP
  with io.BytesIO() as buffer:
    s3_client.download_fileobj(bucket_name, zip_filename, buffer)
    zip_file = zipfile.ZipFile(buffer, "r")
    if target_file not in zip_file.namelist():
      raise FileNotFoundError(f"File '{target_file}' not found in ZIP file '{zip_filename}'.")

  # Extract the file directly to the specified directory
  with zip_file.open(target_file) as file_obj:
    with open(os.path.join(extract_dir, target_file), "wb") as output_file:
      output_file.write(file_obj.read())

  print(f"File '{target_file}' successfully extracted from '{zip_filename}' in S3 bucket {bucket_name}!")

# Example usage
bucket_name = "my-s3-bucket"
zip_filename = "data.zip"
target_file = "my_file.txt"
extract_dir = "/path/to/extract"

extract_from_s3(bucket_name, zip_filename, target_file, extract_dir)
