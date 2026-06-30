# Throttled multi-process transformer test for stale 1-bit Adam sync

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `throttled-multi-process-transformer-test-for-stale-1-bit-a-b5cffe4b8b`
Run ID: `throttled-multi-process-transformer-test-for-stale-1-bit-a-b5cffe4b8b-20260526T192501369744+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Stale-sync home cluster with 1-bit Adam: enoch://control-plane/projects/stale-sync-home-cluster-with-1-bit-adam-df10759c3542/runs/stale-sync-home-cluster-with-1-bit-adam-df10759c3542-20260525T114541011239+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/625d0a40f048

## What looked useful

Full-sync Adam reached final validation loss 0.04209 using 67.34 MiB payload. 1-bit every step used 3.13% of payload but final loss was 0.39960, 9.49x baseline. Stale 1-bit sync every 4 and 8 steps used 0.78% and 0.39% of payload but final losses were 10.12x and 18.25x baseline.

## Boundaries and scale limits

Single node, CPU-only, synthetic deterministic next-token data, 2 workers, 80 optimizer steps, d_model 64, 2 transformer layers. Not a real networked distributed training stack, not GPT-2-small scale, and not tuned for production 1-bit Adam.

## Claim scope

In a two-worker CPU multiprocessing tiny-transformer language-model test with central Adam updates, stale/throttled 1-bit gradient synchronization did not meet the predeclared within-10%-of-full-sync validation-loss threshold despite large payload reductions.

## Why it stopped

Direct Tier 1 small transformer test falsified the stated quality threshold: all 1-bit variants were far above the allowed 1.10x validation-loss ratio versus full-sync Adam, although payload reductions were large.

## Recommended next action

Stop this follow-up as a no-paper useful negative signal; do not escalate stale 1-bit Adam without first showing a controlled same-distribution run within the 1.10x loss threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/throttled-multi-process-transformer-test-for-stale-1-bit-a-b5cffe4b8b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
