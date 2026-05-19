# Real-text storage-matched residual-channel binary MLP sweep

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `real-text-storage-matched-residual-channel-binary-mlp-swee-8c0ef44583`
Run ID: `real-text-storage-matched-residual-channel-binary-mlp-swee-8c0ef44583-20260516T153502472821+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Real-text storage-matched residual-channel binary MLP sweep: internal_generated:real-text-storage-matched-residual-channel-binary-mlp-swee-8c0ef44583

## What looked useful

Residual fp16 channels substantially improve binary MLP validation loss versus same-width pure binary ablations, but all tested residual binary variants remain worse than storage-matched dense MLP baselines.

## Boundaries and scale limits

Small character MLP only; not a Transformer, GPT-2-small-class model, full-corpus language model, learned selector, post-training LLM quantizer, or fused packed inference implementation.

## Claim scope

Three-seed real-text character-level MLP sweep on Tiny Shakespeare comparing static residual-channel binary hidden-layer MLPs against dense fp16-storage MLP baselines at matched stored bytes.

## Why it stopped

Tier 2 fixed-seed real-text sweep found every residual-channel binary MLP worse than the matched dense baseline; best binary residual loss was 2.1307 versus matched dense 2.1162, and closest delta was still +0.0055 worse.

## Recommended next action

Stop this branch as a no-paper result: the direct real-text storage-matched MLP threshold was not met, although the residual-channel repair mechanism was observed.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-text-storage-matched-residual-channel-binary-mlp-swee-8c0ef44583`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
