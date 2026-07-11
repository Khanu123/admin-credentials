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
- Keep only `.env.example` in the repository and load real values locally.

## Portfolio Note

Employers care about secure habits. This repo is framed as a defensive example of secrets management and responsible engineering.

## Employer Review

| Area | Evidence |
| --- | --- |
| Role relevance | Junior Cyber Security Analyst / IT Security / Secure Development |
| Main security lesson | Secrets should be kept out of Git history and loaded through safe local configuration |
| Defensive value | Shows awareness of credential exposure, `.gitignore`, environment variables, and rotation discipline |
| Safe scope | Uses placeholders only; no real credentials should ever be committed |

## How I Would Improve This in a Team

- Add a pre-commit secret scanning hook.
- Add a GitHub Actions workflow using a tool such as Gitleaks or TruffleHog.
- Document an incident response checklist for leaked credentials.
- Replace any sample local secret files with clearly fake `.example` templates only.
- Add a short developer onboarding checklist for safe local environment setup.

## Interview Talking Points

- Why committed credentials remain risky even after deletion.
- How secret rotation should work after exposure.
- Why `.env.example` is useful but `.env` should stay local.
- How GitHub secret scanning and pre-commit checks reduce accidental leaks.

## Current Code Improvements

- Removed tracked local secret-style files from the repository.
- Removed insecure default API key/database placeholder values from runtime config.
- Added secret masking before printing values.
- Added tests for config validation and secret redaction.

## Testing

```bash
python -m unittest discover -v
```
