# CPU-Offloaded Optimizer with Async Pipeline During Forward

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `cpu-offloaded-optimizer-with-async-pipeline-during-forward-0ed47a5ca6af`
Run ID: `cpu-offloaded-optimizer-with-async-pipeline-during-forward-0ed47a5ca6af-20260527T191213696322+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b00ef2eaaae5

## What looked useful

On the 25.18M parameter probe, synchronous CPU offload was 5.38x-6.21x slower than GPU AdamW. CPU update plus copyback took 13.46x-17.61x a forward-only pass, so it could not be hidden during the next forward. The one-step stale async variant remained 3.82x-3.92x slower and had much weaker short-run loss improvement.

## Boundaries and scale limits

Only synthetic MLP regression was tested, up to 25.18M parameters and 20-30 measured steps. No LLM corpus, long convergence run, multi-GPU setup, custom fused CPU optimizer, or production offload runtime was tested.

## Claim scope

Early falsification on a GB10 synthetic GPU MLP benchmark: CPU-resident AdamW update plus parameter copyback could not be hidden under the next forward pass, and the tested async overlap required stale-weight semantics.

## Why it stopped

Proxy/direct bounded GB10 evidence falsified the core overlap premise: CPU optimizer update and copyback were far longer than the next forward, and the only async overlap route used stale weights and degraded short-run loss movement. This is not a full-scale LLM validation.

## Recommended next action

Stop this line as a no-paper early falsification unless a new design removes the fresh-weight dependency or explicitly studies stale optimizer semantics as a different algorithm.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-optimizer-with-async-pipeline-during-forward-0ed47a5ca6af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
