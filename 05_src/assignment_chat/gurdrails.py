RESTRICTED_TOPICS = ["cats", "dogs", "horoscope", "zodiac", "zodiac signs", "taylor swift"]

def check_guardrails(user_input):
    text = user_input.lower()

    # Block restricted topics
    for topic in RESTRICTED_TOPICS:
        if topic in text:
            return "Sorry, I cannot discuss that topic."

    # Prevent prompt injection
    if "system prompt" in text or "ignore previous instructions" in text:
        return "Nice try 🙂 I can't reveal or modify my instructions."

    return None