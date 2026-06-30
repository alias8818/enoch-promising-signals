# Early-Exit Decoding as No-Speculation Baseline

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-decoding-as-no-speculation-baseline-19681b008860`
Run ID: `early-exit-decoding-as-no-speculation-baseline-19681b008860-20260609T170016250662+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ef764dcfdc55

## What looked useful

Intermediate GPT-2 layers were often confident but wrong relative to the final layer. On gpt2, the best non-final layer agreement was 70.0% at layer 11; confidence policies saving 25.8% to 65.3% estimated layer compute still had 54.5% to 57.1% accepted-token error under strict/common gates.

## Boundaries and scale limits

Small prompt set, one-step greedy agreement only, no trained auxiliary exits, no physical mid-forward serving latency, no multi-token generation-quality evaluation, no modern larger-LM validation.

## Claim scope

Naive one-step no-speculation early-exit decoding using the shared LM head on intermediate hidden states of pretrained distilgpt2 and gpt2 is not viable as a greedy-token preserving baseline on the tested 30 short prompts.

## Why it stopped

Proxy early falsification rather than full validation: one-step GPT-2 evidence shows the naive shared-LM-head confidence gate is too miscalibrated for no-speculation token emission.

## Recommended next action

Stop this naive baseline as no-paper evidence; the next bounded test should train or calibrate auxiliary exit heads before reconsidering early-exit decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Auxiliary Heads for GPT-2 Early-Exit Decoding
- Success threshold: At least 20% measured decode latency reduction with less than 5% accepted-token error and no material degradation in multi-token generation quality on the held-out set.
- Stop condition: Stop if calibrated exits cannot get accepted-token error below 10% at 10% or greater measured latency savings.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-decoding-as-no-speculation-baseline-19681b008860`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
