from g4f import AsyncClient

from app.predictions.config import SYSTEM_PROMPT
from app.predictions.models import G4FModel


async def execute_prompt(client: AsyncClient, prompt: str, model: G4FModel, system_prompt: str = SYSTEM_PROMPT) -> str:
    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": prompt,
        }
    ]
    response = await client.chat.completions.create(
        model=model,
        messages=messages,  # pyright: ignore [reportArgumentType]
        web_search=False
    )
    return response.choices[0].message.content
