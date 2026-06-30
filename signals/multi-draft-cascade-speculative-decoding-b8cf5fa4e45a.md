# Multi-Draft Cascade Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-draft-cascade-speculative-decoding-b8cf5fa4e45a`
Run ID: `multi-draft-cascade-speculative-decoding-b8cf5fa4e45a-20260525T172051029692+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/aef8ea46c8ed

## What looked useful

Across 3,960 reduced-sweep scenarios, cascade beat the best single-draft baseline in 17.27% of cases, with median cascade/best-single throughput 0.868 and best observed ratio 1.529. Win rate rose to 48.0% when medium sequential draft cost was 0.24, but was 0.0% when it was 0.04.

## Boundaries and scale limits

No real transformer models, prompts, tokenizer behavior, KV-cache effects, GPU kernels, batching overheads, or memory-pressure measurements were tested. The result maps proxy regimes and should not be treated as end-to-end LLM-serving validation.

## Claim scope

Synthetic categorical proxy for cheap->medium->target speculative decoding under exact acceptance-overlap formulas and a favorable batched-verification latency model. Cascade wins only in a bounded regime where medium sequential draft tokens are expensive and cheap proposals are still moderately accepted by the medium verifier.

## Why it stopped

Proxy evidence is mixed: it falsifies broad superiority over the best single draft but identifies a specific favorable regime. This is not full validation and is not publication-grade.

## Recommended next action

Stop this run as no-paper proxy evidence; run a bounded real-model follow-up using tiny transformer drafts and target to test the high-medium-cost regime identified here.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Cascade Speculative Decoding Latency Test
- Success threshold: Cascade improves median tokens per second by at least 10% over the best single-draft baseline on at least 100 prompts while preserving exact target distribution semantics.
- Stop condition: Stop if cascade fails to beat the best single-draft baseline by 5% on an initial 25-prompt smoke set or if implementation overhead dominates accepted-token gains.

## Evidence references

- Artifact root: `<local-path>/projects/multi-draft-cascade-speculative-decoding-b8cf5fa4e45a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
