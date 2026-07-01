# Quality-Filtered Data Selection for Tiny GPT-2 Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-filtered-data-selection-for-tiny-gpt-2-pretraining-667bcc841e05`
Run ID: `quality-filtered-data-selection-for-tiny-gpt-2-pretraining-667bcc841e05-20260628T034732256355+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/de30b90b0dd7

## What looked useful

Across seeds 7, 11, and 19, quality-top selection reduced clean validation loss versus random by mean -0.7563 nats and reduced perplexity to 0.470x of random; bottom-quality selection was worse than random by mean +0.3565 nats. This supports the local mechanism but not a paper-ready broad claim.

## Boundaries and scale limits

Synthetic corpus only; quality heuristic is aligned with generated corruptions; model is much smaller than GPT-2 small; 450 training steps per policy; no real web corpus, exact GPT-2 tokenizer/architecture, downstream tasks, or long-horizon scaling validation.

## Claim scope

In a controlled synthetic corpus with clean documents plus light/heavy corrupted variants, selecting documents with a simple quality heuristic improved clean held-out loss for a tiny decoder-only GPT-style language model under equal selected-document budgets across three seeds.

## Why it stopped

Closed as no-paper useful signal: controlled evidence supports the mechanism, but synthetic-only data and tiny short-horizon training are insufficient for publication-grade quality-filtered GPT-2 pretraining claims.

## Recommended next action

Run a bounded real-data deepen test on a small public text corpus with matched sequence-item budgets, repeated seeds, top/random/bottom quality controls, and tokenizer-matched perplexity before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data tiny GPT quality-filtered selection check
- Success threshold: Top-quality selection beats random by at least 10% relative held-out perplexity in at least 2 of 3 seeds, and bottom-quality selection is worse than random or clearly worse than top-quality.
- Stop condition: Stop if top-quality fails to beat random in 2 of 3 seeds under matched budgets, if the quality score cannot separate data without synthetic artifacts, or if the run would require more than the local bounded training budget.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filtered-data-selection-for-tiny-gpt-2-pretraining-667bcc841e05`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
