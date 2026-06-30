# Proof-of-Work via Gradient Norm Bounds

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `proof-of-work-via-gradient-norm-bounds-e4442a5691d7`
Run ID: `proof-of-work-via-gradient-norm-bounds-e4442a5691d7-20260601T055721628157+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7c1ce4c99f51

## What looked useful

A 96-step AdamW shortcut reached lower gradient norm than the 512-step SGD reference and, when its final checkpoint was repeated, passed 100% of the SGD gradient-norm thresholds in 8/8 seeds while using a median 0.331x of SGD runtime. Norm bounds alone prove stationarity/quality, not claimed work.

## Boundaries and scale limits

Evidence is local and synthetic: 4096 examples, 64 input dimensions, 128 hidden units, 8 replicated seeds on one GB10 GPU. No large-model, real-dataset, cryptographic, or transition-bound protocol was tested.

## Claim scope

On a synthetic TinyMLP classification task, gradient-norm-only certificates can verify low-gradient checkpoints but do not prove that a claimed 512-step SGD trajectory was executed.

## Why it stopped

Proxy/local early falsification: the tested norm-only verifier accepted cheaper shortcut certificates, so the mechanism is not sound as proof of a specified amount of training work; this is not a full validation of richer proof-of-learning protocols.

## Recommended next action

Stop this norm-only PoW path as unsupported; run a bounded follow-up that adds random optimizer-transition checks and measures whether the shortcut still passes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gradient Norm Certificates with Random Transition Checks
- Success threshold: Honest SGD accepted in at least 7/8 seeds, all shortcut attacks rejected in at least 7/8 seeds, and verifier runtime remains below 0.15x honest SGD training runtime.
- Stop condition: Stop if any shortcut attack passes in more than 1/8 seeds or if verifier runtime exceeds 0.15x training runtime for the configured random-check budget.

## Evidence references

- Artifact root: `<local-path>/projects/proof-of-work-via-gradient-norm-bounds-e4442a5691d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
