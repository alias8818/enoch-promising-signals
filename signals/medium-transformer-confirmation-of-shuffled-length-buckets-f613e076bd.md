# Medium Transformer confirmation of shuffled length buckets on a larger real corpus

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `medium-transformer-confirmation-of-shuffled-length-buckets-f613e076bd`
Run ID: `medium-transformer-confirmation-of-shuffled-length-buckets-f613e076bd-20260602T205423729029+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-corpus CPU training test of shuffled length buckets: enoch://control-plane/projects/real-corpus-cpu-training-test-of-shuffled-length-buckets-69a1461942/runs/real-corpus-cpu-training-test-of-shuffled-length-buckets-69a1461942-20260602T163933727517+0000
- Parent run decision: Length Stratification Cuts Padding Waste in CPU Pretraining: enoch://control-plane/projects/length-stratification-cuts-padding-waste-in-cpu-pretraining-f8a7a51138a4/runs/length-stratification-cuts-padding-waste-in-cpu-pretraining-f8a7a51138a4-20260601T053711338734+0000

## What looked useful

The padding-efficiency mechanism was confirmed, but the direct target metric falsified the useful-training-quality claim in this bounded setting: bucket_shuffled mean validation loss was 2.698828 versus 2.673400 for random, with paired losses worse on all 3 seeds; bucket_sorted was worse still at 2.717303.

## Boundaries and scale limits

CPU-only worker; no GPU/GB10 run; byte-level small/medium transformer rather than GPT-2-small-class; bounded 150-step training rather than convergence; WikiText-2 real corpus but not large-scale pretraining.

## Claim scope

On WikiText-2 with a 397k-parameter byte-level causal transformer, 10,000 train chunks, 1,500 validation chunks, 150 optimizer steps, and fixed seeds 11/23/37, shuffled length-bucket batching reduced padding and slightly improved throughput but worsened validation loss versus standard random batching on every seed.

## Why it stopped

Direct Tier 2 target metrics on a real corpus with fixed seeds, a real random baseline, and a sorted-bucket ablation did not support the shuffled length-bucket hypothesis; the mechanism improved padding but validation loss degraded consistently.

## Recommended next action

Stop this line as no-paper bounded evidence unless a future independent run specifically tests a matched-token-budget or much larger-model variant; do not escalate this result to paper writing.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/medium-transformer-confirmation-of-shuffled-length-buckets-f613e076bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
