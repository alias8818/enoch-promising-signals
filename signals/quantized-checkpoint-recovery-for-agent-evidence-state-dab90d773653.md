# Quantized Checkpoint Recovery for Agent Evidence State

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-checkpoint-recovery-for-agent-evidence-state-dab90d773653`
Run ID: `quantized-checkpoint-recovery-for-agent-evidence-state-dab90d773653-20260526T044111853700+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7cc8b96039e4

## What looked useful

All 45 full-run checkpoints reloaded successfully. Mean top-10 Jaccard vs fp32 was 0.9995 for fp16, 0.9803 for int8, and 0.7312 for int4. Mean top-1 claim agreement was 0.9997 for fp16, 0.9889 for int8, and 0.7995 for int4. Int8 changes concentrated around small fp32 margins, indicating near-tie sensitivity rather than broad geometry collapse.

## Boundaries and scale limits

Synthetic clustered embeddings only; no real agent traces, LangGraph message/tool/provenance state, schema migration, production restart replay, real embedding model, or large evidence corpus was tested.

## Claim scope

Synthetic vector evidence-state checkpoints with 4096 evidence vectors, 1024 queries, three separability regimes, five seeds, and fp16/int8/int4 checkpoint reloads. Int8 per-vector quantization preserved geometry and top-10 retrieval well at about 25.1% of fp32 vector storage, but missed the predeclared 0.99 top-1/decision preservation thresholds across the full sweep; int4 was too lossy.

## Why it stopped

No-paper useful signal: the run is a synthetic proxy and int8 missed the strict 0.99 top-1/decision thresholds, while int4 failed clearly.

## Recommended next action

Run a bounded real-trace replay of fp32/fp16/int8 evidence checkpoints with margin stratification before considering int8 as a hard-cutover checkpoint format.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Margin-Stratified Quantized Evidence Checkpoint Replay
- Success threshold: Int8 or a margin-aware hybrid achieves at least 0.995 downstream decision agreement and at least 0.98 citation/retrieval agreement on high-margin real traces with at least 2x storage reduction versus fp32.
- Stop condition: Stop if real-trace int8 or hybrid recovery falls below 0.99 decision agreement outside explicitly low-margin cases, or if failures are caused by non-vector checkpoint fields not addressed by quantization.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-checkpoint-recovery-for-agent-evidence-state-dab90d773653`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
