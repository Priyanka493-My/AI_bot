def extract_memory(messages):
    memory = {
        'preferences':[],
        'emotional_patterns':[],
        'facts':[]
    }
    for msg in messages:
        lower = msg.lower()

        # Preferences
        if "i like" in lower or 'i prefer' in lower:
            memory['preferences'].append(msg)

        # Emotional patterns
        emotions = ["stressed", "worried", "excited", "angry", "happy", "sad"]
        if any(emo in lower for emo in emotions):
            memory['emotional_patterns'].append(msg)

        # Facts worth remembering
        fact_keywords= ["i work", "my job", "i study", "i am from", "my goal"]
        if any(f in lower for f in fact_keywords):
            memory['facts'].append(msg)
    return memory
