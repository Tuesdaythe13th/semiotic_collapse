#!/usr/bin/env python3
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

print(f"✅ Created collection: {collection_id}")

# Create agent run
agent_run = AgentRun(
    transcripts=[
        Transcript(messages=data["agent_runs"][0]["transcripts"][0]["messages"])
    ],
    metadata=data["agent_runs"][0]["metadata"]
)

# Ingest
client.add_agent_runs(collection_id, [agent_run])

print(f"✅ Ingested {len(data['agent_runs'][0]['transcripts'][0]['messages'])} messages to Docent!")
print(f"🔗 View at: https://docent.transluce.org")
