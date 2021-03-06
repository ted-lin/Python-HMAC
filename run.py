#!/usr/bin/env python

from hashlib import md5

trans_5C = "".join(chr(x ^ 0x5c) for x in xrange(256))
trans_36 = "".join(chr(x ^ 0x36) for x in xrange(256))
blocksize = md5().block_size

def hmac_md5(key, msg):
  if len(key) > blocksize:
    key = md5(key).digest()
  key += chr(0) * (blocksize - len(key))
  o_key_pad = key.translate(trans_5C)
  i_key_pad = key.translate(trans_36)
  return md5(o_key_pad + md5(i_key_pad + msg).digest())

if __name__ == "__main__":
  h = hmac_md5("key", "Im ted")
  print h.hexdigest()
