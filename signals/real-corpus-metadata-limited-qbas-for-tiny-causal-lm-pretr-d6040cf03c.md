# Real-corpus metadata-limited QBAS for tiny causal-LM pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-corpus-metadata-limited-qbas-for-tiny-causal-lm-pretr-d6040cf03c`
Run ID: `real-corpus-metadata-limited-qbas-for-tiny-causal-lm-pretr-d6040cf03c-20260607T013108195069+0000`

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

- Parent run decision: Queue-Based Data Selection with Batch-Adaptive Sampling for Tiny Local Pretraining: enoch://control-plane/projects/queue-based-data-selection-with-batch-adaptive-sampling-for-tiny-local-pretraining-f1d07e2a3f7e/runs/queue-based-data-selection-with-batch-adaptive-sampling-for-tiny-local-pretraining-f1d07e2a3f7e-20260607T002405355468+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/63bd8534a579

## What looked useful

Metadata-limited QBAS that treats low per-bin training loss as quality collapsed toward short/easy bins, lowered training loss, and worsened validation loss by +0.1336 nats/token versus uniform on average.

## Boundaries and scale limits

Small direct Tier 1 test only: WikiText-2, byte-level model, two seeds, 260 steps, one metadata-bin weighting rule, no GPT-2-small-class tokenized baseline, and no longer-run recovery check.

## Claim scope

On WikiText-2 raw paragraph records, a 397k-parameter byte-level causal Transformer trained for 260 matched steps under a metadata-limited easy-bin QBAS sampler had worse held-out loss than uniform sampling across two seeds.

## Why it stopped

Controlled small direct real-corpus causal-LM test falsified the predefined Tier 1 threshold: QBAS was worse than uniform in both matched seeds, so the result is useful no-paper evidence rather than a paper-positive validation.

## Recommended next action

Stop this variant as a no-paper negative; if continuing, test a bounded hard-bin or floor-constrained metadata sampler that must beat uniform by at least 0.02 nats/token across three seeds without easy-bin collapse.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Floor-constrained metadata QBAS for tiny WikiText causal-LM pretraining
- Success threshold: Mean validation cross entropy at least 0.02 nats/token lower than uniform across three matched seeds, with no more than one seed worse than uniform and no metadata bin receiving less than 5% of expected uniform coverage unless absent from the corpus.
- Stop condition: Stop if the constrained sampler is worse than uniform by at least 0.02 nats/token on mean validation loss or if diagnostics still show easy-bin collapse after warmup.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-metadata-limited-qbas-for-tiny-causal-lm-pretr-d6040cf03c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
