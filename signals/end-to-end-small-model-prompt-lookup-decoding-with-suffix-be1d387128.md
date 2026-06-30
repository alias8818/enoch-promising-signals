# End-to-end small-model prompt lookup decoding with suffix index

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-small-model-prompt-lookup-decoding-with-suffix-be1d387128`
Run ID: `end-to-end-small-model-prompt-lookup-decoding-with-suffix-be1d387128-20260605T120254068998+0000`

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

- Parent run decision: Prompt Lookup Decoding with Suffix Cache: enoch://control-plane/projects/prompt-lookup-decoding-with-suffix-cache-cc2712f10e5c/runs/prompt-lookup-decoding-with-suffix-cache-cc2712f10e5c-20260605T045231100342+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2580c6b3cea7

## What looked useful

Repeated phrase and repeated code prompts achieved exact-match median speedups of 5.95x and 4.24x with 83.33% and 77.08% forward-call reductions; the random control also improved 1.50x from incidental short suffix reuse, so boundary conditions need broader characterization.

## Boundaries and scale limits

Only one small model, three constructed prompts, 48 generated tokens, greedy decoding, and a non-production benchmark harness were tested; no batched serving, sampling, KV-cache integration, natural prompt corpus, larger models, or long-context overhead study was performed.

## Claim scope

In a controlled Tier 1 small-model greedy-decoding test with distilgpt2 on three constructed prompts, suffix-index prompt lookup decoding preserved exact greedy output and improved median wall-clock throughput on repeated prompts.

## Why it stopped

Tier 1 direct evidence supports the mechanism but remains too narrow and constructed for publication readiness.

## Recommended next action

Run one bounded deepen follow-up on a small real-prompt corpus with suffix-length/lookahead ablations and an explicit control for incidental repetition before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-corpus suffix-index prompt lookup decoding ablation
- Success threshold: Exact output equality for every prompt; repeated-context median speedup >= 2.0x with p90 speedup >= 1.3x; non-repeated-control median speedup <= 1.2x or a clear diagnostic explaining useful control speedups.
- Stop condition: Stop as no-paper negative if exactness fails, index overhead erases repeated-context median speedup below 1.3x, or non-repeated controls show similar speedups without a separable repetition diagnostic.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-small-model-prompt-lookup-decoding-with-suffix-be1d387128`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
