from intent import detect_intent
from rag import retrieve_answer
from tools import mock_lead_capture

class AutoStreamAgent:
    def __init__(self):
        self.state = {
            "stage": None,
            "name": None,
            "email": None,
            "platform": None
        }

    def handle_input(self, user_input):

        # If collecting lead
        if self.state["stage"]:
            return self.handle_lead_flow(user_input)

        intent = detect_intent(user_input)

        if intent == "greeting":
            return "Hello! 👋 How can I help you with AutoStream?"

        elif intent == "pricing":
            return retrieve_answer(user_input)

        elif intent == "high_intent":
            self.state["stage"] = "name"
            return "Awesome! Let's get you started. What's your name?"

        return "I can help with plans, pricing, or getting started!"

    def handle_lead_flow(self, user_input):

        if self.state["stage"] == "name":
            self.state["name"] = user_input
            self.state["stage"] = "email"
            return "Great! What's your email?"

        elif self.state["stage"] == "email":
            self.state["email"] = user_input
            self.state["stage"] = "platform"
            return "Which platform do you create content on?"

        elif self.state["stage"] == "platform":
            self.state["platform"] = user_input

            mock_lead_capture(
                self.state["name"],
                self.state["email"],
                self.state["platform"]
            )

            self.state = {"stage": None, "name": None, "email": None, "platform": None}

            return "🎉 You're all set! Our team will contact you soon."