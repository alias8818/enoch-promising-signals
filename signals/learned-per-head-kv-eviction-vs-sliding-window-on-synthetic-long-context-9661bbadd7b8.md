# Learned per-head KV eviction vs sliding window on synthetic long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-per-head-kv-eviction-vs-sliding-window-on-synthetic-long-context-9661bbadd7b8`
Run ID: `learned-per-head-kv-eviction-vs-sliding-window-on-synthetic-long-context-9661bbadd7b8-20260621T201939505568+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/21ef13b04662

## What looked useful

Sliding remains the best default for recent and mixed heads; learned eviction helps long-anchor and sentinel heads, especially at budget 64 where sentinel improves by about 9.95 percentage points over sliding. A validation-selected per-head policy improves aggregate hit rate by +0.08, +1.17, and +3.03 percentage points at budgets 16, 32, and 64, while naive learned eviction loses -4.81, -11.12, and -20.11 points.

## Boundaries and scale limits

This run tests synthetic KV cache events, not a trained transformer or real hidden-state KV cache. It does not measure language-model perplexity, downstream task accuracy, serving latency, memory bandwidth, or robustness across real corpora. Main confirmation used 8 test seeds per head and small linear utility models.

## Claim scope

On a synthetic 4-head long-context retrieval cache-policy benchmark with context length 8192 and per-head cache budgets 16, 32, and 64, naive learned per-head eviction underperforms sliding overall, but a validation-selected per-head policy that uses learned eviction only for long-anchor/sentinel heads gives small aggregate hit-rate gains over sliding.

## Why it stopped

No-paper closure: the bounded synthetic cache-policy evidence is mixed and useful, but naive learned eviction is worse than sliding overall and the positive signal is too small/proxy-only for a paper.

## Recommended next action

Run a bounded small-transformer synthetic associative-recall follow-up implementing the validation-selected per-head eviction policy inside attention, with sliding, pooled learned, untrained/random, and oracle controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of validation-selected per-head KV eviction
- Success threshold: Validation-selected per-head eviction improves aggregate downstream retrieval accuracy by at least 3 percentage points over sliding at one or more constrained cache budgets without more than 1 percentage point regression on short-recent queries.
- Stop condition: Stop if validation-selected per-head eviction fails to beat sliding on downstream accuracy at all tested budgets or if gains appear only in the standalone cache simulator and not in transformer attention.

## Evidence references

- Artifact root: `<local-path>/projects/learned-per-head-kv-eviction-vs-sliding-window-on-synthetic-long-context-9661bbadd7b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
