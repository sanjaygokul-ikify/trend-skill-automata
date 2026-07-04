# Contributing to Skill Automata

## Development Setup
1. `git clone https://github.com/your-org/skill-automata`
2. `make dev-venv`
3. `poetry install --with dev`

## Architecture Documentation
Please update docs/rfcs when changing core components. Follow the Mermaid convention for diagrams.

## Code Quality
- 80%+ test coverage required
- Type hints enforced
- Use pydantic for all data models
- Memory usage tracking in benchmarks

## Review Process
All PRs must:
- Include performance metrics
- Contain at least one architectural RFC
- Pass all integration tests
