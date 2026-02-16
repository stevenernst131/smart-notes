"""AI integration service — currently returns mock results.

To enable real AI:
  1. pip install openai
  2. Set environment variables:
       AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
       AZURE_OPENAI_API_KEY=<key>
       AZURE_OPENAI_DEPLOYMENT=<deployment-name>
  3. Uncomment the real implementation below and remove the mock.
"""

from __future__ import annotations

import os
from enum import Enum


class AIAction(str, Enum):
    SUMMARIZE = "summarize"
    ACTION_ITEMS = "action_items"
    SENTIMENT = "sentiment"


_MOCK_RESPONSES = {
    AIAction.SUMMARIZE: "This is a mock summary. Enable AI integration for real results.",
    AIAction.ACTION_ITEMS: "• Mock action item 1\n• Mock action item 2\n• Mock action item 3",
    AIAction.SENTIMENT: "Sentiment: Neutral (mock). Enable AI integration for real analysis.",
}


def is_ai_enabled() -> bool:
    return bool(os.getenv("AZURE_OPENAI_ENDPOINT") and os.getenv("AZURE_OPENAI_API_KEY"))


async def run_ai_action(action: AIAction, content: str) -> str:
    """Run an AI action on the given content.

    Returns mock data unless Azure OpenAI env vars are configured.
    """
    if not is_ai_enabled():
        return _MOCK_RESPONSES[action]

    # ── Real implementation (uncomment when ready) ───────────────────────
    # from openai import AsyncAzureOpenAI
    #
    # client = AsyncAzureOpenAI(
    #     azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    #     api_key=os.environ["AZURE_OPENAI_API_KEY"],
    #     api_version="2024-02-15-preview",
    # )
    #
    # prompts = {
    #     AIAction.SUMMARIZE: f"Summarize the following note concisely:\n\n{content}",
    #     AIAction.ACTION_ITEMS: f"Extract action items from the following note as a bullet list:\n\n{content}",
    #     AIAction.SENTIMENT: f"Analyze the sentiment of the following note. Reply with the sentiment and a one-sentence explanation:\n\n{content}",
    # }
    #
    # resp = await client.chat.completions.create(
    #     model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    #     messages=[{"role": "user", "content": prompts[action]}],
    #     max_tokens=512,
    # )
    # return resp.choices[0].message.content or ""

    return _MOCK_RESPONSES[action]
