# Calibration-trained ternary low-rank residual repair for GPT-2-small BPE validation

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `calibration-trained-ternary-low-rank-residual-repair-for-g-0e07829031`
Run ID: `calibration-trained-ternary-low-rank-residual-repair-for-g-0e07829031-20260519T153816457555+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Calibration-trained ternary low-rank residual repair for GPT-2-small BPE validation: internal_generated:calibration-trained-ternary-low-rank-residual-repair-for-g-0e07829031

## What looked useful

Rank-32 repair reduced PPL from 278,616 for ternary-only to 2,930.8, but dense GPT-2 was 39.24 PPL on the same validation tokens; rank increase from 8 to 32 improved PPL only from 3,941.9 to 2,930.8, far short of paper-readiness.

## Boundaries and scale limits

Completed runs used one seed, 32,640 validation tokens, 256 calibration blocks, short 24-step calibration, ranks 8 and 32, and left embeddings/lm_head dense. Longer 48-step run was externally terminated before writing a completed result.

## Claim scope

Direct GPT-2-small BPE validation on Wikitext-2 shows calibration-trained low-rank residuals can substantially improve ternarized transformer projection weights, but not recover dense GPT-2-small quality.

## Why it stopped

Direct bounded GPT-2 BPE validation falsified the Tier 4 paper-readiness threshold; the result is useful mechanistic evidence, not publication-grade compression quality.

## Recommended next action

Stop this follow-up at depth 4: record the useful mechanism signal but do not pursue another deepen/retry branch because direct validation remains roughly 75x worse than dense PPL.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/calibration-trained-ternary-low-rank-residual-repair-for-g-0e07829031`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
