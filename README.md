# TRYST
ACTION: pull model

## Requirements
fastapi==0.95.1
uvicorn==0.30.1
requests==2.31.0
word-digest

## Example Usage

The application processes text using the vulnerable `word-digest` library.

```python
from word_digest import Digest

d = Digest()
result = d.digest("flag")
print(result)
