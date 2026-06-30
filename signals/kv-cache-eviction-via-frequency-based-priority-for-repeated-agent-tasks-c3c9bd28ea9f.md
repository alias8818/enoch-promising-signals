# KV Cache Eviction via Frequency-Based Priority for Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-eviction-via-frequency-based-priority-for-repeated-agent-tasks-c3c9bd28ea9f`
Run ID: `kv-cache-eviction-via-frequency-based-priority-for-repeated-agent-tasks-c3c9bd28ea9f-20260611T155534884836+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4ab3cbe94cf3

## What looked useful

Across four synthetic scenarios and five capacities, frequency-priority improved token-hit ratio versus LRU by +0.072 to +0.145 and saved roughly +0.56M to +1.44M prefill tokens per run, but was mixed versus LFU with deltas from -0.019 to +0.012. Alpha sensitivity showed size normalization can shift retention from task blocks toward tool blocks without robustly improving total token hits.

## Boundaries and scale limits

Single-process CPU simulator only; no real LLM serving stack, GPU KV cache, production traces, scheduler effects, TTFT/throughput measurements, or multi-tenant workload validation.

## Claim scope

Synthetic repeated-agent KV-block traces show that frequency-aware eviction substantially improves token-weighted cache hits over LRU/FIFO at equal KV-token capacity, but the tested size-normalized frequency-priority formula does not reliably beat plain LFU.

## Why it stopped

Bounded synthetic evidence supports frequency awareness versus LRU but does not support the stronger claim that the proposed frequency-priority policy is better than a simple LFU baseline.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate LFU and tuned frequency-priority policies into a real serving trace replay or vLLM/SGLang-style KV manager and require direct TTFT/throughput evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Real Agent Traces Through LFU and Tuned Frequency-Priority KV Eviction
- Success threshold: At least +3 percentage points token-hit ratio or at least 5% TTFT reduction versus LFU on repeated-agent and phase-shift traces, with no more than 1 percentage point token-hit regression on low-reuse controls.
- Stop condition: Stop if tuned frequency-priority fails to beat LFU on token-hit ratio in real trace replay at two or more cache capacities, or if serving overhead erases the hit-rate benefit.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-eviction-via-frequency-based-priority-for-repeated-agent-tasks-c3c9bd28ea9f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
