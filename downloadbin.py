import hashlib
import requests

def download_file(url, local_filename):
    response = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(response.content)

def compute_md5sum(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

# Replace with your actual file URL
url = 'http://10.67.254.10/genbox-ng/rsi-security-builds/castlabs_upgrade_2025/ntv-mv5/product-targets-ntv-mv5-91.23.8.2-secP.bin'
local_filename = 'product-targets-ntv-mv5-91.23.8.2-secP.bin'

download_file(url, local_filename)
md5sum = compute_md5sum(local_filename)

print(f"MD5 checksum: {md5sum}")


