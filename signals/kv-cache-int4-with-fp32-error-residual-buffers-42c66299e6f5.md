# KV-Cache INT4 with FP32 Error Residual Buffers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-int4-with-fp32-error-residual-buffers-42c66299e6f5`
Run ID: `kv-cache-int4-with-fp32-error-residual-buffers-42c66299e6f5-20260603T140920930706+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bfc35e4763c

## What looked useful

At 10% FP32 residual entries, memory was about 46.6% of FP16 KV. Recent residuals improved mean relative-L2 attention-output error by 5.3% on normal data, 9.5% on heavy-tail data, and 99.0% on a favorable spiky-recent distribution. Oracle high-error residual selection improved heavy-tail error by 80.3%, indicating the mechanism is useful only if a practical selector closes the oracle gap.

## Boundaries and scale limits

No real transformer checkpoint, perplexity, generation-quality, GPU kernel, or serving-throughput validation was run. Sequence lengths were at most 4096 with 8 heads, head dimension 64, 32 decode queries, 3 synthetic distributions, and 3 seeds.

## Claim scope

Synthetic CPU NumPy single-step attention fidelity tests show that INT4 KV-cache plus FP32 residual entries can reduce attention-output error when residuals are assigned to high-error or recent-spiky tokens, but a simple recent-token residual buffer is weak on normal and general heavy-tail synthetic workloads.

## Why it stopped

Proxy synthetic fidelity evidence supports the residual mechanism but early-falsifies the simple recent-buffer version as a general solution; this is not full model or serving validation.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded follow-up that tests cheap online residual selection against the oracle-error upper bound on a small transformer checkpoint.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online KV residual selection for INT4 cache fidelity
- Success threshold: At 10% residual entries and under 50% FP16 KV memory, a deployable selector recovers at least 50% of the oracle-error improvement on heavy-tail or real-model KV traces and improves model-level loss versus plain INT4.
- Stop condition: Stop if deployable selectors improve heavy-tail or real-trace attention-output error by less than 25% versus plain INT4 or if model-level loss remains indistinguishable from plain INT4.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-int4-with-fp32-error-residual-buffers-42c66299e6f5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
