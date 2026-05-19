# CPU-Ngram Context Draft Decoding

Status: `useful_signal`
Project ID: `cpu-ngram-context-draft-decoding-cd3d09a0093d`
Run ID: `cpu-ngram-context-draft-decoding-cd3d09a0093d-20260515T082508067568+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bbda3d5e5c31

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy early falsification for a broad CPU n-gram draft-decoding claim: ordinary prose only reached 0.048-0.086 accepted tokens per position at min_n=4, while positive code/template results were not validated with a real target-model verifier.

## Recommended next action

Stop this run as a proxy/no-paper result; run a bounded direct serving follow-up only for code/editing workloads where accepted-token headroom was observed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Serving Test of CPU N-gram Drafting for Code Contexts
- Success threshold: At least 1.25x wall-clock throughput improvement over no-draft baseline on code/editing prompts, with p95 latency not worse by more than 5% and no quality regression in deterministic replay checks.
- Stop condition: Stop if mean accepted draft tokens per verifier step is below 1.0 or measured wall-clock throughput improvement is below 1.10x after CPU and scheduler overhead.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-ngram-context-draft-decoding-cd3d09a0093d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
