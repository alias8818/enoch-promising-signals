# Deduplication Granularity Matters for Tiny Pretraining Quality

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deduplication-granularity-matters-for-tiny-pretraining-quality-f4c99664d670`
Run ID: `deduplication-granularity-matters-for-tiny-pretraining-quality-f4c99664d670-20260610T221102837826+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/469411b4e18c

## What looked useful

Document-level exact dedup was identical to no dedup because every document was unique, while paragraph-level dedup removed repeated boilerplate, shifted the token budget toward facts, and improved fact-line LM loss from 3.474 to 2.749 nats/token. Answer-token accuracy changed only slightly, so the strongest evidence is for useful-token allocation rather than robust fact memorization.

## Boundaries and scale limits

Synthetic corpus only; no natural web/Wikipedia data, no standard tokenizer, no downstream benchmarks, no GPT-2-small-class baseline, and no long/full-scale pretraining.

## Claim scope

In a controlled synthetic archive corpus with unique document ids/facts plus repeated boilerplate, paragraph-level exact dedup admitted 2.54x more fact sentences into an equal 42,000-token tiny-Transformer pretraining budget than document-level exact dedup and reduced fact-line LM loss across 3 seeds.

## Why it stopped

No-paper useful signal: the controlled mechanism is supported, but the evidence is synthetic and the answer-token quality gain is small, so this is not publication-grade validation.

## Recommended next action

Run a bounded natural-corpus confirmation using a small web/Wikipedia slice with naturally repeated boilerplate/templates, comparing document-, paragraph-, and sentence/shingle-level dedup under an equal token budget with a GPT-2-small-class or parameter-matched tiny baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Corpus Dedup Granularity Confirmation for Tiny Pretraining
- Success threshold: Paragraph/shingle dedup improves content-heavy held-out loss by at least 5% relative to document-level dedup across seeds while not increasing overall validation loss by more than 2%.
- Stop condition: Stop if natural-corpus paragraph/shingle dedup does not improve content-heavy held-out loss over document-level dedup in at least 2 of 3 seeds, or if dedup removes too little boilerplate to materially change token allocation.

## Evidence references

- Artifact root: `<local-path>/projects/deduplication-granularity-matters-for-tiny-pretraining-quality-f4c99664d670`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
