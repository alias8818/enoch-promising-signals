# Adaptive Spec-Decoding with Entropy-Gated Draft Routing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-spec-decoding-with-entropy-gated-draft-routing-7a028163fe2c`
Run ID: `adaptive-spec-decoding-with-entropy-gated-draft-routing-7a028163fe2c-20260621T232344183790+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/49b19478d320

## What looked useful

Entropy can act as a useful routing signal in the synthetic model, but the effect is modest and nearby literature already covers entropy-based draft stopping and adaptive speculative decoding. The idea merits a bounded direct tiny-model benchmark before any paper or large-scale run.

## Boundaries and scale limits

No real LLM logits, no real draft/target model pair, no GPU serving framework, no batching, no KV-cache timing, and no full speculative sampling correctness check were tested. Results are a local mechanism probe only.

## Claim scope

In a synthetic speculative-decoding cost model with token entropy correlated to draft acceptance difficulty, threshold-based entropy routing among fast, balanced, and accurate draft tiers improved mean speedup by 2.51% relative to the best fixed draft tier; an entropy-shuffle ablation reduced the gain to 0.48% with a paired confidence interval crossing zero.

## Why it stopped

No-paper closure: synthetic evidence supports a mechanism but does not provide direct LLM-serving validation or enough novelty for a publication claim.

## Recommended next action

Run a bounded direct tiny-model speculative decoding benchmark with real target/draft logits and fixed-draft plus adaptive-length controls; do not write a paper from the synthetic result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-model entropy-gated draft routing benchmark
- Success threshold: At least 3% paired wall-clock tokens/sec improvement over the best fixed draft policy with no loss of exact speculative decoding correctness and confidence interval excluding zero.
- Stop condition: Stop as negative if the entropy-routed policy fails to beat the best fixed or adaptive-length-only control by 3%, or if gains disappear under one prompt domain or sampling-temperature condition.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-spec-decoding-with-entropy-gated-draft-routing-7a028163fe2c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
