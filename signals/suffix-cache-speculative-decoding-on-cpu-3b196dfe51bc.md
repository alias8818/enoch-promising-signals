# Suffix-Cache Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-cache-speculative-decoding-on-cpu-3b196dfe51bc`
Run ID: `suffix-cache-speculative-decoding-on-cpu-3b196dfe51bc-20260609T012312945132+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3202d22de330

## What looked useful

On 12,800-block synthetic traces, exact-key suffix caching was slower at 9.8% hit rate (0.886x), faster at 34.7% hit rate (1.344x), and much faster at 69.8% hit rate (2.597x to 3.436x). A high context-reuse but unique-draft control had 0% hits and no meaningful speedup, indicating the mechanism depends on repeated verifier keys rather than repeated prompt tails alone.

## Boundaries and scale limits

No real language model, no real draft model, no production prompt trace, no KV-cache memory measurement, and no end-to-end serving stack. The evidence should not be generalized beyond the controlled CPU proxy benchmark.

## Claim scope

Synthetic CPU verifier proxy only: exact suffix-cache reuse keyed by context suffix plus draft block can reduce verifier calls and improve wall-clock time when repeated verifier keys are common.

## Why it stopped

Proxy-only evidence supports a conditional mechanism but is insufficient for a paper or broad validation.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded real-model CPU follow-up only if exact verifier-key reuse can be measured on realistic traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU suffix-cache speculative decoding on repeated prompt traces
- Success threshold: At least 1.20x end-to-end tokens/s over standard speculative decoding at >=30% exact verifier-key hit rate, with identical accepted outputs and less than 10% additional memory overhead for the tested model size.
- Stop condition: Stop if realistic traces show <10% exact verifier-key reuse, if cache overhead makes throughput <=1.05x at >=30% hits, or if cached outputs diverge from the uncached verifier.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-cache-speculative-decoding-on-cpu-3b196dfe51bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
