import math
from binascii import unhexlify, hexlify
from Crypto.Cipher import ChaCha20

def encryption(plaintext: bytes, key: bytes, nonce: bytes) -> bytes:
  plaintext = unhexlify(plaintext)
  key = unhexlify(key)
  nonce = unhexlify(nonce)

  cipher: ChaCha20.ChaCha20Cipher = ChaCha20.new(key=key, nonce=nonce)
  ciphertext: bytes = cipher.encrypt(plaintext)
  return hexlify(ciphertext)


def Hash(message: bytes) -> bytes:
  message_in_hex: bytes = hexlify(message)
  len_message_in_hex: int = len(message_in_hex)

  initial_vector: bytes = message_in_hex[:128]
  if(len(initial_vector) < 128):
    padding: bytes = bytes('f' * (128 - len(initial_vector)), "utf-8")
    initial_vector = initial_vector + padding

  initial_nonce: bytes = initial_vector[:16]

  total_range: int = math.ceil(len_message_in_hex/64)
  for i in range(total_range):
    idx: int = i * 64
    key: bytes = message_in_hex[idx: idx+64]
    if(len(key) < 64):
      padding: bytes = bytes('0' * (64 - len(key)), "utf-8")
      key: bytes = key + padding

    initial_vector: bytes = encryption(initial_vector, key, initial_nonce)
    initial_nonce: bytes = initial_vector[:16]

  digest: bytes = initial_vector
  return digest


def App():
  input_string: str = input("Please provide your message: ")
  message: bytes = bytes(input_string, "utf-8")
  output_digest: bytes = Hash(message)
  print(f"message: {input_string}")
  print(f"digest: {output_digest}")
  return output_digest
