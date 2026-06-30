# Self-distilled 50M draft model for speculative decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-distilled-50m-draft-model-for-speculative-decoding-on-gb10-4d4106b87244`
Run ID: `self-distilled-50m-draft-model-for-speculative-decoding-on-gb10-4d4106b87244-20260609T202135194531+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/de3914d62c41

## What looked useful

Layer copying alone produced very low held-out acceptance around 3%; 120 steps of self-distillation improved held-out acceptance to about 10% and target-forward reduction to about 28%, but throughput remained slower than baseline target-only decoding.

## Boundaries and scale limits

Small GPT-2 target, short generated prompts, greedy decoding, no KV-cache optimized serving path, tiny generated-text distillation corpus, 120 optimizer steps, and no validation on 7B-class or production target models.

## Claim scope

On GB10 with GPT-2-small as target and a 53.6M-parameter two-layer GPT-2 draft, copied target weights plus a 120-step local logit self-distillation probe improved held-out speculative decoding acceptance but did not produce a wall-clock speedup over target-only greedy decoding.

## Why it stopped

Early bounded GB10 evidence showed the self-distilled 50M-class draft improved acceptance but remained too inaccurate and too slow for a practical speculative decoding result; this is not a full-scale validation.

## Recommended next action

Stop this run as a bounded no-paper useful signal; the concrete next test is a KV-cache-aware follow-up with longer local distillation and a success threshold of at least 40% held-out acceptance plus wall-clock speedup over target-only decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware 50M draft distillation threshold test on GB10
- Success threshold: At least 40% held-out acceptance and at least 1.1x wall-clock throughput versus target-only decoding on the same GB10 implementation.
- Stop condition: Stop if acceptance remains below 25% after the planned local distillation budget or if speculative throughput remains below target-only throughput despite target-forward reductions.

## Evidence references

- Artifact root: `<local-path>/projects/self-distilled-50m-draft-model-for-speculative-decoding-on-gb10-4d4106b87244`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
