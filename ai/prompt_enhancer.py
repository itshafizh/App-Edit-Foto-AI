from ai.gemini_client import client


def enhance_prompt(prompt):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
Rewrite this prompt into a professional AI image editing prompt.

Prompt:
{prompt}

Only return the improved prompt.
"""
    )

    return response.text