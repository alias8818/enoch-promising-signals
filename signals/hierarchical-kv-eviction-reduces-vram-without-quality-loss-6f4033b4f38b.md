# Hierarchical KV Eviction Reduces VRAM Without Quality Loss

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-kv-eviction-reduces-vram-without-quality-loss-6f4033b4f38b`
Run ID: `hierarchical-kv-eviction-reduces-vram-without-quality-loss-6f4033b4f38b-20260604T103641890600+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/05a6194bbd96

## What looked useful

Hierarchical attention-anchor eviction was much stronger than a same-budget sliding window. At 128 retained tokens, distilgpt2 delta NLL was 0.007631 with 0.999507 argmax agreement, and gpt2 delta NLL was 0.000175 with 0.997537 agreement, while analytic KV bytes dropped from full-cache 255-token storage to 128-token storage. At 64 retained tokens, distilgpt2 hierarchical eviction had delta NLL 1.465061, so the broad no-quality-loss claim is not budget-independent.

## Boundaries and scale limits

Only GPT-2-family models, batch size 1, local repeated passages, max 256 tokens, and analytic KV-cache memory were tested. No natural long-context benchmark, serving throughput benchmark, allocator-level VRAM measurement, instruction-following task, or larger model was evaluated.

## Claim scope

On small repeated-passage autoregressive scoring with distilgpt2 and gpt2 up to 256 tokens, attention-anchor hierarchical KV eviction can retain 128 of 255 cache tokens and cut analytic KV-cache bytes by about half while staying near full-cache NLL and argmax predictions; the same approach at 64 retained tokens still degrades quality substantially.

## Why it stopped

Bounded local evidence supports the mechanism at a 128-token cache budget but also shows quality loss at a 64-token budget; the result is not broad or robust enough for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on natural long-context datasets with random-anchor controls and direct allocator telemetry before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural Long-Context Validation of Attention-Anchor KV Eviction
- Success threshold: At a retained KV budget of 50% or less, attention-anchor eviction has delta NLL <= 0.02 or task accuracy drop <= 1 percentage point versus full cache, beats sliding and random-anchor controls by a meaningful margin, and shows measured KV/device memory reduction.
- Stop condition: Stop if attention-anchor eviction exceeds delta NLL 0.1 or task accuracy drop 3 percentage points at all budgets that reduce KV by at least 25%, or if it fails to beat random anchors.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-kv-eviction-reduces-vram-without-quality-loss-6f4033b4f38b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
