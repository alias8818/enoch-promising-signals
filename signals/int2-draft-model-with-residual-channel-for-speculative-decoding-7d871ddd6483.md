# INT2 draft model with residual channel for speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-draft-model-with-residual-channel-for-speculative-decoding-7d871ddd6483`
Run ID: `int2-draft-model-with-residual-channel-for-speculative-decoding-7d871ddd6483-20260619T041732416049+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4434a2c467db

## What looked useful

Static residual weights selected by largest weight reconstruction error reduce KL from 35.64 for plain INT2 to 9.67 at 5% residual and 8.37 at 20% residual, but mean one-step acceptance proxy remains only 0.056 at 5% residual and 0.084 at 20% residual.

## Boundaries and scale limits

Proxy-only distribution test; no trained draft, no learnable residual channel, no custom INT2/sparse kernel, no sparse index overhead accounting, no multi-token speculative decoding loop, and no end-to-end serving latency measurement.

## Claim scope

Post-training simulated INT2 quantization with a sparse exact residual weight channel on distilgpt2 over 128 WikiText-2 contexts improves KL versus plain INT2 at residual fractions of 1-20%, but does not recover useful one-step speculative target/draft overlap.

## Why it stopped

Proxy early falsification: static INT2 plus sparse residual improves KL but leaves speculative acceptance far too low, so it is not a paper-ready or deployment-worthy mechanism as tested.

## Recommended next action

Stop this static post-training variant; only pursue a bounded follow-up if the residual channel is trained or distilled and must reach at least 0.30 mean one-step overlap at <=3 effective bits/weight before any serving-kernel work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trainable residual channel for INT2 speculative draft distillation
- Success threshold: Mean one-step overlap >=0.30, p10 overlap >=0.10, and top-1 agreement >=0.15 at <=3 effective bits/weight before sparse index overhead, with improvement over plain INT2 and a bit-budget-matched control.
- Stop condition: Stop if trained residual overlap remains below 0.20 mean or 0.05 p10 after a bounded distillation run, or if effective storage exceeds an INT4 dense draft without better acceptance.

## Evidence references

- Artifact root: `<local-path>/projects/int2-draft-model-with-residual-channel-for-speculative-decoding-7d871ddd6483`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
