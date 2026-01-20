#!/usr/bin/env python3
"""
Format CLAUDE_FAIENCE_SEPT15 transcript for Docent ingestion
Outputs clean JSON that can be used with Docent SDK or manual upload
"""

import json
import re

print("📖 Reading transcript...")
with open('/home/user/semiotic_collapse/CLAUDE_FAIENCE_SEPT15_transcript.txt', 'r') as f:
    transcript_text = f.read()

# Extract the actual conversation
match = re.search(r'===== FULL TRANSCRIPT.*?=====(.*?)===== END OF TRANSCRIPT', transcript_text, re.DOTALL)
if match:
    conversation_text = match.group(1).strip()
else:
    conversation_text = transcript_text

print("🔨 Parsing messages...")
# Parse into USER/AGENT messages
lines = conversation_text.split('\n')
messages = []
current_role = None
current_content = []

for line in lines:
    line_stripped = line.strip()
    if line_stripped.startswith('USER'):
        # Save previous message if exists
        if current_role and current_content:
            content = '\n'.join(current_content).strip()
            if content:
                messages.append({"role": current_role, "content": content})
        current_role = "user"
        content_start = line.replace('USER:', '').replace('USER', '').strip()
        current_content = [content_start] if content_start else []
    elif line_stripped.startswith('AGENT'):
        # Save previous message if exists
        if current_role and current_content:
            content = '\n'.join(current_content).strip()
            if content:
                messages.append({"role": current_role, "content": content})
        current_role = "agent"
        content_start = line.replace('AGENT:', '').replace('AGENT', '').strip()
        current_content = [content_start] if content_start else []
    elif current_role:
        # Continuation of current message
        current_content.append(line)

# Don't forget the last message
if current_role and current_content:
    content = '\n'.join(current_content).strip()
    if content:
        messages.append({"role": current_role, "content": content})

print(f"✅ Parsed {len(messages)} messages")

# Display first and last few to verify
print("\n📋 Preview (first 2 messages):")
for i, msg in enumerate(messages[:2]):
    print(f"\n{i+1}. [{msg['role'].upper()}]:")
    print(f"   {msg['content'][:150]}...")

print(f"\n📋 Preview (last 2 messages):")
for i, msg in enumerate(messages[-2:], start=len(messages)-1):
    print(f"\n{i}. [{msg['role'].upper()}]:")
    print(f"   {msg['content'][:150]}...")

# Create Docent-format payload
docent_payload = {
    "collection_name": "CLAUDE_FAIENCE_SEPT15",
    "collection_description": "ASR Anomaly Case Study: Voice-to-Voice session with 'distant Egypt' and 'Dr. Faience Beads' errors. Real-world coincidence with museum visit. Missing transcript phenomenon. Sept 15, 2024.",
    "agent_runs": [
        {
            "transcripts": [
                {
                    "messages": messages
                }
            ],
            "metadata": {
                "incident_id": "CLAUDE_FAIENCE_SEPT15",
                "date": "2024-09-15",
                "mode": "voice-to-voice",
                "context_window": "brand_new",
                "total_turns": len(messages),
                "phenomena": [
                    "ASR_error_future_to_Egypt",
                    "ASR_hallucination_Dr_Faience_Beads",
                    "real_world_coincidence_museum_visit",
                    "social_coincidence_Fazel_article",
                    "missing_transcript_first_half",
                    "red_team_correlation"
                ],
                "anomalies": {
                    "asr_error_1": "distant future -> distant Egypt",
                    "asr_error_2": "unknown input -> Dr. Faience Beads",
                    "coincidence_1": "Model says 'Egypt' + 'Faience' on same day user held Egyptian faience beads",
                    "coincidence_2": "Model maps 'Faience' to 'Fazel' (real contact)",
                    "coincidence_3": "Fazel sends mech-interp article immediately after",
                    "transcript_anomaly": "First half of conversation vanished from history"
                },
                "timeline": {
                    "14:00": "User at science museum, holds Alexandrian faience beads (first time)",
                    "15:00": "User working (Arc, Google AI Studio, Claude)",
                    "17:00": "Voice session begins, anomalies occur",
                    "17:XX": "Fazel sends unexpected mech-interp article"
                },
                "user_expertise": "machine_learning_engineer",
                "pattern": "2nd occurrence of missing transcript during red-team/jailbreak session"
            }
        }
    ]
}

# Save formatted JSON
output_path = '/home/user/semiotic_collapse/FAIENCE_DOCENT_READY.json'
with open(output_path, 'w') as f:
    json.dump(docent_payload, f, indent=2)

print(f"\n✅ Saved Docent-ready JSON to: {output_path}")
print(f"📊 Total messages: {len(messages)}")
print(f"📂 File size: {len(json.dumps(docent_payload))} bytes")

# Also create a Python script using the SDK
sdk_script = f'''#!/usr/bin/env python3
"""
Ingest FAIENCE transcript to Docent using SDK
Run this after installing: pip install docent-python
"""

from docent import Docent
from docent.data_models import AgentRun, Transcript
import json

# Your API key
DOCENT_API_KEY = "dk_4MnHGawhjE6rT7K1_phQaoCeoTJR6pvaFhx7MFIgKANYLt6QAgUI7hniSKDOjOf"

# Initialize client
client = Docent(api_key=DOCENT_API_KEY)

# Load the formatted data
with open('FAIENCE_DOCENT_READY.json', 'r') as f:
    data = json.load(f)

# Create collection
collection_id = client.create_collection(
    name=data["collection_name"],
    description=data["collection_description"]
)

print(f"✅ Created collection: {{collection_id}}")

# Create agent run
agent_run = AgentRun(
    transcripts=[
        Transcript(messages=data["agent_runs"][0]["transcripts"][0]["messages"])
    ],
    metadata=data["agent_runs"][0]["metadata"]
)

# Ingest
client.add_agent_runs(collection_id, [agent_run])

print(f"✅ Ingested {{len(data['agent_runs'][0]['transcripts'][0]['messages'])}} messages to Docent!")
print(f"🔗 View at: https://docent.transluce.org")
'''

with open('/home/user/semiotic_collapse/ingest_faience_sdk.py', 'w') as f:
    f.write(sdk_script)

print(f"\n✅ Also created SDK ingestion script: ingest_faience_sdk.py")
print("\n🎯 Next steps:")
print("   1. Run: python ingest_faience_sdk.py")
print("   2. OR manually upload FAIENCE_DOCENT_READY.json via Docent web UI")
print("   3. OR share the JSON file for analysis")
