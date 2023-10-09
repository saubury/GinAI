## Setup virtual python environment
Create a [virtual python](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) environment to keep dependencies separate. The _venv_ module is the preferred way to create and manage virtual environments.

 ```console
python3 -m venv .venv
```

Before you can start installing or using packages in your virtual environment you’ll need to activate it. 

```console
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
 ```
 
 # Links
 - https://medium.com/dev-bits/a-clear-guide-to-openai-function-calling-with-python-dcbc200c5d70
 - https://www.markhneedham.com/blog/2023/07/27/return-consistent-predictable-valid-json-openai-gpt/

 ### NotOpenSSLWarning: urllib3

To resolve `NotOpenSSLWarning: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module` try this

```bash
pip uninstall urllib3
pip install 'urllib3<2.0'
```

###  AttributeError
AttributeError: 'GoogleAssistant' object has no attribute 'cc'

```bash
pip install PyChromecast==1.0.3
```

### Downgrade the protobuf package to 3.20.x or lower. 
```bash
pip install protobuf==3.20.1
```

## RGB
 Set `dtparam=audio=off` in `/boot/config.txt`

Will need to run as root

