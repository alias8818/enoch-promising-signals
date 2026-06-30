# Hidden-state router for tiny-to-small model cascade

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `hidden-state-router-for-tiny-to-small-model-cascade-a2bd55246804`
Run ID: `hidden-state-router-for-tiny-to-small-model-cascade-a2bd55246804-20260529T060951364190+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ce92ee43bde

## What looked useful

The tiny-to-small cascade has clear recoverable headroom, but hidden-state routing did not materially outperform confidence-only routing: +0.0018 mean AUC for tiny-correctness prediction and about +/-0.0006 cascade-accuracy differences at matched small-call budgets across 3 seeds.

## Boundaries and scale limits

Not tested on natural-language data, pretrained transformers, generation tasks, GPT-2-small-class baselines, or measured serving latency. Compute cost is represented by small-model call rate and parameter ratio.

## Claim scope

Synthetic sequence-classification probe with a 7,234-parameter tiny GRU, a 178,178-parameter small GRU, and routers trained to predict tiny-model correctness from validation examples.

## Why it stopped

Early bounded falsification of the hidden-state-router advantage on a direct synthetic proxy, not a full natural-language validation.

## Recommended next action

Stop this run as a bounded no-paper result; the next useful test is a real-language pretrained-transformer cascade comparing hidden-state probes against confidence routing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained transformer hidden-state routing on real language tasks
- Success threshold: Hidden-state routing improves tiny-correctness AUC by at least 0.02 or cascade accuracy by at least 0.01 absolute at matched small-call rates on most tasks without erasing latency savings.
- Stop condition: Stop if hidden-state routing remains within 0.005 AUC and 0.003 cascade accuracy of confidence routing across two real tasks.

## Evidence references

- Artifact root: `<local-path>/projects/hidden-state-router-for-tiny-to-small-model-cascade-a2bd55246804`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
