# 1-Bit Weight Training From Scratch

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-weight-training-from-scratch-a639e452b12b`
Run ID: `1-bit-weight-training-from-scratch-a639e452b12b-20260522T134204658304+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/579f753113a8

## What looked useful

Binary-STE validation loss averaged 2.2817 versus 2.4844 for frozen-sign binary control and 2.1525 for dense. Mean binary sign flip fraction was 0.1422, indicating trainable binary signs contributed to learning. The result supports the mechanism but not dense parity.

## Boundaries and scale limits

Small character LM only; dense embeddings, layer norms, output head, and latent real-valued weights/scales remain; no GPT-2-small-class run, no long schedule, no fully binarized model, no bit-packed kernel validation.

## Claim scope

In a 821,760-parameter character-level Tiny Shakespeare transformer, replacing attention/MLP linear layers with 1-bit sign forward weights trained by STE learns from scratch and beats a frozen-sign binary control over 600 steps and three seeds, but remains worse than a dense linear baseline.

## Why it stopped

Bounded evidence supports 1-bit STE learning from scratch in a small proxy, but the binary model is consistently behind dense and the evidence is not full-scale or paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next local deepen test is a GPT-2-small-class or medium token-LM comparison only if a new autonomous budget is assigned.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Token-LM 1-Bit STE Versus Dense Baseline
- Success threshold: Binary-STE closes at least 75% of the dense-to-frozen validation loss gap and is within 5% relative perplexity of dense after the planned token budget, with nonzero persistent sign flips.
- Stop condition: Stop early if binary-STE fails to beat frozen-sign by at least 25% of the dense-to-frozen gap after 20% of the training budget or if dense/binary losses diverge unrecoverably.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weight-training-from-scratch-a639e452b12b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
