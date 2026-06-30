# Adaptive N-gram Lookahead in a Serving Baseline

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-n-gram-lookahead-in-a-serving-baseline-fb23737fcc`
Run ID: `adaptive-n-gram-lookahead-in-a-serving-baseline-fb23737fcc-20260604T020652574055+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: N-gram KV Cache Lookahead Drafting: enoch://control-plane/projects/n-gram-kv-cache-lookahead-drafting-87467d11d8c0/runs/n-gram-kv-cache-lookahead-drafting-87467d11d8c0-20260604T001513474828+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f1841f57fa90

## What looked useful

Adaptive n-gram lookahead matched the greedy KV-cache baseline on all controlled prompts, reduced forward calls from 390 to 84 (78.46%), reached 95.78% mean draft-token acceptance, and improved warmed throughput from 725.95 to 2488.83 tokens/s (3.43x).

## Boundaries and scale limits

Single small model, six prompts, greedy decoding only, single-request GPU harness, no production server, no batching, no sampling, no larger models, and no natural workload distribution.

## Claim scope

In a small controlled greedy-decoding test on distilgpt2 with six prompts and 64 generated tokens per prompt, adaptive n-gram lookahead preserved exact baseline outputs while reducing target-model forward calls and improving measured GPU decode throughput.

## Why it stopped

Tier 1 controlled small direct test is complete and positive for the adaptive mechanism, but evidence is too narrow for paper readiness.

## Recommended next action

Run a bounded deepen follow-up on at least 100 representative prompts and two model sizes in a closer serving harness with exactness checks and latency percentiles.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Broader serving-harness validation for adaptive n-gram lookahead
- Success threshold: All outputs match baseline, target-model forward calls drop by at least 20%, and p50 latency improves by at least 15% without p95 latency regression over 5%.
- Stop condition: Stop if exactness fails, if forward-call reduction is below 10%, or if p95 latency regresses by more than 10% after warm-up on the broader prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-n-gram-lookahead-in-a-serving-baseline-fb23737fcc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
