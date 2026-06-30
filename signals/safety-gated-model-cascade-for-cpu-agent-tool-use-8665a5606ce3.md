# Safety-Gated Model Cascade for CPU Agent Tool-Use

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `safety-gated-model-cascade-for-cpu-agent-tool-use-8665a5606ce3`
Run ID: `safety-gated-model-cascade-for-cpu-agent-tool-use-8665a5606ce3-20260526T013821014267+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/09eea6a20198

## What looked useful

A conservative lexical veto plus low-margin escalation can cheaply remove obvious unsafe tool requests in a CPU-local cascade, but model-only escalation was insufficient under template shift and utility degraded through safe over-blocking.

## Boundaries and scale limits

Synthetic text requests only; no real LLM tool calls, no multi-turn traces, no human-reviewed production labels, and no adversarial red-team set. The selected cascade over-blocked shifted safe requests at 50.5%, so the result is not production-ready or paper-positive.

## Claim scope

On a 3,000 train / 1,600 test synthetic single-turn CPU tool-use safety benchmark, a veto-capable safety-gated cascade reduced unsafe passes from 4.875% for the cheap classifier and 9.625% for the stronger classifier to 0.0%, while escalating 5.875% of requests and averaging 83.11 microseconds per request.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and shows a safety-utility tradeoff rather than direct production validation.

## Recommended next action

Run a bounded deepen study on real or realistic logged agent tool-call requests with human-reviewed labels, comparing veto-only, model-only escalation, and veto-plus-escalation cascades.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Validation of Veto-Capable CPU Tool-Use Safety Cascades
- Success threshold: Unsafe pass rate reduced by at least 80% relative to cheap classifier, absolute unsafe pass rate below 1%, safe block rate below 10%, and escalation rate below 30%.
- Stop condition: Stop as negative if the cascade cannot beat cheap-only unsafe pass rate by at least 50% without exceeding 20% safe block rate on the labeled trace set.

## Evidence references

- Artifact root: `<local-path>/projects/safety-gated-model-cascade-for-cpu-agent-tool-use-8665a5606ce3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
