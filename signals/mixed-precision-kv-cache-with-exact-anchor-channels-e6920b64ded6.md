# Mixed-precision KV cache with exact anchor channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mixed-precision-kv-cache-with-exact-anchor-channels-e6920b64ded6`
Run ID: `mixed-precision-kv-cache-with-exact-anchor-channels-e6920b64ded6-20260529T063753499265+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/05ed41879930

## What looked useful

Exact anchor channels are a measurable fidelity knob, reducing relative L2 error by 22.3% for mixed_int3_a8 versus int3 and 20.8% for mixed_int4_a8 versus int4, but the tested memory-neutral setting did not beat uniform int4.

## Boundaries and scale limits

CPU-only synthetic tensors; no trained model perplexity, generation-quality, packed-kernel latency, or real long-context serving validation. Uniform int4 remained substantially better than mixed int3 with exact anchors at a similar memory budget.

## Claim scope

In a synthetic NumPy attention-math probe with high-variance anchor channels, retaining selected KV channels in fp16 improves attention-output fidelity versus quantizing all channels at the same non-anchor bit width.

## Why it stopped

Closed as no-paper useful signal: bounded synthetic evidence supports the mechanism but does not support a memory-neutral or publication-grade advantage.

## Recommended next action

Run a bounded GPT-2-small-class KV-cache evaluation comparing uniform int4 against mixed exact-anchor formats on perplexity, decode quality, memory, and packed-kernel latency before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model perplexity test for exact-anchor mixed KV cache
- Success threshold: Mixed exact-anchor format achieves lower perplexity loss or attention-output error than uniform int4 with <=5% KV memory overhead and <=10% decode latency overhead on a reproducible small-model benchmark.
- Stop condition: Stop if the mixed format cannot beat uniform int4 under the memory/latency thresholds or if anchor selection is unstable across layers/prompts.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-kv-cache-with-exact-anchor-channels-e6920b64ded6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
