# Confidence-weighted speculative rejection without draft model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-weighted-speculative-rejection-without-draft-model-02ce9cf2653e`
Run ID: `confidence-weighted-speculative-rejection-without-draft-model-02ce9cf2653e-20260614T053700930077+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d4fd9fb89da0

## What looked useful

High confidence can identify a small safe subset of draft-free early exits, but the safe subset occurs too late in the network to provide meaningful speedup in this bounded test.

## Boundaries and scale limits

Tested only GPT-2-family checkpoints with 192 DistilGPT-2 context positions and 72 GPT-2-small context positions. Speedup is estimated from layer fractions, not measured with a custom cache-aware early-exit decoder. No large modern LLMs, human evaluation, or long generation drift tests were run.

## Claim scope

On local GPT-2-family models, confidence-thresholded intermediate-layer logits can reject many unsafe early-token predictions, but reliable acceptance appears only at penultimate layers where estimated layer-compute savings are about 1.01x.

## Why it stopped

Early/proxy falsification: direct token-level agreement tests found reliable acceptance only at near-final layers, and the resulting estimated layer-speedup was negligible rather than practically useful.

## Recommended next action

Stop this no-draft confidence-only path as a paper candidate; only revisit with a trained same-model calibration or early-exit head that can meet 95% agreement from substantially earlier layers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a same-model early-exit calibration head for draft-free speculative rejection
- Success threshold: At least 95% accepted-token agreement from no later than half depth, at least 25% accepted-token rate, and at least 1.15x measured decode throughput without a separate draft model.
- Stop condition: Stop if trained calibration cannot reach 95% accepted-token agreement at or before half depth with at least 10% accept rate on held-out prompts.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-weighted-speculative-rejection-without-draft-model-02ce9cf2653e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
