import os
import json
import yaml

# Load environment variables (simulated with dotenv)
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID", "AKIAFAKEKEY1234567890")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY", "fakeSecretKeyExample1234567890")

print("AWS Access Key:", aws_access_key)
print("AWS Secret Key:", aws_secret_key)

# Load config from YAML
with open("config.yaml") as f:
    config = yaml.safe_load(f)
    print("GitHub Token:", config["github_token"])

# Load credentials from JSON
with open("creds.json") as f:
    creds = json.load(f)
    print("SMTP User:", creds["smtp_user"])
    print("SMTP Password:", creds["smtp_pass"])

# Read a simulated private key
with open("secrets.txt") as f:
    private_key = f.read()
    print("Private Key (first 40 chars):", private_key[:40])
