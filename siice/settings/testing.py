from .development import *
import os


MEDIA_ROOT = os.path.realpath(os.path.join(BASE_DIR, 'storage/testing'))
os.makedirs(MEDIA_ROOT, exist_ok=True)
