import requests

#Define the header values.  Comment out the header attributes you don't want to include.
HTTP_header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
#                'Cookie': '',
#                'Accept': '*/*',
#                'Accept-Language': 'en-US',
#                'Accept-Encoding': '',
#                'Authorization': ''
                }
#Define the content sent through the body of the HTTP request.  Comment out the body attributes you don't want to include.
HTTP_body = {
#            'username': 'test',
#            'password': 'test',
#            'variable': 'value'
#            'keyvaluevalue': ['value1', 'value2']
            }

#Define the conent sent through as HTTP parameters in GET requests.  Each variable within this list will be seperated by a ? in the GET URL.  Comment out the parameter attributes you don't want to include.
HTTP_parameters = {
#            'username': 'test',
#            'password': 'test',
#            'variable': 'value'
#            'keyvaluevalue': ['value1', 'value2']
            }

#Define the local file path to the file used in an HTTP POST / PUT upload.
HTTP_localfile = 'Path/To/File.extension'

##HTTP Request Methods

#HTTP GET. Only includes header, no body.  However, you can pass URL parameters defined above if the destination supports it.
#response = requests.get('http://127.0.0.1:8090', headers=HTTP_header, params=HTTP_parameters)

#HTTP HEAD. Only includes header, no body.
#response = requests.delete('URL', headers=HTTP_header)

#HTTP OPTIONS.  Only includes header, no body.
#response = requests.options('URL', headers=HTTP_header)

#HTTP DELETE. Only includes headers, no body.
#response = requests.delete('URL', headers=HTTP_header)

#HTTP PUT and POST. PUT is primarily used for file upload while POST is used for passing data in a body rather than a GET URL parameter.
#response = requests.post('URL', headers=HTTP_header, data=HTTP_body)
#response = requests.put('URL', headers=HTTP_header, data=HTTP_body)

#For files, you can pass them as a seperate argument instead of the data for body.
#response = requests.post('URL', headers=HTTP_header, files={'file':open(HTTP_localfile, 'rb')})
#response = requests.put('URL', headers=HTTP_header, files={'file':open(HTTP_localfile, 'rb')})


##Various attribues of the response that can be printed.
#print(response.status_code)
#print(response.headers)
#print(response.text)
#print(response.cookies['key'])
