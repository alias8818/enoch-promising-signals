# Tiny mixing-law sweep: code/text/math ratios at matched sequence-item budget

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-mixing-law-sweep-code-text-math-ratios-at-matched-token-budget-aae7035639c1`
Run ID: `tiny-mixing-law-sweep-code-text-math-ratios-at-matched-token-budget-aae7035639c1-20260610T152948743614+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6cfd186277af

## What looked useful

Across 5 seeds, each 60% domain-heavy mix achieved the best held-out loss on its own domain, while the balanced 33/34/33 mix achieved the best balanced evaluation loss. This validates the harness and shows a reproducible toy mixing-law tradeoff.

## Boundaries and scale limits

Synthetic templated corpora only; character-level tokenization; 2-layer d_model 96 Transformer; 120k training-token corpus budget per run; 240 optimizer steps; 5 seeds. Not evidence for real-corpus or large-model optimal pretraining mixtures.

## Claim scope

In a controlled synthetic char-level tiny Transformer sweep, code/text/math mixture ratios at matched corpus token budget produce stable domain-specialization tradeoffs, and the balanced mixture gives the lowest balanced held-out loss.

## Why it stopped

Closed as no-paper useful signal: evidence is reproducible but synthetic/toy and insufficient for publication-grade claims about real pretraining mixtures.

## Recommended next action

Run a bounded deepen follow-up on small real code/text/math corpora with a standard tokenizer and the same matched-token ratio sweep before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny mixing-law confirmation for code/text/math ratios
- Success threshold: The same ordering should hold across at least 3 seeds: each domain-heavy mix wins its own domain, and the balanced mix has the lowest balanced validation loss by more than one standard error.
- Stop condition: Stop if the ordering is unstable across seeds or balanced loss differences are within one standard error, because the synthetic signal did not transfer.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-mixing-law-sweep-code-text-math-ratios-at-matched-token-budget-aae7035639c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
