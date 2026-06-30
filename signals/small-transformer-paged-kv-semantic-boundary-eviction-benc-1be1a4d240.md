# Small-transformer paged-KV semantic-boundary eviction benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-paged-kv-semantic-boundary-eviction-benc-1be1a4d240`
Run ID: `small-transformer-paged-kv-semantic-boundary-eviction-benc-1be1a4d240-20260531T102503815616+0000`

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

- Parent run decision: Semantic-boundary KV eviction for 6GB long-context inference: enoch://control-plane/projects/semantic-boundary-kv-eviction-for-6gb-long-context-inference-51fa19b70d0b/runs/semantic-boundary-kv-eviction-for-6gb-long-context-inference-51fa19b70d0b-20260530T043315545164+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3de4fe3a8a0b

## What looked useful

Across three independent 500-step seed repeats, semantic-boundary eviction achieved mean answer NLL 0.00643 and 100% answer accuracy versus FIFO mean answer NLL 3.46922 and 10.6% accuracy with the same retained-token budget; a 900-step run showed the same pattern.

## Boundaries and scale limits

Synthetic data, explicit oracle boundaries, tiny transformer, short 192-token documents, 32-token KV budget, no pretrained LM, no real text, no serving throughput or memory-fragmentation measurement, and no comparison to attention-score or learned eviction policies.

## Claim scope

In a controlled synthetic segmented language task trained on a tiny decoder-only transformer, preserving the active semantic-boundary page under an equal 32-token paged-KV budget prevents FIFO's late-segment answer-token collapse when the required topic state is introduced only at the segment boundary.

## Why it stopped

Tier 1 direct controlled test succeeded as a useful mechanism signal, but the evidence is synthetic and not broad or realistic enough for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on a pretrained small LM or semi-real multi-document task with variable segment lengths and non-oracle boundary detection before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained small-LM semantic-boundary paged-KV eviction on semi-real multi-document prompts
- Success threshold: Semantic-boundary eviction improves late-query NLL or task accuracy by at least 20% relative to FIFO's degradation from full cache on at least two task families, while adding no more than 5% latency overhead and using the same page budget.
- Stop condition: Stop if semantic-boundary eviction fails to beat FIFO and recency-window baselines on both real/semi-real task families or if boundary-detection overhead exceeds the allowed latency budget.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-paged-kv-semantic-boundary-eviction-benc-1be1a4d240`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
