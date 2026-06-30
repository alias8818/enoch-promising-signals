# Early-Exit Self-Speculative Decoding with Layer Skipping

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-self-speculative-decoding-with-layer-skipping-f499b3110293`
Run ID: `early-exit-self-speculative-decoding-with-layer-skipping-f499b3110293-20260608T224502707770+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/767958d5e25e

## What looked useful

Naive layer skipping did not satisfy the acceptance-versus-cost threshold. Across exits 2/4/6/8/10, distribution-overlap alpha ranged from 0.121 to 0.378 while layer cost fraction ranged from 0.167 to 0.833; a late exit-11 diagnostic reached alpha 0.523 but cost fraction 0.917. All optimistic gamma=4 speedup proxies were below 1.0.

## Boundaries and scale limits

Tested 6,144 next-token positions per medium/late run on GPT-2 small only. Results are proxy distribution and timing metrics, not end-to-end serving throughput, not larger modern LLMs, and not trained LayerSkip-style checkpoints.

## Claim scope

Bounded GPT-2-small/Wikitext-2 probe of raw early-exit self-speculative decoding using intermediate hidden states with the original final layer norm and LM head, without early-exit training or KV-cache generation implementation.

## Why it stopped

The bounded probe falsified the simple speedup condition alpha > exit_layer/full_layers for every tested exit, so raw layer skipping alone is not paper-worthy or practically promising under this setup.

## Recommended next action

Stop this run as a proxy early falsification of the naive raw GPT-2 early-exit approach; the concrete next bounded test is to rerun the same threshold analysis on a model trained with explicit early-exit or LayerSkip losses.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained Early-Exit Head Acceptance Threshold Test
- Success threshold: At least one exit with alpha greater than exit_layer/full_layers by 0.05 or more, top-1 agreement above 0.5 before the final layer, and an optimistic gamma=4 speedup proxy above 1.1 on at least 6,144 held-out token positions.
- Stop condition: Stop if trained/calibrated exits still have alpha less than or equal to layer fraction, or if the only positive exit is within one layer of the full model and measured partial/full latency exceeds 0.9.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculative-decoding-with-layer-skipping-f499b3110293`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
