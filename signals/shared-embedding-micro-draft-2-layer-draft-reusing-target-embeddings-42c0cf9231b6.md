# Shared-Embedding Micro-Draft: 2-Layer Draft Reusing Target Embeddings

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `shared-embedding-micro-draft-2-layer-draft-reusing-target-embeddings-42c0cf9231b6`
Run ID: `shared-embedding-micro-draft-2-layer-draft-reusing-target-embeddings-42c0cf9231b6-20260529T235751141242+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/aa1256092b70

## What looked useful

The two-layer draft architecture learned useful context above a bigram baseline, but target-like frozen embedding reuse was not robust: shared-minus-random top-1 averaged -0.0048 across full seeds, while learned embeddings averaged +0.0124 top-1 over shared. Reuse saved only 2,080 trainable parameters at this toy scale.

## Boundaries and scale limits

The run used character-level text, PPMI-SVD co-occurrence embeddings, 8-token contexts, three random seeds, and proxy top-1 accuracy rather than a pretrained Transformer target, target tokenizer, or real speculative decoding acceptance/latency.

## Claim scope

In a bounded NumPy character-level next-token proxy, a two-hidden-layer draft reusing a frozen PPMI-SVD target-like embedding table did not show a stable quality advantage over a frozen random embedding control and remained below a learned-embedding control, despite reducing incremental trainable parameters.

## Why it stopped

Calibrated replicated proxy evidence did not support a robust reused-embedding draft advantage; this is not a full validation or full falsification of real Transformer-target reuse.

## Recommended next action

Stop this run as a bounded proxy early falsification; only revisit with actual pretrained Transformer target embeddings and real speculative decoding acceptance metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real target-embedding reuse for a GPT-2-small-class draft
- Success threshold: Shared-embedding draft is within 1 percentage point of learned-embedding draft acceptance and at least 3 percentage points above frozen-random control, while reducing incremental draft parameters or memory by a practically meaningful amount.
- Stop condition: Stop if shared embeddings fail to beat frozen-random control by at least 1 percentage point in acceptance after a calibrated small-target run, or if learned embeddings remain more than 2 percentage points better with negligible memory savings.

## Evidence references

- Artifact root: `<local-path>/projects/shared-embedding-micro-draft-2-layer-draft-reusing-target-embeddings-42c0cf9231b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
