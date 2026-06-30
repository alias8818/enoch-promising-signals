# Exact Anchor Attention Sinks for Streaming Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-attention-sinks-for-streaming-long-context-fed5ff7ae6f1`
Run ID: `exact-anchor-attention-sinks-for-streaming-long-context-fed5ff7ae6f1-20260523T183204549170+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/613e7ca7ee3d

## What looked useful

Mean attention mass to the first 8 positions was 0.3416, confirming sink-like behavior, but anchor+recent was worse than recent-only at budgets 64 and 256 and only slightly better at budget 128 where random-old-token retention was similar. Anchor-count sweeps at budget 128 showed small improvements but did not isolate first anchors as uniquely valuable.

## Boundaries and scale limits

Single pretrained GPT-2 small model, one synthetic text distribution, <=900 token context, sparse-prefix proxy rather than live incremental KV-cache serving, and no downstream long-context benchmark.

## Claim scope

On GPT-2 small with a 900-token synthetic technical text and sparse-prefix logit-fidelity measurement, early attention-sink tokens receive substantial attention mass, but exact first-token anchors plus a recent window do not provide a robust or unique same-budget improvement over recency-only or random-old-token retention.

## Why it stopped

Proxy evidence is mixed and does not support the core exact-anchor advantage as a robust or unique cache policy; this is not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; a next bounded test should implement true streaming KV eviction on a real long-context benchmark with random-old-token and recency-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True Streaming KV Test for Exact Anchors Against Random Old-Token Controls
- Success threshold: Anchor policy improves mean KL or NLL delta by at least 5% over both recency-only and random-old-token controls at two or more budgets without reducing task/perplexity quality.
- Stop condition: Stop if anchor policies fail to beat both controls on mean KL/NLL at all tested budgets or if gains are matched by random-old-token retention.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-attention-sinks-for-streaming-long-context-fed5ff7ae6f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
