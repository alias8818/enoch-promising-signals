# Curation Ladder for 50M-Token Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `curation-ladder-for-50m-token-tiny-pretraining-4d95feb1799f`
Run ID: `curation-ladder-for-50m-token-tiny-pretraining-4d95feb1799f-20260613T130700601117+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3c2469b6e979

## What looked useful

Ladder beat uniform mixing on broad validation loss in 3/3 seeds at 360 steps and 5/5 seeds at 720 steps. Confirmation broad loss was 0.6969 for ladder versus 0.8419 for uniform, a 17.2% relative reduction; reverse ladder was worse at 1.2477.

## Boundaries and scale limits

Synthetic data only; tiny 2-layer transformer; 1.47M and 2.95M training tokens per schedule/seed; no real 50M-token corpus, downstream task, tokenizer, or production curation validation.

## Claim scope

In a deterministic synthetic tiny-pretraining proxy, a clean-to-mixed curation ladder improved broad held-out character-level language modeling loss versus uniform mixing under matched sequence-item budgets.

## Why it stopped

Closed as no-paper useful signal: the proxy supports the mechanism but is synthetic and below the direct 50M-token evidence required for a publication-grade claim.

## Recommended next action

Run a bounded real-corpus deepen test with 5M-50M tokens, explicit curation tiers, matched uniform/reverse/clean-only controls, multiple seeds, and broad validation plus downstream or truthfulness probes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Curation Ladder for Tiny Pretraining
- Success threshold: Ladder beats uniform mixing on broad validation loss in at least four of five seeds and does not regress the downstream or truthfulness probe by more than 2% relative.
- Stop condition: Stop if ladder fails to beat uniform in at least three of the first five seeds, if reverse ladder matches ladder within noise, or if deduplication/tier controls remove the effect.

## Evidence references

- Artifact root: `<local-path>/projects/curation-ladder-for-50m-token-tiny-pretraining-4d95feb1799f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
