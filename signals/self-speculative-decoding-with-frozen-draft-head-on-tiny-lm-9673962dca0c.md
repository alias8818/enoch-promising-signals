# Self-Speculative Decoding with Frozen Draft Head on Tiny LM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-with-frozen-draft-head-on-tiny-lm-9673962dca0c`
Run ID: `self-speculative-decoding-with-frozen-draft-head-on-tiny-lm-9673962dca0c-20260609T181901402903+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ca73369961ca

## What looked useful

Frozen draft-head self-speculation reached modeled speedups of 1.24x and 1.29x in two seeds, but fell to 0.71x in a third similar-loss seed; aggregate mean was 1.08x with high variance.

## Boundaries and scale limits

Three tiny char-level seeds, 400 training steps, one draft layer, gamma=4, no KV-cache wall-clock benchmark, no subword/GPT-2-small-class validation.

## Claim scope

On a 4-layer char-level Tiny Shakespeare LM, a frozen layer-2 draft head can sometimes produce high greedy self-speculative acceptance, but the benefit is seed-sensitive and only proxy-speed-measured.

## Why it stopped

No-paper mixed useful signal: the local proxy result shows possible mechanism support but not robust practical speedup.

## Recommended next action

Run a bounded layer/gamma sweep with actual KV-cache wall-clock decoding on saved tiny models before considering a larger token-level model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer and gamma sweep for frozen-head self-speculation with real decoding timing
- Success threshold: Frozen-head configuration achieves at least 1.15x measured wall-clock speedup on every seed and at least 1.25x mean speedup without changing greedy output.
- Stop condition: Stop if all layer/gamma settings are below 1.0x measured speedup on any two seeds or if output equivalence fails.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-with-frozen-draft-head-on-tiny-lm-9673962dca0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
