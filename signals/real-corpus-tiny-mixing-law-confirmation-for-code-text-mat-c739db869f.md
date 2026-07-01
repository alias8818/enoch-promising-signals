# Real-corpus tiny mixing-law confirmation for code/text/math ratios

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-tiny-mixing-law-confirmation-for-code-text-mat-c739db869f`
Run ID: `real-corpus-tiny-mixing-law-confirmation-for-code-text-mat-c739db869f-20260610T155213486165+0000`

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

- Parent run decision: Tiny mixing-law sweep: code/text/math ratios at matched sequence-item budget: enoch://control-plane/projects/tiny-mixing-law-sweep-code-text-math-ratios-at-matched-token-budget-aae7035639c1/runs/tiny-mixing-law-sweep-code-text-math-ratios-at-matched-token-budget-aae7035639c1-20260610T152948743614+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6cfd186277af

## What looked useful

Direct real-corpus Tier 1 evidence supports per-domain train-mixture sensitivity for code/text/math, but does not fully confirm a stable balanced mixing law at this tiny scale.

## Boundaries and scale limits

Three seeds; 2-layer 128-hidden byte LM; about 1.2 MB train and 0.2 MB validation bytes per domain; 220 training steps per ratio; five train ratios; no larger tokenizer/model, longer convergence, downstream transfer, or dense ratio simplex.

## Claim scope

A tiny byte-level Transformer trained on small real code/text/math corpus slices shows robust domain-specific mixture sensitivity: across three seeds, code, text, and math held-out losses were each minimized by the corresponding 60% train-share mixture. The stronger balanced-target optimality condition was mixed, with the equal mix winning in two of three seeds.

## Why it stopped

The controlled small direct test produced mixed evidence: robust domain-alignment support, but balanced-target optimality failed in one of three seeds and the experiment is far below publication scale.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded medium deepen test with more seeds, 1k-5k steps, a denser ratio simplex, and confidence intervals before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-corpus code/text/math mixture simplex with confidence intervals
- Success threshold: Across at least five seeds, each single-domain held-out loss is minimized by a high-share matching train mixture and the balanced held-out mixture is minimized by an equal or near-equal train mixture with non-overlapping or practically meaningful confidence intervals.
- Stop condition: Stop if domain bests are not aligned in at least two of three domains after 1000 steps, or if balanced-target confidence intervals remain overlapping across all near-balanced and heavy mixtures after the planned budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-mixing-law-confirmation-for-code-text-mat-c739db869f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
