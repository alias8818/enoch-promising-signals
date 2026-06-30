# SpecDecomp-Q: Speculative Decoding with 1-Bit Draft and Residual Channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `specdecomp-q-speculative-decoding-with-1-bit-draft-and-residual-channel-88886daa6ee8`
Run ID: `specdecomp-q-speculative-decoding-with-1-bit-draft-and-residual-channel-88886daa6ee8-20260628T151311935588+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c84415f6acd

## What looked useful

Plain 1-bit draft acceptance alpha averaged 0.202769, while oracle top-64 residual correction reached 0.986299, close to int8 at 0.987575. The mechanism is worth testing only if the residual channel can be predicted cheaply without target-logit oracle access.

## Boundaries and scale limits

No trained transformer, no non-oracle residual predictor, no GPU kernel, no serving latency measurement, vocab limited to 4096 synthetic logits and 512 contexts per seed.

## Claim scope

Synthetic logit-decomposition proxy with 5 fixed seeds shows naive 1-bit draft logits are not useful for speculative decoding, but oracle sparse residual correction of high-mass logits can recover near-int8 acceptance.

## Why it stopped

No-paper closure: current evidence is a synthetic oracle-residual proxy, useful for mechanism triage but insufficient for a deployable SpecDecomp-Q claim.

## Recommended next action

Run a bounded direct follow-up on a tiny trained transformer with a learned or cheap residual predictor and compare accepted tokens/sec against standard speculative decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle residual predictor for 1-bit speculative draft
- Success threshold: On a held-out decode set, non-oracle residual top-k correction reaches mean acceptance alpha >= 0.90 and accepted tokens/sec at least 1.25x over the best practical baseline at matched quality assumptions.
- Stop condition: Stop if non-oracle residual alpha remains below 0.75 or residual compute/bandwidth removes any accepted tokens/sec gain versus int8 or small dense draft baselines.

## Evidence references

- Artifact root: `<local-path>/projects/specdecomp-q-speculative-decoding-with-1-bit-draft-and-residual-channel-88886daa6ee8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
