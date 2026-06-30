# Real-trace DFlash prefix labels for SSD-lite verification prediction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-trace-dflash-prefix-labels-for-ssd-lite-verification-4d58f0064e`
Run ID: `real-trace-dflash-prefix-labels-for-ssd-lite-verification-4d58f0064e-20260520T015907859479+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Per-token DFlash outcome labels for SSD-lite verification prediction: enoch://control-plane/projects/per-token-dflash-outcome-labels-for-ssd-lite-verification-4d769e7131/runs/per-token-dflash-outcome-labels-for-ssd-lite-verification-4d769e7131-20260520T015407832810+0000
- Parent run decision: SSD-lite outcome prediction on real DFlash verification traces: enoch://control-plane/projects/ssd-lite-outcome-prediction-on-real-dflash-verification-tr-bbe1c536e9/runs/ssd-lite-outcome-prediction-on-real-dflash-verification-tr-bbe1c536e9-20260519T233514486181+0000

## What looked useful

Token-plus-DFlash achieved AUC 0.8563, 0.8762, and 0.8999 for survival horizons >=2, >=3, and >=4 versus token-only AUC 0.6769, 0.7234, and 0.7415. Mean AUC gains over token-only were +0.1794, +0.1528, and +0.1584, and every fixed split had a positive gain. Shuffled-label controls stayed near chance.

## Boundaries and scale limits

This is a real model-generated speculative-verification stand-in, not actual DFlash diffusion decoding. It uses distilgpt2 as draft and gpt2 as target on CPU, offline prediction only, with no Qwen3-4B DFlash checkpoint, production kernel timing, online draft-length intervention, answer-quality evaluation, or broad model-family coverage.

## Claim scope

On 320 real GPT-2-family draft/target speculative verification traces drawn from local Enoch/Codex trace documents, causal DFlash-style prefix verifier labels improve SSD-lite survival prediction over token/confidence-only, position-only, and randomized-label controls across horizons 2, 3, and 4.

## Why it stopped

Tier 3 bounded local validation supports the prefix-label mechanism on real model-generated speculative traces, but the evidence is still a DFlash stand-in and offline predictor rather than actual DFlash/Qwen deployment evidence.

## Recommended next action

Instrument actual DFlash/Qwen traces with per-token causal prefix labels and rerun this locked protocol against position-only, token/confidence-only, and randomized-label controls before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual DFlash/Qwen per-token prefix-label survival prediction
- Success threshold: Mean held-out AUC improvement >= +0.05 over the strongest simple control and randomized-label control across at least five fixed splits, every split non-negative, plus no leakage finding.
- Stop condition: Stop if actual DFlash per-token traces cannot be obtained, if prefix labels require non-causal final-outcome information, or if the AUC gain over the strongest simple control is below +0.02.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-dflash-prefix-labels-for-ssd-lite-verification-4d58f0064e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
