# Secrets Hygiene Demo

A defensive cybersecurity repository for demonstrating why credentials and configuration secrets should never be committed to source control.

## Important Notice

This repository should not contain real credentials, API keys, tokens, passwords, private keys, or production configuration. Any examples should be fake placeholders used only for education.

## Purpose

The goal of this project is to show secure handling of sensitive configuration in a professional development workflow.

## Topics Covered

- Why secrets do not belong in Git history
- Using environment variables for local configuration
- Keeping `.env` files out of source control
- Rotating exposed credentials
- Using secret-scanning tools before pushing code

## Recommended Safe Structure

```text
.env.example      # fake placeholder values only
.gitignore        # excludes .env and local secrets
README.md         # setup and security guidance
```

## Example `.env.example`

```text
APP_ENV=development
API_BASE_URL=https://example.invalid
API_TOKEN=replace_me_with_a_real_token_locally
```

## Professional Security Checklist

- Never commit real passwords or tokens.
- Add `.env` and private key files to `.gitignore`.
- Use GitHub secret scanning where available.
- Rotate any secret that was ever committed publicly.
- Document setup using safe placeholder values.

## Portfolio Note

Employers care about secure habits. This repo is framed as a defensive example of secrets management and responsible engineering.
