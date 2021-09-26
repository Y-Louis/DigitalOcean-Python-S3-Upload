import os, datetime, boto3

# Upload Variables
SpaceRegion = "" # Space Region
SpaceEndPoint = "" # Space Endpoint
SpaceAccessKey = "" # Space Access Key
SpaceSecretKey = "" # Space Secret

FilesDirectory = "" # Directory on your server
UploadDirectory = "" # Target Directory on DO Space


# Configure Connection
SpaceConnection = SpaceSession.client("s3", region_name=SpaceRegion, endpoint_url=SpaceEndPoint, aws_access_key_id=SpaceAccessKey, aws_secret_access_key=SpaceSecretKey)


# Upload Files
for filename in os.listdir(FilesDirectory):
    SpaceConnection.upload_file(FilesDirectory + filename, UploadDirectory, filename)
