# Shard-size and top-k retrieval ablation for multi-model AnchorState reload

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `83`
Project ID: `shard-size-and-top-k-retrieval-ablation-for-multi-model-an-20e8d5620c`
Run ID: `shard-size-and-top-k-retrieval-ablation-for-multi-model-an-20e8d5620c-20260520T143610106263+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Multi-model semi-real AnchorState reload validation: enoch://control-plane/projects/multi-model-semi-real-anchorstate-reload-validation-e219eb79ae/runs/multi-model-semi-real-anchorstate-reload-validation-e219eb79ae-20260520T140134124892+0000
- Parent run decision: Medium AnchorState persistence under naturalistic distractors and separate-process reload: enoch://control-plane/projects/medium-anchorstate-persistence-under-naturalistic-distract-57723cd7b7/runs/medium-anchorstate-persistence-under-naturalistic-distract-57723cd7b7-20260520T134703470696+0000

## What looked useful

The parent multi-model AnchorState reload failure is mostly a candidate-set selection bottleneck rather than durable state loss. Exact top-1 retrieval restored all four models to >=0.978 exact recall, while top-k 3 and 5 failed the all-model threshold because smaller models often selected wrong in-state values.

## Boundaries and scale limits

This run reuses parent semi-real generated episodes and model-extracted JSON files, uses deterministic candidate construction that guarantees target inclusion, and tests a local JSON state store rather than production retrieval, noisy retriever miss rates, real private user logs, or a deployed state service.

## Claim scope

On the parent semi-real fixed-seed AnchorState corpus, four cached local instruction models recovered exact code recall after separate-process JSON reload when the reader prompt contained a deterministic top-1 retrieved candidate: minimum model accuracy was 0.978 across 45 episodes/model, versus parent 15-entry full-shard accuracies of 0.556-0.956 and no-memory/corrupt controls at 0.0.

## Why it stopped

The scoped retrieval ablation succeeded, but the evidence remains a semi-real deterministic-retrieval benchmark rather than publication-grade production validation; controller follow-up depth is already 4, so no further follow-up is recommended.

## Recommended next action

Stop this depth-4 follow-up campaign with the bounded useful signal; do not claim paper readiness without a separate production/noisy-retrieval validation on real or less-template data.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/shard-size-and-top-k-retrieval-ablation-for-multi-model-an-20e8d5620c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
