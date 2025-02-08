import os
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key="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")
prompt = """
Please classify the following text as either an event or non-event. Return '1' for event and '0' for non-event.

The event should meet the following criteria:
- The text describes an event (e.g., a specific event name, date, and description)
- The event can relate to fields such as computer science, biology, history, sports, conferences, workshops, volunteer activities, academic or non-academic clubs, universities, or organizations.

Here is the description of the event (or non-event):

{event_description}

Please return '1' for event and '0' for non-event.
"""

# Example event descriptions to test
non_event_description = """
Photo by GDG Algiers on January 07, 2025. Peut être une image de 1 personne, affiche et texte qui dit ’Techweek Writing Your First Android pp: Tools, Frameworks, and Best Practices Anis Lanad Kotlin Android Developer Wednesday, January 8th at 8:00 PM on andour.DiscardComunityServer our Discord Community Server GDG Algiers’.', 
"""

# Make the API call to generate a response
response = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt.format(event_description=non_event_description)}],
    model="llama-3.3-70b-versatile",
)

# Print the generated response
print(response.choices[0].message.content)