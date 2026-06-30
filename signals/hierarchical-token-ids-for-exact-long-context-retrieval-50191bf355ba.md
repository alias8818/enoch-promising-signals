# Hierarchical Token IDs for Exact Long-Context Retrieval

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `hierarchical-token-ids-for-exact-long-context-retrieval-50191bf355ba`
Run ID: `hierarchical-token-ids-for-exact-long-context-retrieval-50191bf355ba-20260529T182123320867+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/770071bce95e

## What looked useful

Hierarchy is information-equivalent to flat offsets for exact lookup and provides no exactness gain by itself. Compression into a small token-ID vocabulary breaks exactness through collisions, while marker-token representations reduce payload capacity by 0.49% to 3.15% in tested context budgets.

## Boundaries and scale limits

This was an algorithmic CPU-only synthetic probe, not a trained language-model evaluation. It does not test whether learned hierarchical embeddings or marker tokens improve transformer retrieval accuracy, length generalization, or natural-language RAG behavior.

## Claim scope

For exact address-based retrieval on synthetic token arrays up to 1,048,576 tokens, hierarchical token/location IDs do not improve exactness over flat global IDs. Exact hierarchical paths match flat IDs at 100% accuracy with added lookup overhead; compressed hierarchical IDs introduce collisions; explicit hierarchy markers consume context budget.

## Why it stopped

Proxy early falsification rather than full long-context validation: the tested exact ID/address mechanism offered no retrieval accuracy advantage and showed concrete overhead/collision costs.

## Recommended next action

Stop this ID-mechanism claim as a proxy early falsification; if continuing, run a separate small-transformer key-value retrieval experiment comparing hierarchical position features against absolute and sinusoidal/rotary baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer hierarchical position feature retrieval test
- Success threshold: At least a 10 percentage point exact retrieval accuracy improvement over the best parameter-matched baseline on longer-than-train contexts, with no larger effective context budget and no degradation above 2 percentage points on train-length contexts.
- Stop condition: Stop if the hierarchical variant fails to beat the best baseline by 5 percentage points on two seeds, or if equal-budget marker overhead explains the apparent improvement.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-token-ids-for-exact-long-context-retrieval-50191bf355ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
