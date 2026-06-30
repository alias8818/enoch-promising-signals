# Speculative Decode with 2-Bit Draft Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decode-with-2-bit-draft-residual-channels-bd5cd8b5e301`
Run ID: `speculative-decode-with-2-bit-draft-residual-channels-bd5cd8b5e301-20260529T141543409059+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/cf50c4e48289

## What looked useful

2-bit residual channels are only viable in this probe when formulated as offset-invariant log-probability or centered residuals. Raw-logit residual channels collapse acceptance because model logit offsets are not comparable. Best observed point was top-K 32 log-prob residuals: acceptance 0.8144 versus draft 0.7247, gain 0.0897 for 64 bits/context.

## Boundaries and scale limits

Distribution-level oracle residual probe only; no trained residual predictor, no multi-token speculative decoding throughput, no large-model validation, and no serving-side channel overhead measurement.

## Claim scope

On GPT-2 target versus DistilGPT-2 draft over 1024 WikiText-2 validation contexts, oracle 2-bit offset-invariant top-K residuals improve exact one-step speculative acceptance by 0.063 to 0.090, while naive raw-logit residuals are strongly harmful.

## Why it stopped

No-paper useful signal: this run used oracle residuals and exact one-step acceptance, so it supports a mechanism and a design constraint but not a deployable or publication-grade result.

## Recommended next action

Run a bounded deepen follow-up that trains a small draft-side residual-code head to predict top-K log-prob residual codes without target logits, then evaluate multi-token speculative acceptance against standard speculative decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a Draft-Side 2-Bit Log-Probability Residual Head
- Success threshold: On held-out text, predicted 2-bit log-prob residuals recover at least 50% of the oracle top-K 32 acceptance gain and improve end-to-end speculative tokens/sec by at least 5% over the same draft without residuals.
- Stop condition: Stop if predicted residual codes recover less than 25% of oracle acceptance gain or if residual-head overhead removes all measured throughput benefit.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decode-with-2-bit-draft-residual-channels-bd5cd8b5e301`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
