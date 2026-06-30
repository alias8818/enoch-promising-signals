# Entropy-Spike KV Selection for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-spike-kv-selection-for-long-context-9556c4ed0b16`
Run ID: `entropy-spike-kv-selection-for-long-context-9556c4ed0b16-20260523T021604379178+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b356e38b90fa

## What looked useful

Entropy-spike selection achieved 1.000 average hit rate in the entropy-correlated regime and 0.785 averaged across budgets in the mixed regime, versus about 0.08 for random and near-zero for recency. In the entropy-decoy regime it fell to 0.192 average, demonstrating a clear fragility when spikes are not causally tied to future utility.

## Boundaries and scale limits

No real transformer attention traces, no trained-model perplexity or answer-accuracy measurement, no GPU serving benchmark, and no 7B+ model validation. Sequence length was 8192 with 96 synthetic needles and budgets 128-512 over 24 trials per regime.

## Claim scope

Synthetic long-context KV cache simulation with planted retrieval needles, fixed cache budgets, and online scalar entropy/spike signals. Entropy-spike retention is useful when spikes correlate with future retrieval utility, but it is fragile under entropy-decoy distractors.

## Why it stopped

No-paper closure: the current evidence is a synthetic proxy useful signal, not a full validation. It partially supports the mechanism and early-falsifies broad entropy-spike-only reliability claims.

## Recommended next action

Run a bounded direct-evidence follow-up by replaying real transformer attention traces on long-context retrieval examples and measuring answer/logit preservation under entropy-spike KV pruning versus established baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Attention Trace Replay for Entropy-Spike KV Selection
- Success threshold: At equal KV budget, entropy-spike or persistence-filtered entropy-spike pruning improves answer/logit preservation by at least 10 percentage points over recency and random and is competitive with a standard attention-score baseline on real traces, without collapsing on decoy-heavy prompts.
- Stop condition: Stop if entropy-spike pruning is not better than random by at least 5 percentage points on real traces or if decoy prompts erase the benefit at all tested budgets.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-spike-kv-selection-for-long-context-9556c4ed0b16`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
