# Tiered memory for small cascade-aware agents

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiered-memory-for-small-cascade-aware-agents-9d4edff0fd58`
Run ID: `tiered-memory-for-small-cascade-aware-agents-9d4edff0fd58-20260614T002131413328+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c3b5be52bae7

## What looked useful

Naive tiered retrieval reduced mean token cost by 88.7% versus fallback-backed flat similarity but dropped main-run accuracy to 0.5969 versus 1.0000 fallback-backed flat similarity and 0.8340 potential small-model accuracy for flat retrieval. Budget sensitivity did not rescue the policy.

## Boundaries and scale limits

No real LLMs, learned embeddings, real agent traces, or serving stack were evaluated; results are proxy evidence only and should not be generalized to all hierarchical memory systems.

## Claim scope

Synthetic retrieval/cascade benchmark for a naive entity-attribute tiered memory policy under a small-agent context budget.

## Why it stopped

Proxy early falsification: structural tier hits produced overconfident no-cascade decisions and substantial accuracy loss, so this is not a full validation and not paper-ready.

## Recommended next action

Stop this naive policy as a paper path; only retest if adding calibrated answer-sufficiency and uncertainty-aware fallback to the tiered memory gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Uncertainty-Calibrated Tiered Memory Gate
- Success threshold: Accuracy >= 0.95 of flat fallback-backed baseline and mean token cost <= 0.50 of flat fallback-backed baseline on the corrected benchmark.
- Stop condition: Stop if calibrated tiered accuracy remains below 0.90 or cost reduction is below 25% after budget and threshold sweeps.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-memory-for-small-cascade-aware-agents-9d4edff0fd58`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
