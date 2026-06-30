# Shared Optimizer Statistics Across Homogeneous Transformer Layers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `shared-optimizer-statistics-across-homogeneous-transformer-layers-a168edf03652`
Run ID: `shared-optimizer-statistics-across-homogeneous-transformer-layers-a168edf03652-20260529T003303460554+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b40ae817e9c8

## What looked useful

Depth-shared adaptive scale statistics are plausible and worth a bounded real-text follow-up; depth-shared momentum/direction statistics are not supported by this probe.

## Boundaries and scale limits

Synthetic toy task only; no real text corpus, GPT-2-small-class scale, mixed precision optimizer state, fused/distributed optimizer, long-run stability, or memory-pressure validation was tested.

## Claim scope

On a 6-layer, 96-wide toy causal decoder trained for 1000 GPU steps on a synthetic arithmetic-progression next-token task, sharing AdamW second-moment statistics across same-shaped corresponding transformer layer parameters matched standard AdamW validation loss within seed noise while reducing optimizer-state elements by 31.4%; sharing both first and second moments caused a clear optimization regression.

## Why it stopped

Proxy-scale useful signal only: the synthetic transformer experiment supports a mechanism but is not direct publication-grade language-model evidence.

## Recommended next action

Run a bounded real-text nanoGPT/GPT-2-small-class deepen test for the shared_v variant and stop if validation loss regresses by more than 2% at matched tokens despite at least 30% optimizer-state reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text validation of depth-shared AdamW second moments
- Success threshold: shared_v final validation loss within 2% of AdamW at matched token budget with at least 30% optimizer-state element reduction and no training instability.
- Stop condition: Stop if shared_v exceeds AdamW validation loss by more than 2% on two independent seeds or fails to deliver at least 30% optimizer-state reduction in the real-text setup.

## Evidence references

- Artifact root: `<local-path>/projects/shared-optimizer-statistics-across-homogeneous-transformer-layers-a168edf03652`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
