import http.client
import mimetypes
import string
import random

def post_multipart(host, port, selector, fields, files):
    content_type, body = encode_multipart_formdata(fields, files)

    if(selector.find('https') == 0):
        h = http.client.HTTPSConnection(host, port)
    else:
        h = http.client.HTTPConnection("127.0.0.1", 8888)

    #h.set_tunnel(host, 8080)
    h.putrequest('POST', selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.endheaders()
    h.send(body)
    response = h.getresponse()
    return response.read()

def encode_multipart_formdata(fields, files):
    BOUNDARY_STR = get_random_str(30)
    CHAR_ENCODING = "utf-8"
    CRLF = bytes("\r\n", CHAR_ENCODING)
    L = []
    for (key, value) in fields.items():
        L.append(bytes("--" + BOUNDARY_STR, CHAR_ENCODING))
        L.append(bytes('Content-Disposition: form-data; name="%s"' % key, CHAR_ENCODING))
        L.append(b'')
        L.append(bytes(value, CHAR_ENCODING))
    for (key, value) in files.items():
        filename = value['filename']
        content = value['content']
        L.append(bytes('--' + BOUNDARY_STR, CHAR_ENCODING))
        L.append(bytes('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename), CHAR_ENCODING))
        L.append(bytes('Content-Type: %s' % get_content_type(filename), CHAR_ENCODING))
        L.append(b'')
        L.append(content)
    L.append(bytes('--' + BOUNDARY_STR + '--', CHAR_ENCODING))
    L.append(b'')

    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=' + BOUNDARY_STR
    return content_type, body

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

def get_random_str(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])
