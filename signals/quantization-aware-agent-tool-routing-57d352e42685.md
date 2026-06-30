# Quantization-Aware Agent Tool Routing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantization-aware-agent-tool-routing-57d352e42685`
Run ID: `quantization-aware-agent-tool-routing-57d352e42685-20260528T230131015982+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4b7f37f21ef6

## What looked useful

Across 20 seeds, full precision averaged 0.7704 accuracy. A 2-bit quantized router fell to 0.7085 accuracy, while margin-gated fallback recovered 0.7694 accuracy with 39.04% fallback and 0.5428 modeled relative cost; the gate captured 77.91% of quantized errors and beat expected random fallback by 0.0642 accuracy. At 3-bit the signal was smaller, and at 4/8-bit fallback had little practical value on this proxy.

## Boundaries and scale limits

Proxy-only evidence: synthetic utterances, single-label tool choice, Naive Bayes scoring tables, and modeled relative cost. No real agent traces, transformer router, quantized model serving, latency, memory, or end-to-end task success were measured.

## Claim scope

On a synthetic eight-tool natural-language routing benchmark with a Naive Bayes router and simulated low-bit score-table quantization, quantized score-margin gating identifies fragile routing decisions and can recover near full-precision accuracy for severe 2-bit quantization at lower modeled cost than all-full-precision scoring.

## Why it stopped

Bounded proxy evidence supports the mechanism but is not direct/full validation for real agent tool routing.

## Recommended next action

Stop this worker run as a no-paper useful-signal result; next run should test the same margin-gated fallback policy on a small quantized transformer or embedding router with real or curated agent tool-call traces and measured serving cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based Quantized Router Margin Fallback
- Success threshold: Recover at least 90% of the full-precision versus quantized-only accuracy gap with at least 25% measured routing-cost reduction versus all-full-precision routing, and beat random fallback at the same fallback rate by at least 2 accuracy points.
- Stop condition: Stop as negative if margin-gated fallback fails to beat random fallback by 2 accuracy points or if measured cost reduction is below 25% at the accuracy target.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-aware-agent-tool-routing-57d352e42685`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
