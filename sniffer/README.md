# sniffer

**Category:** crypto

This challenge is about Block Cipher on Counter mode, but with initial vector reusing problem, besides the first log that is just shown.

## Deploy

After changing directory to `/sniffer`, you can run a server with:

```bash
docker compose -up --build -d
```

Then access the challenge with netcat:

```bash
nc localhost 31337
```

## Local Run

Because it gets the flag value from the env, for local testing you need to adjust the main code by loading the env:

```python
from dotenv import load_dotenv

load_dotenv()
```

Then you can run normally with:

```bash
python main.py
```
