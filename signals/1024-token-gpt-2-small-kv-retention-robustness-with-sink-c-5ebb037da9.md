# 1024-token GPT-2-small KV retention robustness with sink-count ablations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `1024-token-gpt-2-small-kv-retention-robustness-with-sink-c-5ebb037da9`
Run ID: `1024-token-gpt-2-small-kv-retention-robustness-with-sink-c-5ebb037da9-20260603T162241395648+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Online KV-Cache Sink-vs-Heavy-Hitter Retention on GPT-2-Small-Class Long Contexts: enoch://control-plane/projects/online-kv-cache-sink-vs-heavy-hitter-retention-on-gpt-2-sm-80bd94ce4a/runs/online-kv-cache-sink-vs-heavy-hitter-retention-on-gpt-2-sm-80bd94ce4a-20260602T203903721220+0000
- Parent run decision: Compare Attention-Sink Retention Against Heavy-Hitter KV Eviction: enoch://control-plane/projects/compare-attention-sink-retention-against-heavy-hitter-kv-e-82a0b2cf5d/runs/compare-attention-sink-retention-against-heavy-hitter-kv-e-82a0b2cf5d-20260602T164000940663+0000

## What looked useful

Recent-only retention was severely degraded: delta bits/token versus full cache were 9.140, 8.635, and 6.922 for budgets 64, 128, and 256. Adding sink tokens recovered most of that gap; best tested policies recovered 86.8%, 92.2%, and 94.8% respectively, with best delta bits/token 1.204 for budget64_sink16, 0.672 for budget128_sink32, and 0.360 for budget256_sink32.

## Boundaries and scale limits

Single model family and size, one corpus, one fixed window-sampling seed, aggregate metrics without per-window confidence intervals, no downstream generation/task evaluation, no modern model replication, and no production serving-kernel validation.

## Claim scope

For pretrained GPT-2-small on 64 sampled 1024-token WikiText-103 validation windows, retaining initial sink tokens plus a recent suffix substantially improves bounded KV-cache next-token NLL versus recent-only retention at budgets 64, 128, and 256, while remaining below exact full-cache quality.

## Why it stopped

Completed the requested bounded direct GPT-2-small 1024-token KV-retention ablation; result is a useful mechanism signal but lacks the uncertainty estimates, corpus/model replication, and downstream validation needed for publication readiness.

## Recommended next action

Run a bounded replication that records per-window metrics and confidence intervals across at least two seeds and a second corpus, then decide whether the sink-retention claim is robust enough for a scoped paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replicated GPT-2-small sink-retention KV ablation with confidence intervals
- Success threshold: For every tested budget 64/128/256, the best sink policy recovers at least 80% of the recent-only NLL gap versus full cache, and the confidence interval excludes recent-only by a practically large margin on both corpora.
- Stop condition: Stop if any budget fails to recover at least 50% of the recent-only NLL gap on the second seed or second corpus, or if the API sanity check shows the current sink advantage is a cache-positioning artifact.

## Evidence references

- Artifact root: `<local-path>/projects/1024-token-gpt-2-small-kv-retention-robustness-with-sink-c-5ebb037da9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
