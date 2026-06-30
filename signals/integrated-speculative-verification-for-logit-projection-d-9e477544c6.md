# Integrated speculative verification for logit-projection drafts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `integrated-speculative-verification-for-logit-projection-d-9e477544c6`
Run ID: `integrated-speculative-verification-for-logit-projection-d-9e477544c6-20260620T062131068495+0000`

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

- Parent run decision: Logit-cache projection drafting from recent decoding steps: enoch://control-plane/projects/logit-cache-projection-drafting-from-recent-decoding-steps-9eb07091775f/runs/logit-cache-projection-drafting-from-recent-decoding-steps-9eb07091775f-20260620T053554497122+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1ff5a6bb3738

## What looked useful

Layer-5 intermediate projection reached 45.9% corpus top-1 match and 34.7% proposed-token acceptance, but only 1.36 accepted tokens per 4-token block and an optimistic layer-cost speed estimate of 0.439x baseline. The mechanism is real but ungated naive drafting is not viable in this controlled test.

## Boundaries and scale limits

Small pretrained model, short handcrafted prompt/corpus set, greedy decoding only, idealized partial-forward cost model, no trained heads, no confidence gating, no wall-clock fused implementation.

## Claim scope

On distilgpt2 with 8 prompts and exact greedy block verification, naive intermediate-layer logit-projection drafts show depth-correlated agreement but do not reach cost-adjusted speedup over target-only greedy decoding.

## Why it stopped

Controlled small direct test supports only a weak mechanism signal and falsifies practical viability for naive ungated intermediate logit-projection drafts under an optimistic cost model; this is not full-scale validation.

## Recommended next action

Stop this ungated logit-projection draft variant as no-paper; if continuing, run a bounded confidence-gated or trained-head follow-up that must beat 1.05x cost-adjusted speedup on the same exact greedy verification protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-gated logit-projection drafts for exact greedy self-verification
- Success threshold: Cost-adjusted speedup > 1.05 with exact target greedy equivalence and zero-accept blocks below 35% of verified blocks.
- Stop condition: Stop if the best pre-registered gate has cost-adjusted speedup <= 1.0 or accepts fewer than 1.5 tokens per verified block.

## Evidence references

- Artifact root: `<local-path>/projects/integrated-speculative-verification-for-logit-projection-d-9e477544c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
