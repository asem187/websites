"""Multi-agent link chain using LangChain and OpenAI.

This script demonstrates how to orchestrate a planner, content, design, SEO,
and build agent. LangChain handles the prompt/response flow for each agent while
OpenAI provides the LLM backend. Use it to generate one or many websites by
specifying an output directory for each run. The examples here assume you have
the ``OPENAI_API_KEY`` environment variable set. Replace or extend the
placeholder functions if you want to experiment with OpenAI's official
multi-agent API (available under ``openai.beta``).
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, Any

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# If you want to use OpenAI's official multi-agent API, you could create
# assistants with ``openai.beta.assistants`` here. See the README for details.

@dataclass
class AgentResponse:
    content: str
    metadata: Dict[str, Any] | None = None

llm = ChatOpenAI(temperature=0)

def call_llm(prompt: str) -> str:
    """Call the OpenAI model via LangChain."""
    chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template("{prompt}"))
    return chain.run(prompt=prompt)


def planner_agent(topic: str) -> AgentResponse:
    prompt = f"Plan a website around the topic: {topic}. Include sections and layout."
    content = call_llm(prompt)
    return AgentResponse(content)


def content_agent(plan: str) -> AgentResponse:
    prompt = f"Generate page content based on this plan: {plan}"
    content = call_llm(prompt)
    return AgentResponse(content)


def design_agent(content: str) -> AgentResponse:
    prompt = (
        "Generate HTML and CSS for the following content. Use accessible "
        f"markup and mobile-first responsive design: {content}"
    )
    design = call_llm(prompt)
    return AgentResponse(design)


def seo_agent(html: str) -> AgentResponse:
    prompt = f"Improve the SEO metadata and structure for this HTML: {html}"
    optimized = call_llm(prompt)
    return AgentResponse(optimized)


def build_agent(html: str, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Website built at {file_path}")


def generate_website(topic: str, output_dir: str = "site_output") -> None:
    plan = planner_agent(topic).content
    content = content_agent(plan).content
    design = design_agent(content).content
    optimized = seo_agent(design).content
    build_agent(optimized, output_dir)

# -- Optional OpenAI Multi-Agent API demonstration ---------------------------
# The official API allows creating and coordinating multiple assistants. Below
# is a minimal example showing how you might integrate this script with that
# API. Remove the leading underscores to use once you have your API key set.
#
# def _create_assistant(name: str, instructions: str):
#     return openai.beta.assistants.create(
#         name=name,
#         instructions=instructions,
#         model="gpt-4o",
#     )
#
# def _run_multi_agent(topic: str):
#     planner = _create_assistant("Planner", "Plan website layouts")
#     content = _create_assistant("Content", "Write website copy")
#     # ...additional assistants for design and SEO
#     # Use openai.beta.threads and runs to orchestrate their conversation
#     # and fetch the final result.


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate a website via multi-agent chain")
    parser.add_argument("topic", help="Topic for the website")
    parser.add_argument("--output", default="site_output", help="Directory for generated site")
    args = parser.parse_args()

    generate_website(args.topic, args.output)
