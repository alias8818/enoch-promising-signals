# Tiny Ternary Draft for CPU Spec-Decode

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-ternary-draft-for-cpu-spec-decode-d09308f38756`
Run ID: `tiny-ternary-draft-for-cpu-spec-decode-d09308f38756-20260608T045912183312+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4244dd767c13

## What looked useful

Best setting used threshold 0.75 sigma, temperature 1.0, and gamma 2: acceptance alpha 0.74245, expected tokens per target pass 2.2937, target verification median latency 51.13 us, draft median latency 13.00 us, predicted speedup 1.5204x, and 3.94x storage compression versus fp32 logits including row scale.

## Boundaries and scale limits

No real transformer, KV cache, tokenizer, production CPU inference stack, or learned ternary draft was tested. The draft was quantized from target logits, so the result is an optimistic mechanism probe rather than deployment evidence.

## Claim scope

In a controlled synthetic next-token distribution with 4096 contexts and 256-token vocabulary, an optimistic row-scaled ternary logits-table draft preserved enough probability mass and was cheap enough on CPU to predict speculative-decoding speedup versus a dense target-verification proxy.

## Why it stopped

Closed as no-paper useful signal: the proxy supports the mechanism but does not validate a real CPU LLM or learned ternary draft.

## Recommended next action

Run a bounded direct follow-up that trains a tiny ternary neural draft and measures exact CPU speculative decoding against a small transformer target, because this run is only a synthetic/proxy useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Tiny Ternary Draft Against a Small CPU Transformer
- Success threshold: At least 1.15x median wall-clock tokens/s over target-only decoding with acceptance alpha >= 0.65 and no worse than 5% task/perplexity degradation on the evaluated corpus.
- Stop condition: Stop if the learned ternary draft acceptance is below 0.55 or if draft overhead eliminates speedup on two independent CPU runs.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-ternary-draft-for-cpu-spec-decode-d09308f38756`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
