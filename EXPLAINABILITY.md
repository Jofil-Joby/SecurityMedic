## Decision and Reasoning

SecurityMedic decides whether source or configuration content contains a defined credential-like pattern. A match becomes a review finding with evidence and a remediation suggestion, not a claim of a confirmed vulnerability.

## Inputs and Data Sources

It uses readable source and configuration text from the inspected project. The current rule looks for password, secret, or API-key-like assignments using a deterministic pattern.

## Limits and Constraints

It does not replace SAST, secret-scanning platforms, threat modeling, or manual security review. False positives and secrets represented through unusual formats may occur.
