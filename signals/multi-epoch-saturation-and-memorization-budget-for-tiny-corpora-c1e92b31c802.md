# Multi-epoch saturation and memorization budget for tiny corpora

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-epoch-saturation-and-memorization-budget-for-tiny-corpora-c1e92b31c802`
Run ID: `multi-epoch-saturation-and-memorization-budget-for-tiny-corpora-c1e92b31c802-20260612T010356330370+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c05ce8741705

## What looked useful

Across three seeds, best held-out loss occurred by epoch 4 for 512 tokens and by epoch 1 for 2048/8192 tokens, while final train loss collapsed to 0.071-0.175 and final train-minus-heldout copy16 gaps reached 0.878-0.897.

## Boundaries and scale limits

Synthetic token streams only; corpus sizes 512, 2048, and 8192 tokens; three seeds; tiny Transformer only; no natural-language corpus, GPT-2-small-class baseline, canary exposure, or larger-scale validation.

## Claim scope

In a synthetic finite-state tiny-corpus setup with a 2-layer width-96 causal Transformer, held-out loss saturated after 1-4 epochs while train-specific 16-token continuation recall kept rising through 64 epochs.

## Why it stopped

Closed as no-paper useful signal: synthetic small-model evidence supports the mechanism but is not broad or direct enough for publication-grade validation.

## Recommended next action

Run a bounded real-corpus follow-up on one or two tiny text datasets with canary exposure or membership-inference metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tiny-corpus saturation and extraction check
- Success threshold: For both corpora, held-out loss reaches within 1% of best before the final quarter of training while direct memorization rises by at least 0.2 normalized units after that saturation point in at least two of three seeds.
- Stop condition: Stop if held-out loss and direct memorization both improve together through the final checkpoint, or if the memorization metric does not increase after saturation in at least two seeds per corpus.

## Evidence references

- Artifact root: `<local-path>/projects/multi-epoch-saturation-and-memorization-budget-for-tiny-corpora-c1e92b31c802`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
