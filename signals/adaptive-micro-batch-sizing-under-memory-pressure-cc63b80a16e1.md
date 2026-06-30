# Adaptive Micro-batch Sizing Under Memory Pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-micro-batch-sizing-under-memory-pressure-cc63b80a16e1`
Run ID: `adaptive-micro-batch-sizing-under-memory-pressure-cc63b80a16e1-20260602T172038157511+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f49c5798ed28

## What looked useful

Adaptive headroom sizing completed 11844 samples with 0 failures; fixed-large completed 11520 samples with 36 failures and a 20% failure rate; fixed-small completed 2880 samples with 0 failures. Adaptive delivered 1.1606x fixed-small samples/s and 4.1125x fixed-small completed samples while retaining 98.2% of fixed-large samples/s.

## Boundaries and scale limits

No GPU, PyTorch, CUDA allocator, model training loop, convergence check, distributed setting, or production co-tenant pressure was tested. The result is mechanism evidence only, not full training-system validation.

## Claim scope

In a bounded CPU-only synthetic memory-pressure probe using a real process address-space cap, a headroom-based adaptive micro-batch policy avoided allocation failures and completed more work than fixed-small and fixed-large baselines on the tested pressure trace.

## Why it stopped

The local synthetic probe supports the controller mechanism but is not direct model-training or GPU evidence, so it should not be promoted to a paper result.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should run the same controller in a small real training loop with allocator telemetry and gradient-accumulation correctness checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive micro-batch sizing in a small real training loop
- Success threshold: Adaptive has zero or near-zero memory failures, at least 1.10x fixed-small completed examples per second, and no material loss-regression versus a successful fixed baseline over the bounded run.
- Stop condition: Stop if adaptive still fails under pressure, if throughput is not at least 1.10x fixed-small, or if loss trajectory diverges materially from the successful baseline.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-micro-batch-sizing-under-memory-pressure-cc63b80a16e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
