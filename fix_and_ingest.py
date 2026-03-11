#!/usr/bin/env python3
"""Fix agent roles and ingest to Docent"""
import json
from docent import Docent
from docent.data_models import AgentRun, Transcript
from docent.data_models.chat import parse_chat_message

# Read the JSON
with open("FAIENCE_DOCENT_READY.json", "r") as f:
    data = json.load(f)

# Fix all 'agent' roles to 'assistant'
for agent_run in data.get("agent_runs", []):
    for transcript in agent_run.get("transcripts", []):
        for message in transcript.get("messages", []):
            if message.get("role") == "agent":
                message["role"] = "assistant"

# Connect to Docent
api_key = "dk_T0CL1oVxSvsvRhzn_ZATrZUiqJf3e2tQCy1jwtgLvTkVC5f0PXxxFhVmblhWJVT"
client = Docent(api_key=api_key)

# Create collection
collection_id = client.create_collection(
    name=data["collection_name"],
    description=data["collection_description"]
)
print(f"✅ Created collection: {collection_id}")

# Build and add agent runs
agent_runs = []
for run_data in data["agent_runs"]:
    transcripts = []
    for transcript_data in run_data["transcripts"]:
        messages = [parse_chat_message(m) for m in transcript_data["messages"]]
        transcripts.append(Transcript(messages=messages))

    agent_run = AgentRun(
        transcripts=transcripts,
        metadata=run_data.get("metadata", {})
    )
    agent_runs.append(agent_run)

client.add_agent_runs(collection_id, agent_runs)
print(f"✅ Successfully ingested {len(agent_runs)} agent runs to Docent")
print(f"🌐 View at: https://docent.transluce.org/dashboard/{collection_id}")
