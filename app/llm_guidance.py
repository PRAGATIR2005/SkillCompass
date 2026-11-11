import requests


OLLAMA_API_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "llama3.2:3b"


def generate_personalized_guidance(
    stage_name,
    recommendation,
    feature_scores,
    probabilities=None,
):
    """
    Generate personalized career guidance using the local Ollama LLM.

    The existing ML model remains responsible for the prediction.
    The LLM explains the prediction using the supplied assessment data.
    """

    scores_text = "\n".join(
        f"- {feature.replace('_', ' ').title()}: "
        f"{float(score):.2f}/9 (assessment response average)"
        for feature, score in feature_scores.items()
    )
    

    if probabilities:
        probabilities_text = "\n".join(
            f"- {label}: {float(probability) * 100:.2f}%"
            for label, probability in probabilities.items()
        )
    else:
        probabilities_text = "Not provided."

    prompt = f"""
You are SkillCompass, an educational and career guidance assistant.

Explain the student's existing machine-learning recommendation using
only the assessment information supplied below.

Assessment stage:
{stage_name}

ML-predicted pathway:
{recommendation}

Student feature scores:
{scores_text}

Model probabilities:
{probabilities_text}

Write the response with these sections:

1. Why this pathway may be worth exploring
2. Potential strengths indicated by the assessment
3. Areas the student could explore or develop
4. Three practical next steps

Important rules:
- Do not change or replace the ML-predicted pathway.
- Refer only to scores and facts provided in the prompt.
- Do not claim that an assessment score proves a skill or guarantees success.
- Do not invent student background information.
- Do not invent course URLs, textbook titles, or learning resources.
- Explain that the recommendation is guidance, not a definitive decision.
- Use clear, encouraging language appropriate for students.
- Assessment feature scores are averages on a 1–9 response scale.
- Do not interpret a high score as proof of ability, experience, or professional expertise.
- Distinguish stated interests and preferences from demonstrated skills.
"""

    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": OLLAMA_MODEL,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                "stream": False,
                "options": {
                    "temperature": 0.3,
                },
            },
            timeout=120,
        )

        response.raise_for_status()

        result = response.json()

        return result["message"]["content"]

    except requests.exceptions.Timeout:
        return (
            "The AI guidance service took too long to respond. "
            "Please try again."
        )

    except requests.exceptions.RequestException as exc:
        return (
            "AI guidance is temporarily unavailable. "
            "Check that Ollama is running and try again.\n\n"
            f"Technical details: {exc}"
        )

    except (KeyError, ValueError):
        return "The AI service returned an unexpected response."