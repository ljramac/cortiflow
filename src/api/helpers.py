import hashlib


def get_md5(filepath):
    hash_md5 = hashlib.md5()

    with open(filepath, 'rb') as f:
        for block in iter(lambda: f.read(4096), b""):
            hash_md5.update(block)

    return hash_md5.hexdigest()
