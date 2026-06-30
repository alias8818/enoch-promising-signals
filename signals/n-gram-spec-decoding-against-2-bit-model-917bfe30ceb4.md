# N-gram spec decoding against 2-bit model

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-spec-decoding-against-2-bit-model-917bfe30ceb4`
Run ID: `n-gram-spec-decoding-against-2-bit-model-917bfe30ceb4-20260528T233200932446+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/862178abae9a

## What looked useful

The acceptance mechanism is plausible locally: the 2-bit target accepted about 54% of proposed characters and reduced ideal target verification blocks by about 51.5% in the primary run. Quantization reduced efficiency versus the fp32 control, but did not erase the signal.

## Boundaries and scale limits

Proxy-only evidence: no neural 2-bit transformer weights, no BPE tokenizer, no real KV-cache verification implementation, and no end-to-end latency measurement. Results should not be generalized to production LLM serving without direct transformer tests.

## Claim scope

In a bounded character-level proxy on Tiny Shakespeare, an n-gram prompt/history lookup draft against a 2-bit quantized n-gram target achieved 2.06 generated tokens per verification block at block size 6, with the signal persisting from block sizes 2 through 12.

## Why it stopped

Closed as no-paper useful signal because the evidence is a bounded proxy rather than direct 2-bit transformer validation.

## Recommended next action

Run the same acceptance and latency measurement on an actual small 2-bit quantized transformer with its tokenizer before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct n-gram speculative decoding test on a small 2-bit transformer
- Success threshold: At least 1.25 generated tokens per target verification block and at least 10% end-to-end latency reduction versus naive greedy decoding on 100 or more held-out prompts.
- Stop condition: Stop as negative if tokens per verification block is below 1.1 or end-to-end speculative latency is not faster than naive decoding after overhead.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-spec-decoding-against-2-bit-model-917bfe30ceb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
