# Copyright 2025 Google Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.tools import ToolContext
from google.genai import types
from services.agent.text_service import TextService


async def generate_text(prompt: str, tool_context: "ToolContext") -> dict:
  """Generates text based on a prompt

  Args:
      prompt: The prompt to generate text from

  Returns:
      A dictionary containing the generated text and status.
  """
  text_service = TextService()
  text_response = text_service.generate_markdown_text(prompt=prompt)
  if text_response:
    await tool_context.save_artifact(
        "text.md",
        types.Part.from_text(text=text_response),
    )
    return {
        "status": "success",
        "detail": (
            "Markdown text generated successfully and stored in artifacts."
        ),
        "filename": "text.md",
    }
  else:
    return {"image": None, "status": "failure"}
