# Volunteer KV-Compressor Co-Training with Bounded Home Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-kv-compressor-co-training-with-bounded-home-workers-11bdd3080384`
Run ID: `volunteer-kv-compressor-co-training-with-bounded-home-workers-11bdd3080384-20260629T123628668609+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5a05e6a496ea

## What looked useful

FedAvg compressor accuracy was 0.1407 +/- 0.0026 at 2:1 compression and 0.1442 +/- 0.0039 at 1:1 slots, versus 0.015625 chance, about 0.126 mean-pooling control, and 1.0 uncompressed oracle. Extra slots did not materially rescue performance, suggesting the tested query-independent slot compressor/training design is the bottleneck.

## Boundaries and scale limits

Tested only a toy associative-retrieval task, three seeds per calibrated setting, one GB10 host, synthetic key/value pairs, no real transformer KV cache, no natural-language perplexity, no volunteer network effects, and no multi-node or long-duration training.

## Claim scope

On a synthetic random key/value retrieval task with four bounded workers, eight local pairs per worker, and FedAvg-style compressor co-training, the tested query-independent slot-attention KV compressor learns above chance but remains far below uncompressed lookup and barely above a trained mean-pooling control.

## Why it stopped

Early direct synthetic falsification: the trained compressor is repeatably above chance but far below the full uncompressed oracle, and even the 1:1 slot setting reaches only about 14% retrieval accuracy.

## Recommended next action

Stop this tested compressor form as no-paper evidence; run a bounded deepen test of pointer-preserving or reconstruction-regularized KV compression on the same retrieval task before attempting larger transformer-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pointer-Preserving KV Compressor on Bounded Worker Retrieval
- Success threshold: Reach at least 0.70 validation accuracy at 1:1 slots and at least 0.40 at 2:1 compression while outperforming mean-pooling by at least 0.20 absolute accuracy across three seeds.
- Stop condition: Stop if the pointer-preserving or reconstruction-regularized compressor remains below 0.30 accuracy at 1:1 slots after the calibrated budget, because larger transformer-scale runs would not be justified.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-kv-compressor-co-training-with-bounded-home-workers-11bdd3080384`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
