# CPU KV-cache eviction with learned recency-frequency scoring

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-kv-cache-eviction-with-learned-recency-frequency-scoring-65c96ff328cf`
Run ID: `cpu-kv-cache-eviction-with-learned-recency-frequency-scoring-65c96ff328cf-20260605T155008466745+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0797ab292fce

## What looked useful

Learned scoring reached 0.8970 mean hit rate versus 0.8035 for the fixed recency-frequency heuristic and 0.8653 for LRU. It achieved 56.3% mean relative miss reduction versus the heuristic, won 24/24 pairs versus the heuristic, and won 19/24 pairs versus LRU.

## Boundaries and scale limits

Synthetic traces only; 3k-token traces; 4 generated regimes; 3 held-out seeds; 2 cache capacities; no real transformer traces, perplexity, generation quality, latency, memory-bandwidth, or production-serving measurements.

## Claim scope

In a bounded CPU synthetic attention-reference simulator, a per-regime learned online recency/frequency scorer improved KV retention versus a fixed recency-frequency heuristic in all 24 paired held-out conditions and improved mean hit rate versus LRU, but LRU remained competitive in high-capacity/local settings.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy mechanism evidence, not direct model-serving validation.

## Recommended next action

Run a bounded direct-trace follow-up using a small open transformer to collect attention-reference traces, then replay the same policies at matched cache budgets and compare retention plus perplexity or quality impact.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-model attention trace validation for learned KV eviction scoring
- Success threshold: Learned policy reduces miss rate or attention-mass loss by at least 10% versus LRU and fixed recency-frequency baselines on held-out real traces at two or more cache budgets, with no meaningful degradation in the chosen quality proxy.
- Stop condition: Stop if learned scoring fails to beat LRU on real held-out traces at most cache budgets or if quality proxy degradation exceeds the baseline at matched retention.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-kv-cache-eviction-with-learned-recency-frequency-scoring-65c96ff328cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
