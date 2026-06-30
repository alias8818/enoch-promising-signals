# Data-sequencing curriculum: easy->hard vs random for tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `data-sequencing-curriculum-easy-hard-vs-random-for-tiny-pretraining-53df19476381`
Run ID: `data-sequencing-curriculum-easy-hard-vs-random-for-tiny-pretraining-53df19476381-20260610T035854687910+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7ed16ef07a68

## What looked useful

Random sequencing achieved the best final balanced validation loss (3.5588 mean over 3 seeds). Strict easy-to-hard was worse by +0.5077 nats, hard-to-easy was worse by +4.3333 nats, and a 25% replay mixed curriculum was still worse by +0.2954 nats. The pattern indicates recency/forgetting from block curricula in this proxy.

## Boundaries and scale limits

Synthetic algorithmic sequences only; 4-layer d_model=128 transformer; 800 steps per run; 3 seeds per policy; not validated on natural-language corpora, downstream tasks, larger models, or longer token budgets.

## Claim scope

In a synthetic tiny causal-transformer next-token pretraining proxy with four difficulty buckets, fixed token/update budget, and balanced validation, strict easy-to-hard phase ordering underperforms random data sequencing.

## Why it stopped

Synthetic proxy early falsification of naive easy-to-hard sequencing, not a full natural-language validation.

## Recommended next action

Stop this run as a bounded no-paper negative/useful-signal result; a next bounded deepen test should use a small real text corpus with difficulty buckets and replay-rate ablations before considering larger pretraining.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text replay ablation for easy-to-hard tiny pretraining
- Success threshold: A replay curriculum beats random by at least 0.05 nats balanced validation loss with no bucket worse by more than 0.10 nats across at least three seeds.
- Stop condition: Stop if strict and replay curricula both fail to beat random, or if improvements appear only on the last-seen bucket while balanced loss remains worse than random.

## Evidence references

- Artifact root: `<local-path>/projects/data-sequencing-curriculum-easy-hard-vs-random-for-tiny-pretraining-53df19476381`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
