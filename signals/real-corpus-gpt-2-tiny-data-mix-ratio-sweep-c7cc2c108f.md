# Real-corpus GPT-2-tiny data-mix ratio sweep

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-gpt-2-tiny-data-mix-ratio-sweep-c7cc2c108f`
Run ID: `real-corpus-gpt-2-tiny-data-mix-ratio-sweep-c7cc2c108f-20260620T011532425084+0000`

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

- Parent run decision: DataMix ratio sweep for GPT-2-tiny on gb10: enoch://control-plane/projects/datamix-ratio-sweep-for-gpt-2-tiny-on-gb10-b9fd866c7633/runs/datamix-ratio-sweep-for-gpt-2-tiny-on-gb10-b9fd866c7633-20260620T010135205971+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c78037a2cdbf

## What looked useful

A coarse five-ratio sweep showed interior mixes improve balanced validation but violate the AG News guardrail at high WikiText ratios; a near-endpoint refinement found 10%, 12.5%, and 15% WikiText qualify, with 15% WikiText improving balanced validation by 0.4477 nats and regressing AG News by only 0.0495 nats versus AG-only.

## Boundaries and scale limits

6.84M-parameter GPT-2-style model, 160 updates per condition, two seeds, sequence length 64, WikiText-2 and AG News only; not long-run convergence, GPT-2-small scale, broad corpus mixing, or downstream evaluation.

## Claim scope

In a Tier 1 GPT-2-tiny short-run training sweep on WikiText-2 plus AG News, near-endpoint mixtures with 10-15% WikiText improved balanced validation loss over single-corpus endpoints while keeping AG News regression within a 0.08-nat guardrail.

## Why it stopped

No-paper useful signal: the Tier 1 direct evidence supports a bounded data-mix effect, but the run is too short and too small for publication-grade claims.

## Recommended next action

Run a medium confirmation with independent endpoint initializations, at least three seeds, longer training, and a GPT-2-small-class or clearly parameter-matched model focused on the 10-20% WikiText region.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium confirmation of near-endpoint WikiText/AG News data-mix gains
- Success threshold: Best guardrailed interior ratio improves balanced validation loss by at least 0.03 nats over the best endpoint and keeps each per-corpus validation loss within 0.08 nats of the best endpoint comparison across at least three seeds.
- Stop condition: Stop if no interior ratio in 10-25% WikiText improves balanced validation by at least 0.03 nats, or if every improving interior ratio regresses AG News by more than 0.08 nats.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-gpt-2-tiny-data-mix-ratio-sweep-c7cc2c108f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
