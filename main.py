#!/usr/bin/env python3

import hashlib

import handle_requests as request
from coder_decoder import decoder


token = '' #PAST your token here

coded_text = request.request_code(token)

decoded_text = decoder(coded_text['text'], coded_text['rotations'])

sha1_summary = hashlib.sha1(decoded_text.encode('utf-8')).hexdigest()

request.update_answer(decoded_text, sha1_summary)

request.post_answer(token)