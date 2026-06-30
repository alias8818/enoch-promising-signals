# CPU N-Gram Speculative Decode with Exact Parity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decode-with-exact-parity-3b29f973824a`
Run ID: `cpu-n-gram-speculative-decode-with-exact-parity-3b29f973824a-20260604T043840741684+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d1eff6718125

## What looked useful

Across 192 configurations all runs preserved exact parity. Best verifier-call reduction was 93.8% on repetitive code-like traces, 60.4% on Markov topic traces, 51.1% on repeated prompt text, and 0% on random adversarial traces.

## Boundaries and scale limits

No real LLM runtime, logits, tokenizer, KV-cache, or wall-clock model verification was tested; results use oracle target traces and a verifier-call cost proxy over 2400-token continuations.

## Claim scope

Trace-level CPU n-gram speculative decoding can preserve exact target-token parity and reduce verifier calls on repetitive and locally structured token streams, while failing closed with no speedup on adversarial random streams.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a trace/oracle proxy, not direct model-serving validation.

## Recommended next action

Run a bounded real-runtime deepen test in llama.cpp or an equivalent CPU LLM backend with greedy decoding, exact baseline parity checks, and wall-clock latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM N-Gram Speculative Decode Parity and Latency Test
- Success threshold: At least 20% end-to-end tokens/sec improvement on structured prompts with 100% token parity and no more than 5% slowdown on low-repetition controls.
- Stop condition: Stop if exact parity fails, if proposer overhead eliminates wall-clock gains on structured prompts, or if low-repetition prompts show more than 5% slowdown.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decode-with-exact-parity-3b29f973824a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
