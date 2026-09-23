import re

text = """
API_KEY=demo_ABC123456
WALLET_KEY=fake_private_key_123456789
normal_text=hello
"""

patterns = {
    "API key": r"demo_[A-Z0-9]{6,}",
    "Fake wallet key": r"fake_private_key_[0-9]+"
}

for name, pattern in patterns.items():
    matches = re.findall(pattern, text)

    for match in matches:
        print(f"Possible {name} found: {match}")
