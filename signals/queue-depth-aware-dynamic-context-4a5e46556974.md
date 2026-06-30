# Queue-Depth Aware Dynamic Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-depth-aware-dynamic-context-4a5e46556974`
Run ID: `queue-depth-aware-dynamic-context-4a5e46556974-20260602T102413519858+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/18f8c2625857

## What looked useful

Dynamic context reduced p95 latency versus always-full context by 27.7%-99.8% across 12 scenarios while losing 1.4%-30.2% synthetic utility; it passed a 75 ms proxy p95 SLA in all scenarios and preserved 0.698-0.986 mean utility, above static medium's 0.642 and static short's 0.383. Static medium/short remained much faster, so the mechanism is useful only when higher retained-context utility is worth latency near the SLO.

## Boundaries and scale limits

No real serving engine, batching scheduler, KV-cache paging, tokenizer/model quality evaluation, or downstream task accuracy was measured. CUDA evidence is a one-layer prefill proxy, and utility is synthetic retained-context utility.

## Claim scope

In a local synthetic single-server queue simulation grounded by a small GB10 CUDA prefill attention cost curve, queue-depth-aware dynamic context kept p95 latency near 65-70 ms across bursty/high-load scenarios and retained higher synthetic context utility than static 1024/2048-token policies, but it did not dominate fixed shorter-context baselines on latency.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a simulation plus CUDA cost proxy, not direct model-serving quality evidence.

## Recommended next action

Run a bounded direct serving-engine validation with vLLM or SGLang using a small open model, real long-context tasks, and the same full/medium/short/dynamic policy controls at matched p95 latency SLOs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Serving Validation Of Queue-Depth Dynamic Context
- Success threshold: Dynamic policy meets the target p95 latency SLO and improves measured task quality by at least 5% relative to the best static context baseline that also meets the SLO, without reducing throughput by more than 5%.
- Stop condition: Stop if dynamic fails the p95 latency SLO, fails to improve measured quality over the best SLO-satisfying static baseline, or causes unstable GPU memory/queue behavior in two independent traces.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-aware-dynamic-context-4a5e46556974`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
