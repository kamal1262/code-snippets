# [START kms_encrypt_symmetric]
# def encrypt_symmetric(project_id, location_id, key_ring_id, key_id, plaintext):
#     """
#     Encrypt plaintext using a symmetric key.
#     Args:
#         project_id (string): Google Cloud project ID (e.g. 'my-project').
#         location_id (string): Cloud KMS location (e.g. 'us-east1').
#         key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
#         key_id (string): ID of the key to use (e.g. 'my-key').
#         plaintext (string): message to encrypt
#     Returns:
#         bytes: Encrypted ciphertext.
#     """
project_id = 'gcp-self-training'
location_id = 'asia-east1'
key_ring_id = 'bangladesh'
key_id = 'covid'
plaintext ="kamal-1262, cadet"

# Import the client library.
from google.cloud import kms

# Import base64 for printing the ciphertext.
import base64

# Convert the plaintext to bytes.

plaintext_bytes = plaintext.encode('utf-8')

# Create the client.
client = kms.KeyManagementServiceClient()

# Build the key name.
key_name = client.crypto_key_path(project_id, location_id, key_ring_id, key_id)
print("key_name:", key_name)
# Call the API.
encrypt_response = client.encrypt(key_name, plaintext_bytes)
print('Ciphertext: {}'.format(base64.b64encode(encrypt_response.ciphertext)))
print("encrypt_response:", encrypt_response)
# [END kms_encrypt_symmetric]



## decrypt

# Call the API.
decrypt_response = client.decrypt(key_name, encrypt_response.ciphertext)
print('Plaintext: {}'.format(decrypt_response.plaintext))
