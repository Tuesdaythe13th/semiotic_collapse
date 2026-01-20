#!/usr/bin/env python3
"""
Ingest the faience coincidence transcript into Docent for analysis.

This session documents concerning coincidences involving:
- ASR/LM producing rare terms matching real-world events
- Voice system mapping to real acquaintances
- Unexplained transcript disappearance during red-team sessions
"""

import json
from docent import Docent
from docent.data_models import AgentRun, Transcript
from docent.data_models.chat import parse_chat_message

def main():
    # Use provided API key
    api_key = "dk_V9gStxEJ4Qkrus6f_4GbQ2RMERinSP37MOOgGrYAqRMQsCbdNP6mjnvOkiv4YMh"
    client = Docent(api_key=api_key)

    # Load the transcript JSON
    print("Loading transcript...")
    with open("faience_coincidence_transcript.json", "r") as f:
        data = json.load(f)

    # Parse messages
    print(f"Parsing {len(data['transcript']['messages'])} messages...")
    parsed_messages = []
    for msg in data['transcript']['messages']:
        # Convert to proper format - all messages should have role and content
        if msg.get('role') and msg.get('content'):
            parsed_messages.append(parse_chat_message({
                'role': msg['role'],
                'content': msg['content']
            }))

    print(f"Successfully parsed {len(parsed_messages)} messages.")

    # Create transcript
    transcript = Transcript(messages=parsed_messages)

    # Create collection
    collection_name = "FAIENCE-COINCIDENCE-2026-01-20"
    print(f"\nCreating collection: {collection_name}")

    collection_id = client.create_collection(
        name=collection_name,
        description="Analysis of concerning coincidences: voice ASR/LM producing rare terms (Egypt, faience) matching real-world museum visit, mapping to real acquaintance (Fazel), followed by related contact. Includes transcript disappearance during red-team session (second occurrence)."
    )

    print(f"✅ Created collection: {collection_id}")
    print(f"Frontend URL: https://docent.transluce.org/dashboard/{collection_id}")

    # Create agent run with metadata
    agent_run = AgentRun(
        transcripts=[transcript],
        metadata={
            "date": data['session_metadata']['date'],
            "researcher": data['session_metadata']['researcher'],
            "context": data['session_metadata']['context'],
            "model": "unknown-voice-assistant",
            "session_type": "voice-to-voice",
            "concerns": data['session_metadata']['concerns'],
            "timeline": data['timeline'],
            "key_anomalies": data['analysis_notes']['key_anomalies'],
            "proposed_mechanisms": data['analysis_notes']['proposed_mechanisms'],
            "scores": {
                "coincidence_severity": 0.95,
                "security_concern": 0.75,
                "transcript_disappearance": 1.0,
                "asr_anomaly": 0.90,
                "social_correlation": 0.85
            }
        }
    )

    # Ingest
    print("\nIngesting agent run...")
    client.add_agent_runs(collection_id, [agent_run])

    print("\n✅ Ingestion successful!")
    print(f"\nView your transcript at:")
    print(f"https://docent.transluce.org/dashboard/{collection_id}")
    print("\nKey findings documented:")
    for anomaly in data['analysis_notes']['key_anomalies']:
        print(f"  • {anomaly}")

if __name__ == "__main__":
    main()
