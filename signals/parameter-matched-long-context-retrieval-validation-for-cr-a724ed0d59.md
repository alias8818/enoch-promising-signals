# Parameter-matched long-context retrieval validation for cross-layer KV anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `parameter-matched-long-context-retrieval-validation-for-cr-a724ed0d59`
Run ID: `parameter-matched-long-context-retrieval-validation-for-cr-a724ed0d59-20260526T151051216637+0000`

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

- Parent run decision: Cross-Layer KV Anchors for Long Context: enoch://control-plane/projects/cross-layer-kv-anchors-for-long-context-b69c9abb795d/runs/cross-layer-kv-anchors-for-long-context-b69c9abb795d-20260525T235652516548+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b4b0386b97fe

## What looked useful

Cross-layer value-position anchors were parameter matched and consistently improved mean accuracy over baseline by +1.79 percentage points at 32 pairs and +1.30 percentage points at 64 pairs, but absolute accuracy remained low and 128-pair extrapolation was near chance.

## Boundaries and scale limits

Toy synthetic data, small 227k-parameter models, three seeds, 1000 training steps, no pretrained LLMs, no realistic document retrieval workload, and no publication-grade robustness or ablations.

## Claim scope

In a small synthetic key-value retrieval classifier trained at 32 pairs, a parameter-matched transformer with value-position cross-layer KV anchors produced a small accuracy lift over a standard causal transformer at 32 and 64 evaluation pairs, with only marginal near-chance behavior at 128 pairs.

## Why it stopped

Controlled small direct validation produced only a small toy retrieval lift, not robust long-context retrieval evidence or publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with a bounded direct follow-up that requires at least 2x chance accuracy at 64 and 128 pairs plus at least a 5 percentage point anchor-over-baseline gain across three seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer-trained value-anchor retrieval with explicit success threshold
- Success threshold: Across at least three seeds, anchor accuracy is >=12.5% for 16-class values at both 64 and 128 pairs and exceeds the parameter-matched baseline by >=5 percentage points at both lengths.
- Stop condition: Stop if the anchor variant fails to exceed baseline by 5 percentage points at 64 and 128 pairs after the calibrated training budget, or if both variants remain below 2x chance.

## Evidence references

- Artifact root: `<local-path>/projects/parameter-matched-long-context-retrieval-validation-for-cr-a724ed0d59`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
