# Speculative decoding with n-gram suffix cache on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-n-gram-suffix-cache-on-cpu-3337954820dc`
Run ID: `speculative-decoding-with-n-gram-suffix-cache-on-cpu-3337954820dc-20260605T151835749189+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0797ab292fce

## What looked useful

The mechanism is real but modest: best longest-online K=8 reduced target calls by 12.84% while accepting only 2.73% of proposed tokens; a much cheaper online n=2 K=8 policy reached 12.36% reduction with about 0.52 microseconds mean Python lookup overhead per call.

## Boundaries and scale limits

No real LLM target, BPE tokenizer, KV-cache verification, or end-to-end CPU inference engine was tested. Results are natural-text trace replay only and cannot establish wall-clock decoding speedup.

## Claim scope

Trace-driven CPU proxy over 70,651 held-out word/punctuation tokens from three public-domain prose corpora shows that an n-gram suffix-cache draft can reduce speculative target verification calls by about 10% to 13%, with best observed aggregate reduction of 12.84%.

## Why it stopped

Proxy trace evidence supports only a modest call-count reduction and does not validate practical CPU speculative decoding speedup.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is direct integration with a small CPU LLM decoder to measure wall-clock tokens/s and target forward-pass reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrate n-gram suffix cache into a small CPU LLM speculative decoder
- Success threshold: At least 8% end-to-end tokens/s improvement over baseline CPU decoding on two natural prompt sets without changing generated tokens under greedy decoding, or clear evidence that verification overhead prevents the trace-level savings from materializing.
- Stop condition: Stop if a smoke integration shows less than 3% target-call reduction or any wall-clock slowdown greater than 5% after cache implementation overhead is measured.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-n-gram-suffix-cache-on-cpu-3337954820dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
