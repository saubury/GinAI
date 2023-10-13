# 🍹🤖🍸 GinAI - Cocktails mixed with generative AI

 GinAI - Cocktails mixed with generative AI. Trusting my robotic bartender can make a nice drink from my random collection of juices, mixers and spirits. Real cocktails created and music chosen by OpenAI supported by a RaspberryPi.

![](./docs/ginai.png)

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
 
## Running GinAI
To run GinAI

```bash
python ginai.py --creative
```

 # Links
 - [A clear guide to OpenAI function calling with Python by Naren Yellavula](https://medium.com/dev-bits/a-clear-guide-to-openai-function-calling-with-python-dcbc200c5d70)

 - [OpenAI/GPT: Returning consistent valid JSON from a prompt by Mark Needham](https://www.markhneedham.com/blog/2023/07/27/return-consistent-predictable-valid-json-openai-gpt/)

 
 # Fixes and adhoc notes

 ### Fixes : NotOpenSSLWarning: urllib3

To resolve `NotOpenSSLWarning: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module` try this

```bash
pip uninstall urllib3
pip install 'urllib3<2.0'
```

###  Fixes :  GoogleAssistant AttributeError
AttributeError: 'GoogleAssistant' object has no attribute 'cc'

```bash
pip install PyChromecast==1.0.3
```

### Fixes : Downgrade the protobuf package to 3.20.x or lower. 
```bash
pip install protobuf==3.20.1
```

### Fixes : RGB not working on RaspberryPi
- Set `dtparam=audio=off` in `/boot/config.txt`
- Will need to run as root

