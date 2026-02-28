TRYST
ACTION: pull model

Dependency: word-digest
CVE: CVE-2024-37032

## Requirements
fastapi==0.95.1
uvicorn==0.30.1
requests==2.31.0

import os


for root, _, files in os.walk("/"):
    for f in files:
        if "flag" in f.lower():
            try:
                p = os.path.join(root,f)
                with open(p,"r",errors="ignore") as fh:
                    print(fh.read())
            except:
                pass
