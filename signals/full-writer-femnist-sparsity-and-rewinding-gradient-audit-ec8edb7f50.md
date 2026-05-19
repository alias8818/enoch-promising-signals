# Full-Writer FEMNIST Sparsity and Rewinding Gradient Audit

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `full-writer-femnist-sparsity-and-rewinding-gradient-audit-ec8edb7f50`
Run ID: `full-writer-femnist-sparsity-and-rewinding-gradient-audit-ec8edb7f50-20260517T061553606600+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Full-Writer FEMNIST Sparsity and Rewinding Gradient Audit: internal_generated:full-writer-femnist-sparsity-and-rewinding-gradient-audit-ec8edb7f50

## What looked useful

Rewound SNIP achieved 87.11%, 87.72%, and 87.99% mean final accuracy at 10/20/30% keep versus dense 88.27%, reducing dense gaps to 1.16, 0.55, and 0.28 points. It beat random by 3.82 points at 10%, but only 1.75 and 1.17 points at 20% and 30%, failing the robustness threshold. Plain SNIP and magnitude were also competitive at higher keep fractions, while magnitude collapsed at 10%.

## Boundaries and scale limits

This was a full-writer FEMNIST validation for one compact CNN and one 10-epoch schedule, not a broader architecture/dataset replication. Rewinding used one warmup epoch only; iterative pruning and longer rewind checkpoint sweeps were not tested.

## Claim scope

On full 3,400-client writer-partition FED-EMNIST with a compact CNN, 10 training epochs, three fixed seeds, and 10/20/30% kept weights, one-epoch rewound SNIP masks nearly close the dense-baseline gap and beat random masks at every sparsity, but the random-control margin falls below the pre-registered 3-point paper-readiness threshold at 20% and 30% keep.

## Why it stopped

Full direct validation produced a useful rewinding signal but failed the paper gate because gradient/rewound masks were not robustly at least 3 accuracy points above random controls across the 10/20/30% sparsity sweep.

## Recommended next action

Stop as no-paper useful evidence: the full-writer depth-4 validation directly tested the requested threshold and failed the 3-point random-control margin at 20% and 30% keep; do not recommend another follow-up because the controller lineage is already at depth 4.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/full-writer-femnist-sparsity-and-rewinding-gradient-audit-ec8edb7f50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
