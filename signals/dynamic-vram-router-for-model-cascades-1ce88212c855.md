# Dynamic VRAM Router for Model Cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dynamic-vram-router-for-model-cascades-1ce88212c855`
Run ID: `dynamic-vram-router-for-model-cascades-1ce88212c855-20260519T190616995559+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b5bc4b826607

## What looked useful

Across 40 seeds x 5000 requests at a 24 GB simulated budget, vram_aware achieved 0.7133 mean quality/all requests and 0.99995 SLO rate versus confidence_only at 0.6572 and 0.8926; p95 latency was 78.1 ms versus 1148.7 ms, evictions were 0.25 versus 894.6, and OOM fallbacks were 0 versus 53.1 per seed. A 16/20/24/28 GB budget sweep preserved +7.51% to +14.19% quality improvement and +7.53 to +11.10 SLO percentage-point improvement versus confidence_only.

## Boundaries and scale limits

No real models, real token throughput, real answer-quality benchmark, production batching, concurrent KV-cache growth, or hardware VRAM allocation telemetry were tested. Results are simulator-only and should not be treated as deployment or paper-grade validation.

## Claim scope

In a deterministic synthetic cascade simulator with shifted request difficulty and bursty external VRAM pressure, a VRAM-aware router improved proxy quality and SLO hit rate versus a confidence-only cascade by avoiding load churn and infeasible model choices.

## Why it stopped

No-paper closure: this run produced useful simulator evidence, but it is proxy-only rather than direct validation on real model serving.

## Recommended next action

Run a bounded real-runtime follow-up with two or three small local Hugging Face models, actual memory/load telemetry, and a fixed task-quality benchmark before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-runtime VRAM-aware cascade replay with small local models
- Success threshold: VRAM-aware routing improves quality at the fixed SLO by at least 5% relative to confidence-only routing while reducing OOM/fallback or model reload events by at least 50% across three seeds or trace shards.
- Stop condition: Stop if real measured load/memory telemetry does not reproduce the simulator mechanism, or if quality-at-SLO is within 2% of confidence-only while adding router complexity.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-vram-router-for-model-cascades-1ce88212c855`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
