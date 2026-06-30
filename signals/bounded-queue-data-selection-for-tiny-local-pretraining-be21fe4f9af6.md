# Bounded Queue Data Selection for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `bounded-queue-data-selection-for-tiny-local-pretraining-be21fe4f9af6`
Run ID: `bounded-queue-data-selection-for-tiny-local-pretraining-be21fe4f9af6-20260605T182735232242+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8a5cab6b4755

## What looked useful

Raw bounded top-loss queues are unsafe for tiny local pretraining because they over-retain high-loss corrupted/noisy examples. Additive quality scoring mitigates but does not prevent this. A strict quality gate removes noise but still underperforms random streaming on rare held-out loss, suggesting stale hard-example retention and lost distributional coverage.

## Boundaries and scale limits

Synthetic grammar corpus only; no real tokenizer-based corpus, no downstream tasks, no GPT-2-small-class transformer, and no long/full-scale pretraining. Evidence is a bounded local proxy and should not be read as a universal data-selection failure.

## Claim scope

Synthetic tiny character-level LM pretraining with online bounded queues under equal step, batch, model, and candidate-scoring budgets. The tested raw high-loss and simple quality-aware bounded queues did not outperform random stream training.

## Why it stopped

Proxy early falsification: in two local synthetic settings, bounded high-loss queues were worse than random streaming, and a quality-gated queue still failed to beat random on rare held-out loss.

## Recommended next action

Stop this run as a proxy early falsification; the next bounded test should replace stale top-loss retention with recency decay plus diversity/distribution caps before any real-corpus scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Recency-Decayed Diverse Bounded Queue for Tiny Pretraining
- Success threshold: Rare held-out loss at least 10% lower than random_stream with clean loss no worse than random_stream by more than 5%, and final queue noise share below 5%.
- Stop condition: Stop if recency/diversity controls fail to beat random_stream on rare held-out loss in the scarce-rare setting or if clean loss degrades by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-queue-data-selection-for-tiny-local-pretraining-be21fe4f9af6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
