# Cross-layer KV sharing cuts CPU RAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cross-layer-kv-sharing-cuts-cpu-ram-b8fed4815209`
Run ID: `cross-layer-kv-sharing-cuts-cpu-ram-b8fed4815209-20260523T173334565225+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ba0aaaf3c26

## What looked useful

A reproducible local benchmark measured 75.0% RSS reduction for 4-layer sharing groups and 87.5% RSS reduction for 8-layer sharing groups on a 32-layer KV-cache proxy, with aliasing checks confirming shared backing storage.

## Boundaries and scale limits

This run used synthetic byte-addressable KV-cache allocations shaped like transformer caches. It did not run a real transformer, did not test perplexity or accuracy, did not test serving latency, and did not validate whether model layers can semantically tolerate shared K/V states.

## Claim scope

For CPU-resident transformer KV-cache storage, grouped cross-layer sharing of backing KV allocations reduces measured process RSS almost exactly according to the number of unique sharing groups, demonstrated up to a 32-layer, 1 GiB standard-cache proxy.

## Why it stopped

Stopped after a bounded allocation-mechanism validation: the CPU RAM saving is supported, but the evidence is proxy-only and not sufficient for a paper or broad model-quality claim.

## Recommended next action

Run a bounded real-model follow-up that patches a small transformer decoder to use grouped cross-layer KV cache sharing and measures memory, perplexity, and decode latency against a standard cache baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer cross-layer KV sharing quality and latency check
- Success threshold: At least 50% measured KV-cache RSS reduction versus standard cache, no more than 10% decode throughput loss, and no more than 5% relative perplexity degradation on the selected small workload.
- Stop condition: Stop if the shared-KV model exceeds 5% relative perplexity degradation, loses more than 10% decode throughput, or fails to reproduce at least 50% RSS reduction.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-sharing-cuts-cpu-ram-b8fed4815209`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
