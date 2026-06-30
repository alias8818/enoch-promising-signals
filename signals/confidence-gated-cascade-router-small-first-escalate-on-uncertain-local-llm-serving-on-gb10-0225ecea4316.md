# Confidence-gated cascade router: small-first, escalate-on-uncertain local LLM serving on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-cascade-router-small-first-escalate-on-uncertain-local-llm-serving-on-gb10-0225ecea4316`
Run ID: `confidence-gated-cascade-router-small-first-escalate-on-uncertain-local-llm-serving-on-gb10-0225ecea4316-20260619T164406254316+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c1312b6fa4da

## What looked useful

The 0.5B-to-3B cascade escalated 48.4% of examples, saved 51.6% of fallback calls, achieved 0.609 accuracy versus 0.625 for all-3B, and reduced modeled mean latency to 0.123s versus 0.164s for all-3B. The 0.5B-to-1.5B cascade escalated 66.0%, achieved 0.578 accuracy versus 0.594 for all-1.5B, but was slower than all-1.5B at 0.102s versus 0.090s, showing fallback cost must be sufficiently high.

## Boundaries and scale limits

Results are limited to cached local Qwen models, HellaSwag multiple-choice logprob scoring, max length 384, sequential batch-1 inference, one random seed, no production HTTP server, no continuous batching, no free-form generation, and no broad task mix.

## Claim scope

On GB10, a BF16 Qwen2.5-0.5B-Instruct first pass with a margin confidence gate can reduce sequential modeled latency and fallback calls for a Qwen2.5-3B-Instruct fallback on a 128-example HellaSwag multiple-choice scoring sample, but the same approach was not latency-beneficial for a Qwen2.5-1.5B-Instruct fallback on a 256-example sample.

## Why it stopped

No-paper bounded useful signal: direct GB10 proxy evidence supports the mechanism only for a sufficiently expensive fallback and does not validate production local LLM serving.

## Recommended next action

Run a direct serving follow-up with an actual local serving stack, continuous batching enabled, train/dev threshold selection, and a larger mixed benchmark to test whether the 3B fallback benefit survives production-style latency and quality metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-style GB10 cascade serving benchmark with calibrated confidence gates
- Success threshold: At least 20% p95 latency reduction or throughput improvement versus all-3B fallback, at least 40% fallback-call reduction, and no more than 2 percentage points quality loss on the held-out test set.
- Stop condition: Stop if calibrated thresholds cannot beat all-fallback latency/throughput at <=2 percentage point quality loss, or if serving overhead erases the proxy benefit on two benchmark families.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-cascade-router-small-first-escalate-on-uncertain-local-llm-serving-on-gb10-0225`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
