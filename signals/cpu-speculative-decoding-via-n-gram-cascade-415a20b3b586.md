# CPU Speculative Decoding via N-gram Cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-speculative-decoding-via-n-gram-cascade-415a20b3b586`
Run ID: `cpu-speculative-decoding-via-n-gram-cascade-415a20b3b586-20260530T032813438751+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8eee2585211c

## What looked useful

Across gamma 2, 4, and 8 medium runs, the best cascade reached 1.1644, 1.1946, and 1.1985 tokens per verifier call, beating the best fixed n-gram by 3.52%, 4.37%, and 4.38% respectively. Higher-order cascades did not help; the useful mechanism was bigram-to-unigram backoff.

## Boundaries and scale limits

This run did not use BPE tokens, a transformer verifier, target-model probability acceptance, or end-to-end CPU LLM serving. The measured 1.16-1.20 emitted tokens per verifier call is an idealized proxy, not a deployed decoding speedup.

## Claim scope

On a 250k-token public-domain text proxy with regex tokenization and held-out continuation verification, a deterministic bigram-to-unigram n-gram cascade improved ideal speculative verifier-call productivity over unigram and fixed-order n-gram drafters.

## Why it stopped

Proxy evidence is useful but insufficient for a paper or direct serving claim; this is not a full validation.

## Recommended next action

Run a bounded deepen experiment with GPT-2-small-class BPE tokens and a real CPU verifier to measure exact speculative acceptance and end-to-end wall-clock speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer CPU verifier test for n-gram cascade speculative decoding
- Success threshold: At least 5% end-to-end CPU tokens/second improvement over greedy decoding and at least 3% over the best fixed n-gram drafter on the same prompts, with no degradation in generated-token equivalence under exact speculative verification.
- Stop condition: Stop if BPE cascade acceptance remains below 1.10 emitted tokens per verifier call or end-to-end CPU speedup is under 2% after gamma/backoff tuning.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-decoding-via-n-gram-cascade-415a20b3b586`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
