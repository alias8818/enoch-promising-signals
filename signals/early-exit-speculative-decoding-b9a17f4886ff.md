# Early-Exit Speculative Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-speculative-decoding-b9a17f4886ff`
Run ID: `early-exit-speculative-decoding-b9a17f4886ff-20260525T183151467013+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/04773911dabc

## What looked useful

Raw intermediate logits are too misaligned with final logits to pay for their own compute: layer 11 achieved 55.6% final-token agreement at 91.7% layer cost, and earlier exits were much worse. This saves follow-up work from assuming untrained logit-lens exits are viable speculative drafts.

## Boundaries and scale limits

Single pretrained GPT-2 small model, one corpus, greedy agreement proxy, no trained exit heads, no end-to-end speculative decoding latency benchmark.

## Claim scope

For GPT-2 small on a 16,256-token WikiText-2 probe, raw/untrained intermediate-layer logits used as deterministic early-exit speculative drafts do not reach break-even acceptance under optimistic or serial verification cost bounds.

## Why it stopped

Proxy/direct early falsification: measured greedy draft acceptance for raw early exits is below break-even on GPT-2 small, so the raw variant is not worth paper-scale validation without calibrated heads.

## Recommended next action

Run one bounded deepen follow-up that trains calibrated early-exit heads or tuned lenses at layers 6-9, then require acceptance above layer fraction and measured tokens/sec above full-model greedy decoding before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Early-Exit Heads for Speculative Decoding
- Success threshold: At least one exit at or before layer 9 must exceed its layer fraction in greedy agreement by 10 percentage points and deliver at least 1.10x measured tokens/sec versus full-model greedy decoding at matched greedy outputs.
- Stop condition: Stop if trained exits fail to exceed layer-fraction break-even on held-out agreement or if measured end-to-end decoding is not faster than the full-model baseline.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-speculative-decoding-b9a17f4886ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
