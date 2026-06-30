# Top-K Gradient Masking for Sparse Optimizer States

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `top-k-gradient-masking-for-sparse-optimizer-states-db1070a4267d`
Run ID: `top-k-gradient-masking-for-sparse-optimizer-states-db1070a4267d-20260621T101612066853+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/e2df2029c8a7

## What looked useful

Per-step top-k masking alone is not enough to create durable sparse Adam state because coordinate churn rapidly touches almost every coordinate. Recency-based eviction is the bounded adjacent mechanism worth testing next.

## Boundaries and scale limits

Synthetic linear regression only; no real sparse optimizer storage kernel, no measured allocator memory savings, no transformer or GPT-2-small-class training, no large embedding table, no distributed setting, and only three seeds over one dimension and one TTL.

## Claim scope

On two 8192-parameter synthetic linear regression probes, top-k masked Adam improved validation loss versus dense Adam, but plain persistent sparse optimizer state became effectively dense because the cumulative selected-coordinate union reached 98-100% within 500 steps. A 1% top-k, 50-step TTL eviction variant kept live state near 38-40% while retaining better-than-baseline validation loss in this proxy.

## Why it stopped

No-paper useful signal: the local proxy supports the masking/eviction mechanism but early-falsifies naive persistent sparse-state savings; this is not full validation.

## Recommended next action

Run a bounded direct follow-up with a real sparse-state TopK-Adam-TTL optimizer on a small transformer or embedding-heavy model, measuring actual optimizer memory, validation loss, and runtime against dense Adam.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sparse-State TopK-Adam-TTL on a Small Transformer
- Success threshold: At least 50% lower measured optimizer-state memory than dense Adam, validation loss within 5% of dense Adam, and no more than 10% throughput regression on the bounded model across three seeds.
- Stop condition: Stop if live sparse state exceeds 70% of dense state or validation loss is more than 10% worse than dense Adam after the calibrated bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/top-k-gradient-masking-for-sparse-optimizer-states-db1070a4267d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
