# Branching Guidelines

To coordinate multiple bots working on this project, create a dedicated branch for each segment described in [SEGMENTS.md](SEGMENTS.md). The recommended naming convention is `segment-X-description`, where `X` is the segment number.

## Creating a branch

1. Fetch the latest changes from `main`:
   ```bash
   git checkout main
   git pull origin main
   ```
2. Create a new branch for your segment:
   ```bash
   git checkout -b segment-1-research
   ```
3. Commit your work regularly and push the branch:
   ```bash
   git push -u origin segment-1-research
   ```
4. Open a pull request targeting `main` when the segment is complete. After review, merge and delete the branch.

## Suggested branches

- `segment-1-research` – Research & Requirements
- `segment-2-structure` – Project Structure
- `segment-3-core-pipeline` – Core Multi-Agent Pipeline
- `segment-4-templates` – Template System & Front-End Framework
- `segment-5-llm-integration` – Content Generation & LLM Integration
- `segment-6-accessibility` – Accessibility & SEO
- `segment-7-testing` – Testing & Quality Assurance
- `segment-8-deployment` – Deployment Automation
- `segment-9-examples` – Example Site Development
- `segment-10-docs` – Documentation & Final Polishing

Keep your branch up to date with `main` using `git fetch` and `git rebase` or `git merge` regularly to avoid conflicts.

