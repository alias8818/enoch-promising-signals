# Quantized Residual Connections for Agent Memory Architecture

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-residual-connections-for-agent-memory-architecture-f99f05b6b1be`
Run ID: `quantized-residual-connections-for-agent-memory-architecture-f99f05b6b1be-20260613T212311999210+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fdc72ec0d6bc

## What looked useful

Residual-update quantization is more robust than quantizing the whole memory state after every write in this proxy. A 4-bit residual update gave an 8x residual-update representation reduction with small recall loss, while 4-bit state quantization caused large recall drops. Error feedback recovered nearly all fp32 recall but changes the memory/resource tradeoff.

## Boundaries and scale limits

This run did not test end-to-end LLM agent memory, learned policies, human-facing tasks, multi-session persistence, or large model integration. Error-feedback variants keep a full-precision error accumulator during writes, so the strongest result supports update bandwidth/log compression rather than total working-memory compression.

## Claim scope

In a synthetic linear associative-recall proxy with random key-value writes, quantizing residual memory updates can preserve fp32 recall while reducing residual-update representation size; 4-bit residual updates stayed within 0.7 to 2.2 percentage points of fp32 across 64, 128, and 256 item capacities, and error-feedback residual quantization matched fp32 within about 1.1 percentage points even at 1 bit.

## Why it stopped

Proxy-only closure: the synthetic associative-recall mechanism was supported, but direct agent-memory evidence is required before any paper-positive claim.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next, run a bounded learned-agent memory test that applies residual-update quantization during training and evaluation against fp32 and qstate controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Agent Memory Residual-Update Quantization
- Success threshold: qres4 or qres4_ef achieves at least 98% of fp32 task success with at least 8x residual-update representation reduction, while qstate4 remains meaningfully worse or more resource-expensive.
- Stop condition: Stop if qres4 and qres4_ef fall below 95% of fp32 task success in two independent seeds or if update compression disappears once accounting for required error/state storage.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-residual-connections-for-agent-memory-architecture-f99f05b6b1be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
