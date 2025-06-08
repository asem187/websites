# AI Website Builders Knowledge Base

This repository collects notes about open-source AI-assisted website builders and the frameworks they commonly use. We'll continue to research these tools and determine which ones to use for building multiple websites.

## Open-source AI Builders

- **AI-Driven Website Generator** ([thewebalchemist/ai-builder](https://github.com/thewebalchemist/ai-builder))
  - Uses GPT-3 to generate HTML, CSS, and JavaScript for landing pages.
  - Styling is handled with Tailwind CSS.

- **PythaPress (AI Visual Website Builder)** ([Pythagora-io/ai-visual-website-builder](https://github.com/Pythagora-io/ai-visual-website-builder))
  - Node.js backend with Express.
  - Stores data in MongoDB via Mongoose.
  - Uses EJS for templating and Bootstrap with jQuery on the frontend.
  - Integrates an LLM to create, edit, and preview website sections in real time.

## Common Frameworks

Even proprietary AI website builders often rely on well-known open-source frameworks and tools such as:

- **React** (including frameworks like Next.js and Gatsby)
- **Svelte** (and SvelteKit)
- **Vue.js** (with Nuxt.js)
- Static site generators like **Hugo** and **Jekyll**
- CSS frameworks such as **Tailwind CSS**, **Bootstrap**, and **Bulma**

## Multi-Agent Link Chain Concept

To address gaps in accessibility, customization, and performance, we propose a multi-agent workflow that orchestrates different tasks when generating a website:

1. **Planner Agent** – outlines the page layout and required components.
2. **Content Agent** – writes copy and media prompts for each section.
3. **Design Agent** – produces accessible HTML/CSS based on the content.
4. **SEO Agent** – optimizes markup and metadata for search engines.
5. **Build Agent** – assembles the result into a deployable site.

A production-grade implementation of this workflow is available in [`multi_agent/link_chain.py`](multi_agent/link_chain.py). The script leverages **LangChain** with OpenAI's API to run each agent, includes logging, and shows how to adapt the code for OpenAI's official multi-agent API (available under `openai.beta`).

## Example Sites

The `sites/` directory contains sample websites built to demonstrate this workflow:

- **`sites/portfolio/`** – A simple portfolio page styled with Tailwind CSS.
- **`sites/blog/`** – A basic blog layout using Bootstrap.
- **`sites/landing/`** – A landing page example built with the Bulma framework.

Run `python multi_agent/link_chain.py "<topic>" --output sites/<name>` to generate additional sites with the multi-agent script. (An OpenAI API key is required.)

## Next Steps

1. **Additional Research**: Explore more open-source projects and frameworks that support AI-driven site building.
2. **Project Structure**: Set up directories for each planned website to keep their sources organized.
3. **Evaluation**: Compare features, community support, and flexibility to decide which tools we should incorporate.
4. **Prototype**: Expand the multi-agent script to use real LLM calls and integrate front-end frameworks (e.g., React or Svelte) for richer sites.
5. **Coordination**: Assign each segment in [SEGMENTS.md](SEGMENTS.md) to a dedicated branch and merge via pull request so all bots work toward a unified goal.
6. **Branch Setup**: Follow [BRANCHING.md](BRANCHING.md) for naming conventions and commands to create branches for each bot.

This README serves as our knowledge base and planning document as we gather information and build out multiple websites.

See [MARKET_READY_TASKS.md](MARKET_READY_TASKS.md) for the roadmap to make this project market-ready using ChatGPT Codex.
See [SEGMENTS.md](SEGMENTS.md) for the ten-segment implementation plan.
