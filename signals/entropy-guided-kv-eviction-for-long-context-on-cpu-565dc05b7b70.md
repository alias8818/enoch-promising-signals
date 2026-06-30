# Entropy-Guided KV Eviction for Long Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-guided-kv-eviction-for-long-context-on-cpu-565dc05b7b70`
Run ID: `entropy-guided-kv-eviction-for-long-context-on-cpu-565dc05b7b70-20260604T063804038985+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8ecf6cd3b5fd

## What looked useful

At 5% cache budget, entropy_mul improved H2O by 4.41% relative on distant-mass recall and 4.76% on delayed-retrieval mass in aligned traces. At 10% budget H2O saturated retrieval recall, and a high entropy-weight stress test showed large regressions when the entropy/usefulness relation was adversarial.

## Boundaries and scale limits

No real transformer KV cache, no perplexity/task accuracy, no production CPU inference latency or memory-bandwidth measurement, 10 random seeds, synthetic attention/retrieval traces only.

## Claim scope

Synthetic 2048-token trace-level KV eviction probe on CPU: entropy-guided scoring can modestly improve H2O-style cumulative-attention eviction at tight cache budgets when entropy is a helpful weak prior, but the effect is small and tuning-sensitive.

## Why it stopped

Synthetic proxy evidence produced a useful mechanism signal but not direct/full validation; stress ablation showed tuning-sensitive failure modes, so this run should not advance to paper writing.

## Recommended next action

Run one bounded real-transformer follow-up implementing entropy-aware KV eviction in a small CPU inference loop and require task/perplexity plus latency evidence before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer entropy-guided KV eviction check
- Success threshold: At a tight KV budget, entropy-guided eviction improves a real task or NLL metric by at least 3% relative versus H2O with no more than 5% CPU latency regression, and does not regress materially under neutral/noisy entropy.
- Stop condition: Stop if entropy guidance fails to beat H2O by 3% on real quality metrics, requires more than 5% latency overhead, or only wins under synthetic/aligned entropy assumptions.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-guided-kv-eviction-for-long-context-on-cpu-565dc05b7b70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
