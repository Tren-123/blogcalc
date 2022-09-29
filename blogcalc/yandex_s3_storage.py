from storages.backends.s3boto3 import S3Boto3Storage

from .settings import YANDEX_USERS_AVATARS_BUCKET_NAME


class UsersAvatarsStorage(S3Boto3Storage):
    bucket_name = YANDEX_USERS_AVATARS_BUCKET_NAME
    file_overwrite = False
