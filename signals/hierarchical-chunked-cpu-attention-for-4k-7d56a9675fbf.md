# Hierarchical Chunked CPU Attention for 4K

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-chunked-cpu-attention-for-4k-7d56a9675fbf`
Run ID: `hierarchical-chunked-cpu-attention-for-4k-7d56a9675fbf-20260523T221345613440+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4550ade894df

## What looked useful

At n=4096, random Q/K/V remained poorly approximated by both local and hierarchical methods (hierarchical mean cosine 0.158-0.255). On chunk-latent inputs, local and hierarchical methods reached high mean cosine (0.990-0.998), but hierarchical summaries added negligible accuracy and reduced speedup versus local-only.

## Boundaries and scale limits

No language-model training, no real transformer Q/K/V traces, no causal multi-head evaluation, no perplexity/task metric, and no learned/adaptive summary mechanism were tested.

## Claim scope

On synthetic 4096-token CPU forward-pass attention with d=64, a simple hierarchy using one mean key/value summary per chunk does not materially improve approximation quality over block-local attention enough to justify its overhead; block-local attention is very fast and accurate only when inputs are already chunk-local.

## Why it stopped

Proxy/synthetic evaluation falsified the simple mean-summary hierarchy as a clear CPU attention improvement over local-only; this is not a full model-quality validation.

## Recommended next action

Stop this run as a bounded useful-signal negative for mean-summary hierarchy; next, evaluate local-only versus learned or adaptive summary tokens on saved real transformer Q/K/V traces at 4K.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-based CPU attention comparison for learned or adaptive chunk summaries
- Success threshold: Adaptive summaries improve mean cosine by at least 0.05 absolute over local-only on non-local heads while keeping at least 5x speedup over exact 4096-token CPU attention.
- Stop condition: Stop if adaptive summaries fail to improve mean cosine by 0.02 absolute over local-only on real traces or if speedup drops below 3x.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-chunked-cpu-attention-for-4k-7d56a9675fbf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
