# Live LLM billing and quality validation for repeated prompt anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `live-llm-billing-and-quality-validation-for-repeated-promp-f21aa2302d`
Run ID: `live-llm-billing-and-quality-validation-for-repeated-promp-f21aa2302d-20260621T225203101229+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Live LLM repeated prompt-anchor context consumption test: enoch://control-plane/projects/live-llm-repeated-prompt-anchor-context-consumption-test-be652b9c0c/runs/live-llm-repeated-prompt-anchor-context-consumption-test-be652b9c0c-20260621T212632441771+0000
- Parent run decision: Live LLM PASS transcript validation for repeated prompt-anchor features: enoch://control-plane/projects/live-llm-pass-transcript-validation-for-repeated-prompt-an-7dbd795442/runs/live-llm-pass-transcript-validation-for-repeated-prompt-an-7dbd795442-20260621T200901721971+0000

## What looked useful

Static anchors placed before dynamic payloads and at or above the 1024-token threshold produced estimated cache hits after warmup and 71.9% to 84.7% estimated input-cost savings versus dynamic-first controls under GPT-5.4 mini pricing; 768-token anchors, dynamic-first prompts, nonce-mutated prefixes, and random controls produced zero estimated cache hits. Payload integrity stayed at 100% for all strategies.

## Boundaries and scale limits

5,000 simulated prompt instances using tiktoken o200k_base and a documented-rule cache estimator. No provider usage.cached_tokens, latency, invoice/dashboard data, or live model-output quality was collected because no API key was available and key creation/reuse requires explicit confirmation.

## Claim scope

Local deterministic validation of repeated prompt-anchor cache eligibility and prompt payload integrity for OpenAI-style prompt caching rules; no live API calls or billing ledger reconciliation.

## Why it stopped

Original live LLM billing and quality validation was not closed: the worker had no API credential and could only validate the local cache-eligibility mechanism and prompt integrity estimator.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next valid deepen test is an explicitly authorized live API run that records returned cached_tokens, latency, invoice/dashboard reconciliation, and model-output quality on the same prompt matrix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Authorized live cached-token and quality reconciliation for repeated prompt anchors
- Success threshold: At least 200 live requests per cell, >=90% post-warmup cache-hit request rate for anchor-first prompts >=1024 tokens, zero cache hits for mutated-prefix controls, >=40% reconciled input-cost reduction versus dynamic-first baseline, and quality within 1 percentage point of baseline.
- Stop condition: Stop if authorized credentials or billing export access are unavailable, if returned usage lacks cached_tokens, or if anchor-first live cache-hit rate remains below 50% after warmup while controls and prompt construction are verified.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-billing-and-quality-validation-for-repeated-promp-f21aa2302d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
