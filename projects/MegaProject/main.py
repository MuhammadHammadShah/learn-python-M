import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Set the first voice (or iterate through voices)
engine.setProperty('voice', voices[0].id)

# Adjustable female pitch range
female_pitch_range = (165, 255)


def speak(text, pitch=female_pitch_range[0]):
    """Speaks the given text with adjustable pitch.

    Args:
        text: The text to be spoken.
        pitch: The desired pitch (Hz) within the female range.
    """
    engine.setProperty('pitch', pitch)
    engine.say(text)
    engine.runAndWait()


# Example usage with adjustable pitch
text = "This is a test message with a female-like pitch."

# Try different pitch values within the range
speak(text, pitch=180)
speak(text, pitch=60)  # Experiment with different values
