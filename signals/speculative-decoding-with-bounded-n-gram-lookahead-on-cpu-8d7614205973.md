# Speculative decoding with bounded n-gram lookahead on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-bounded-n-gram-lookahead-on-cpu-8d7614205973`
Run ID: `speculative-decoding-with-bounded-n-gram-lookahead-on-cpu-8d7614205973-20260611T041402560016+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c3a6d8866078

## What looked useful

Exact n-gram lookahead can provide large call reductions on repetitive text, but natural word-token traces only reached about 1.05-1.15 emitted tokens per verification call and fail the CPU proxy break-even. Natural byte-token traces reached 1.50-1.76 emitted tokens per call and 1.07-1.25x proxy speedup, suggesting a narrow BPE/byte-level follow-up but not a paper-ready result.

## Boundaries and scale limits

No real transformer, KV cache, GPT/BPE tokenizer, logits, sampling, or end-to-end serving latency was measured. Natural corpora were Alice and Tiny Shakespeare with up to 30000 evaluated tokens per case.

## Claim scope

Causal trace benchmark of exact bounded n-gram lookahead on CPU-worker corpora, plus a NumPy CPU verification-cost proxy. The mechanism is supported for repeat-heavy traces but not for broad natural-language word-token traces.

## Why it stopped

Proxy/trace evidence is mixed: repeat-heavy controls support the mechanism, but natural word-token traces are negative and natural byte-token gains are not direct full-serving validation.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next action is a bounded real-model CPU benchmark with GPT-2 BPE tokens, KV cache, and end-to-end latency on natural and repetition-heavy corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU small-LM benchmark for n-gram speculative decoding
- Success threshold: At least 1.15x end-to-end CPU tokens/s improvement on two corpora with unchanged greedy outputs and no more than 10% memory overhead.
- Stop condition: Stop if BPE-token accepted drafts remain below 1.25 emitted tokens per verification call or measured end-to-end speedup is below 1.05x on all natural/repetition-heavy corpora.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-bounded-n-gram-lookahead-on-cpu-8d7614205973`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
