# Rolling Attention Score KV-Cache Eviction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rolling-attention-score-kv-cache-eviction-3919c029d565`
Run ID: `rolling-attention-score-kv-cache-eviction-3919c029d565-20260628T045505383706+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/bd7acb8f5843

## What looked useful

Pure rolling attention-score eviction has a cold-start/admission failure and performs like cumulative heavy-hitter, far below sliding-window recency. A 32-token recency-protected rolling variant can beat sliding in a landmark-heavy favorable case, but sliding dominates the aggregate synthetic sweep.

## Boundaries and scale limits

No trained model, real KV cache, long-context benchmark, hardware serving path, or task-level accuracy was tested. Synthetic traces proxy attention demand but do not model distribution shifts caused by evicting keys in an actual transformer.

## Claim scope

Synthetic online KV-cache eviction simulation at sequence length 1536, cache ratios near 5%, 10%, and 20%, over 6 synthetic attention scenarios and 8 seeds. Metrics are retained full-history attention mass and normalized attention-output error.

## Why it stopped

This is a synthetic/proxy early falsification of standalone rolling-score eviction, not a full validation on real models; the useful recency-protected signal needs direct model evidence.

## Recommended next action

Run one bounded direct-model follow-up on a GPT-2-small-class long-context/perplexity and needle-landmark harness comparing sliding, pure rolling, and recency-protected rolling before considering any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-model test of recency-protected rolling attention KV eviction
- Success threshold: Recency-protected rolling must improve at least one direct model metric by 5% relative over sliding-window at the same cache budget without degrading perplexity by more than 2%; pure rolling should be reported separately.
- Stop condition: Stop if recency-protected rolling fails to beat sliding on both perplexity and retrieval at two cache budgets, or if implementation overhead prevents a faithful KV eviction comparison within a bounded local run.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-attention-score-kv-cache-eviction-3919c029d565`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
