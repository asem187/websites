"""Production-grade multi-agent pipeline using LangChain and OpenAI.

This module defines a small framework for orchestrating planner, content,
design, SEO and build agents. Each agent is represented by a dataclass with
clear instructions. LangChain handles the prompt/response flow while OpenAI
serves as the LLM backend. The pipeline writes the generated HTML to an output
folder. This script assumes the ``OPENAI_API_KEY`` environment variable is set.

The code is structured so it can be swapped out with OpenAI's official
multi-agent API. See the ``run_with_openai_beta`` example at the bottom of the
file for guidance.
"""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Dict, Any, Callable

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# ---------------------------------------------------------------------------
# Base infrastructure
# ---------------------------------------------------------------------------

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s")

llm = ChatOpenAI(temperature=0)


def call_llm(prompt: str) -> str:
    """Call the OpenAI model via LangChain with basic error handling."""
    logger.info("LLM prompt:\n%s", prompt)
    chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template("{prompt}"))
    try:
        return chain.run(prompt=prompt)
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(f"LLM call failed: {exc}") from exc


@dataclass
class Agent:
    """Simple representation of an agent with a name and template."""

    name: str
    template: str
    process: Callable[[str], str] | None = None

    def run(self, input_text: str) -> AgentResponse:
        prompt = self.template.format(input=input_text)
        content = call_llm(prompt) if self.process is None else self.process(prompt)
        return AgentResponse(content)


@dataclass
class AgentResponse:
    content: str
    metadata: Dict[str, Any] | None = None


# ---------------------------------------------------------------------------
# Agent definitions
# ---------------------------------------------------------------------------

PLANNER = Agent(
    name="Planner",
    template="Plan a website around the topic: {input}. Include sections and layout.",
)

CONTENT = Agent(
    name="Content",
    template="Generate detailed page content based on this plan: {input}",
)

DESIGN = Agent(
    name="Design",
    template=(
        "Generate HTML and CSS for the following content. "
        "Use accessible markup and responsive design: {input}"
    ),
)

SEO = Agent(
    name="SEO",
    template="Improve the SEO metadata and structure for this HTML: {input}",
)


# ---------------------------------------------------------------------------
# Pipeline orchestration
# ---------------------------------------------------------------------------

def build_site(html: str, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "index.html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    logger.info("Website built at %s", path)


def generate_website(topic: str, output_dir: str = "site_output") -> None:
    plan = PLANNER.run(topic).content
    content = CONTENT.run(plan).content
    design = DESIGN.run(content).content
    optimized = SEO.run(design).content
    build_site(optimized, output_dir)


# ---------------------------------------------------------------------------
# Optional OpenAI Multi-Agent API demonstration
# ---------------------------------------------------------------------------
# The following demonstrates how this pipeline could be replaced by
# OpenAI's official multi-agent API. Uncomment and adjust once you have an API
# key and want to experiment with the beta assistants.
#
# import openai
#
# def run_with_openai_beta(topic: str, output_dir: str = "site_output") -> None:
#     planner = openai.beta.assistants.create(
#         name="Planner", instructions="Plan website layouts", model="gpt-4o"
#     )
#     content = openai.beta.assistants.create(
#         name="Content", instructions="Write website copy", model="gpt-4o"
#     )
#     # Additional assistants would be created for design and SEO.
#     # You would then use threads and runs to orchestrate communication
#     # between these assistants and retrieve the final HTML.
#     raise NotImplementedError
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate a website via multi-agent pipeline")
    parser.add_argument("topic", help="Topic for the website")
    parser.add_argument("--output", default="site_output", help="Directory for generated site")
    args = parser.parse_args()

    generate_website(args.topic, args.output)
