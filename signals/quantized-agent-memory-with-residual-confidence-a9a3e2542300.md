# Quantized Agent Memory with Residual Confidence

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `quantized-agent-memory-with-residual-confidence-a9a3e2542300`
Run ID: `quantized-agent-memory-with-residual-confidence-a9a3e2542300-20260525T113531071549+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a884e882bba0

## What looked useful

Across a 2,000-memory clustered benchmark, quantization caused no retrieval failures and confidence selected alpha=0. In harder unique-memory stress tests, quantization caused errors, but confidence produced zero or slightly negative mean recall/MRR deltas versus naive quantization.

## Boundaries and scale limits

Synthetic static vectors only; no real agent traces, no natural-language embedding corpus, no learned confidence model, no downstream task evaluation, and no large-model or online-memory validation.

## Claim scope

A simple residual quantization-error confidence penalty did not improve synthetic embedding-memory retrieval over naive scalar-quantized memory in the tested CPU-bounded benchmarks.

## Why it stopped

Proxy/early falsification: the simple residual-confidence scoring mechanism failed to improve held-out synthetic retrieval, so the current idea is not viable as a paper claim from this run.

## Recommended next action

Stop this mechanism as no-paper evidence; only revisit with a bounded direct benchmark using real embedding traces or a learned uncertainty model rather than the scalar residual-error penalty tested here.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual Confidence on Real Agent Embedding Traces
- Success threshold: Residual confidence improves held-out recall@1 or downstream correctness by at least 2 percentage points over naive quantization at the same bit width without more than a 1 percentage point recall@5 loss.
- Stop condition: Stop if residual confidence fails to beat naive quantization on two real-trace datasets or if gains disappear under held-out calibration.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-agent-memory-with-residual-confidence-a9a3e2542300`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
