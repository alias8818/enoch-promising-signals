# True GPT-2-small KV-cache heavy-hitter eviction on bounded retrieval generation

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `true-gpt-2-small-kv-cache-heavy-hitter-eviction-on-bounded-4f8f5f7417`
Run ID: `true-gpt-2-small-kv-cache-heavy-hitter-eviction-on-bounded-4f8f5f7417-20260527T053753229996+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Public benchmark GPT-2-small perplexity and retrieval check for heavy-hitter KV eviction: enoch://control-plane/projects/public-benchmark-gpt-2-small-perplexity-and-retrieval-chec-079beb43e0/runs/public-benchmark-gpt-2-small-perplexity-and-retrieval-chec-079beb43e0-20260524T180855818474+0000
- Parent run decision: GPT-2-small heavy-hitter KV eviction budget and retrieval robustness sweep: enoch://control-plane/projects/gpt-2-small-heavy-hitter-kv-eviction-budget-and-retrieval-fee3a3acba/runs/gpt-2-small-heavy-hitter-kv-eviction-budget-and-retrieval-fee3a3acba-20260524T185202292567+0000

## What looked useful

Heavy-hitter candidate accuracy was 0.2917/0.3333/0.3750 at 32/64/128 tokens versus corrected recency 0.1667 at all budgets and random 0.1667/0.1250/0.0833. Full cache reached 0.4167, but oracle-span retention reached only 0.1667, so the result is a bounded mechanism signal rather than a publication-grade validation.

## Boundaries and scale limits

Only 24 synthetic examples on GPT-2-small CPU inference were evaluated. The task is not a public benchmark suite, the policy is a pre-query attention-mass approximation rather than full production streaming H2O, and the oracle-span positive control underperformed despite retaining the answer span, indicating the protocol is not robust enough for paper-readiness.

## Claim scope

On a local fixed-seed synthetic 64-fact bounded retrieval next-token task with real GPT-2-small past_key_values pruning, pre-query attention-mass heavy-hitter selection outperformed corrected recency and random bounded-cache controls at 32, 64, and 128 retained fact tokens, but did not establish robust retrieval-generation viability.

## Why it stopped

Tier 4 paper-readiness threshold not met: heavy-hitter beat naive controls, but full-cache GPT-2-small accuracy was low and the oracle-span control failed, so the evidence is mixed and not robust enough for a paper-positive claim.

## Recommended next action

Stop this depth-4 branch as no-paper useful signal; do not launch another follow-up from this lineage cap unless a new controller branch explicitly changes the protocol and success threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/true-gpt-2-small-kv-cache-heavy-hitter-eviction-on-bounded-4f8f5f7417`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
