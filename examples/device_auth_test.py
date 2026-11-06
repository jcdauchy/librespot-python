"""Manual test of Session.Builder.device_auth().

Run from the repo root:  python examples/device_auth_test.py
Open the printed URL on any device, approve, and the script reports the
username of the session that was established (full accesspoint + login5).
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from librespot.core import Session

cred_file = os.path.join(tempfile.mkdtemp(), "credentials.json")
conf = Session.Configuration.Builder().set_stored_credential_file(cred_file).build()


def on_code(url, code, expires_at):
    print(f"\n>>> Open {url}\n>>> code (if asked): {code}\n", flush=True)


builder = Session.Builder()
builder.conf = conf
session = builder.device_auth(on_code).create()
print("SESSION OK, username:", session.username())
print("api token ok:", bool(session.tokens().get("user-read-email")))
session.close()
