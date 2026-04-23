def detect_intent(user_input):
    text = user_input.lower()

    # Priority 1: High intent
    if any(word in text for word in ["buy", "subscribe", "try", "sign up", "start"]):
        return "high_intent"

    # Priority 2: Pricing / product queries
    elif any(word in text for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"

    # Priority 3: Greeting
    elif any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    return "general"