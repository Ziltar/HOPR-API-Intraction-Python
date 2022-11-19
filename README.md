# HOPR-API-Intraction-Python
A simple script to use the HOPR API in Python. It is used to test the functionality and stability of the node.

## Description
The script opens channels to random nodes at regular intervals, sends direct messages and hop messages. The channels are closed after use.
## Usage

1. Clone the repository : `git clone https://github.com/Ziltar/HOPR-API-Intraction-Python.git && cd HOPR-API-Intraction-Python` 
3. Install requirements: `pip install requirements.txt `
4. Edit the *hoprApi.py* File, set NODE_URL, API_KEY, NODE_HOPR_ADR<br>
	**EXAMPLE:**<bt>
	NODE_URL = "http://127.0.0.1:3001" <br>
	API_KEY = "MyApiToken!12345678!"<br>
	NODE_HOPR_ADR = "16Uiu2HAm7k3J89Z82XHSYFt1KmMvVUierxxK9qsu3EM72QkB9V8a"
5. Run *node-text.py*: `python3 node-test.py`
