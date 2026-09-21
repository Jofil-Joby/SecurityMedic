# SecurityMedic

> Portable agent for detecting obvious hard-coded credential patterns in source and configuration.

## What it does

SecurityMedic scans available project evidence for credential-like patterns such as passwords, secrets, or API keys embedded directly in source/configuration text. When it finds a match, it explains the observation and recommends moving secrets into appropriate secret management.

### Diagnostic fingerprint

**Pattern detection → evidence capture → security finding → safer handling**

## Why this agent is distinct

SecurityMedic is not presented as a full vulnerability scanner. Its scope is intentionally explicit: identify a high-signal class of credential exposure that can be checked deterministically.

That makes the result reproducible, explainable, and suitable for a portable agent contract.

## Evidence-first behavior

```text
Project files
    ↓
Source/config text
    ↓
Credential-pattern rule
    ↓
Observed evidence
    ↓
Recommended remediation
```

No finding is based on a claim that cannot be tied back to scanned evidence.

## Verification

The repository contains:
- OpenGAP passport metadata
- behavior and explainability contracts
- security-focused fixture data
- OpenAI, CrewAI, Claude Code, and Lyzr adapters
- automated adapter verification

The passport has been validated with OpenGAP and all four generated framework exports have been exercised successfully.

## Repository layout

```text
agent.yaml
SOUL.md
EXPLAINABILITY.md
AGENTS.md
DUTIES.md
agent.py
tools/
adapters/
tests/
```

## Safety boundary

A pattern match is a signal for review, not proof of malicious behavior. SecurityMedic intentionally recommends safer secret handling instead of making unsupported claims about the project.

## Medic family

SecurityMedic is one focused diagnostic in a portable family of engineering agents. The architecture stays consistent so agents can interoperate, while each agent owns a different evidence domain.