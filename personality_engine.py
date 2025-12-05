def apply_personality(base_reply,personality):
    styles = {
        "calm":(f"As a calm mentor :{base_reply}."
                f"Let's break it down slowly and look at the next steps."),
        "witty_friend":(f"Witty Friend :{base_reply}."
                        f"Honestly, that's kinda relatable"),
        "therapist":(f"Therapist-style: I hear you.{base_reply}."
                     f"What do you think is affecting you the most?")
    }
    return styles.get(personality,base_reply)
