# KV-cache importance pruning for bounded local inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-importance-pruning-for-bounded-local-inference-d2088a772494`
Run ID: `kv-cache-importance-pruning-for-bounded-local-inference-d2088a772494-20260610T080038160256+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b85f706b1f3e

## What looked useful

Attention-received importance retained more designated old anchor tokens but did not reliably reduce attention-output MSE versus recency. Plain attention-importance won 11/24 summarized conditions versus recency with average MSE improvement -0.075%; the recent-floor variant won 9/24 with average improvement -0.552%. The mechanism appears insufficient as a generally reliable bounded-cache policy in this proxy.

## Boundaries and scale limits

Proxy-only evidence: no pretrained LLM, no next-token perplexity/KL, no task accuracy, no multi-layer hidden-state effects, and no production latency or allocator measurements. It should not be treated as full validation or full disproof for real model serving.

## Claim scope

Synthetic streaming causal-attention replay with sequence lengths 768 and 1536, KV budgets 32/64/128, four regimes, and four random seeds per condition. Cumulative attention-received KV importance was compared against recency, random, and an importance-plus-recent-floor variant using full-context attention output MSE as the primary target.

## Why it stopped

Early/proxy falsification: the tested importance signal improved anchor retention but failed to consistently beat recency on the direct synthetic attention-output MSE target, so the broad pruning hypothesis is not paper-ready.

## Recommended next action

Stop this run as a proxy useful-signal negative; next bounded test should implement value-aware or loss-aware KV utility inside a pretrained small decoder and measure next-token KL/perplexity at matched budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained small-decoder KV utility pruning with next-token KL
- Success threshold: At least 5% mean next-token KL or perplexity improvement over recency at one or more bounded KV budgets without worse latency than the attention-received baseline, replicated across at least three prompt sets.
- Stop condition: Stop if the proposed utility score fails to beat recency by 2% on mean next-token KL/perplexity in a smoke set or if implementation overhead makes latency worse by more than 20% at matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-importance-pruning-for-bounded-local-inference-d2088a772494`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
