import re

# Exemple de données extraites manuellement de la capture
data = """
11:42:04.766656 IP BP-Linux8.ssh > 192.168.190.130.50019: Flags [P.], seq 2243505564:2243505672, ack 1972915080, win 312, options [nop,nop,TS val 102917262 ecr 377952805], length 108
11:42:04.766694 IP BP-Linux8.ssh > 192.168.190.130.50019: Flags [P.], seq 108:144, ack 1, win 312, options [nop,nop,TS val 102917262 ecr 377952805], length 36
11:42:04.766723 IP BP-Linux8.ssh > 192.168.190.130.50019: Flags [P.], seq 144:252, ack 1, win 312, options [nop,nop,TS val 102917262 ecr 377952805], length 108
"""

# Regex pour extraire les informations nécessaires
pattern = r"IP (?P<src>[\w.-]+) > (?P<dst>[\w.-]+): Flags \[(?P<flags>[\w.]+)\], seq (?P<seq>[\d:]+), ack (?P<ack>\d+), win (?P<win>\d+), options \[.*\], length (?P<length>\d+)"

matches = re.finditer(pattern, data)
entries = []

# Extraction des données
for match in matches:
    entries.append(match.groupdict())

# Génération de la page Markdown
markdown_content = "# Network Data Capture\n\n"
markdown_content += "## Extracted Data\n\n"
markdown_content += "| Source IP       | Destination IP   | Flags | Seq Range         | Ack Number  | Window Size | Length |\n"
markdown_content += "|-----------------|------------------|-------|-------------------|-------------|-------------|--------|\n"

for entry in entries:
    markdown_content += f"| {entry['src']} | {entry['dst']} | {entry['flags']} | {entry['seq']} | {entry['ack']} | {entry['win']} | {entry['length']} |\n"

# Sauvegarde dans un fichier Markdown
with open("network_data.md", "w") as file:
    file.write(markdown_content)

print("Markdown file generated: network_data.md")
