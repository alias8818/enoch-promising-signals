# CPU N-Gram Draft with KV Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-draft-with-kv-quantization-ac8c5168c797`
Run ID: `cpu-n-gram-draft-with-kv-quantization-ac8c5168c797-20260609T021906199524+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0a636c0a9ba4

## What looked useful

A Python CPU n-gram drafter reached 638k evaluated positions/s and 92.6% first-token coverage, but only 16.1% of positions accepted at least one token and the upper-bound verifier yield was 1.228 tokens/call. Int8/int4 KV cache accounting saves 48.4%/73.4% memory versus fp16 under the stated scale-overhead model.

## Boundaries and scale limits

No transformer verifier was run with quantized KV; no end-to-end speculative decoding throughput, output quality, attention error, GPU kernel, or large-model evidence was produced. Results use up to 200k train tokens and 50k evaluated positions.

## Claim scope

Bounded local probe on Wikitext-2 raw train text using GPT-2 BPE tokens: CPU n-gram tables can draft exact next tokens cheaply, but acceptance depth is shallow; KV quantization memory savings are analytical only.

## Why it stopped

Proxy/early bounded result: n-gram drafting mechanism was directly measured, but quantized-KV serving was only analytically accounted for and the draft acceptance is too shallow to support a paper claim.

## Recommended next action

Run one bounded deepen test with a GPT-2-small-class GPU verifier, real speculative decoding, and an actual quantized-KV path; stop here for this proxy run because it is not paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2 verifier test for CPU n-gram drafting with quantized KV
- Success threshold: At least 10% end-to-end tokens/s improvement over the fp16-KV baseline on the same prompts with no material quality regression and measured acceptance >=1 token on at least 15% of verifier steps.
- Stop condition: Stop as negative if real verifier integration delivers less than 5% tokens/s improvement or if int8 KV causes visible quality/divergence failures on the bounded prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-with-kv-quantization-ac8c5168c797`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
