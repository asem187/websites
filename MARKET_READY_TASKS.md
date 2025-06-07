# Market-Ready Roadmap

This document outlines tasks required to turn the prototype into a commercial product using **OpenAI ChatGPT Codex** (i.e., OpenAI's code-focused models and multi-agent API).

## Latest Codex Update

The [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) list a new update dated **June 4, 2025**, which introduces connectors in beta for deep research and custom connectors via the Model Context Protocol.

## Tasks

1. **Research & Evaluation**
   - Expand the knowledge base with additional AI website builders and frameworks.
   - Compare features and pick the best tools that integrate well with ChatGPT Codex.

2. **Multi-Agent Pipeline**
   - Replace placeholders in `multi_agent/link_chain.py` with real API calls using OpenAI's multi-agent API.
   - Implement Planner, Content, Design, SEO, and Build agents that exchange messages through Codex.
   - Allow custom connectors so each agent can pull from external data sources as described in the June 4, 2025 update.

3. **Website Generation**
   - Produce accessible HTML/CSS/JS with responsive design and modern frameworks (React, Svelte, or Vue).
   - Include automated SEO metadata and structured data.
   - Provide options for dynamic components and CMS integrations.

4. **Testing & Quality Assurance**
   - Validate generated pages for WCAG accessibility and run performance checks.
   - Lint and test Python code and generated sites.

5. **Deployment Workflow**
   - Automate building and hosting multiple sites (e.g., GitHub Pages or other static hosts).
   - Document usage so a user can run the pipeline with a single command.

6. **Ongoing Improvements**
   - Monitor OpenAI release notes for further Codex updates.
   - Gather user feedback and iterate on features and design.
