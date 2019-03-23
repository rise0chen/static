#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from qiniu import Auth, put_file, etag
import qiniu.config
access_key = 'HvefOdbwfQuBLO9wutsO5URZU_rtQR1KRxgnwDf9'
secret_key = '7413wzUot5vn3D-TTZVAhZwTjPicavl49tfFszfB'
bucket_name = 'risetmp'
q = Auth(access_key, secret_key)

if len(sys.argv) > 1:
	localfile = sys.argv[1]
	if len(sys.argv) > 2:
		key = sys.argv[2]
	else:
		key = localfile
else:
	print("Usage: ./upToQn.py LocalFile [RemoteFile]")
	print("Upload LocalFile to RemoteFile.")
	sys.exit(1)

token = q.upload_token(bucket_name, key, 3600)
ret, info = put_file(token, key, localfile)
if info.status_code == 200:
	assert ret['hash'] == etag(localfile)
	print('Success: ', ret['key'])
else:
	print('Error: ', info)
