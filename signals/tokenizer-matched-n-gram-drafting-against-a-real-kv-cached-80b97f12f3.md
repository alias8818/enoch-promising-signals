# Tokenizer-Matched N-Gram Drafting Against a Real KV-Cached Small LM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tokenizer-matched-n-gram-drafting-against-a-real-kv-cached-80b97f12f3`
Run ID: `tokenizer-matched-n-gram-drafting-against-a-real-kv-cached-80b97f12f3-20260629T181147652613+0000`

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

- Parent run decision: N-Gram Statistical Drafting with KV-Cache Window: enoch://control-plane/projects/n-gram-statistical-drafting-with-kv-cache-window-1d66be146fbc/runs/n-gram-statistical-drafting-with-kv-cache-window-1d66be146fbc-20260629T171047581398+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/101a628c8c88

## What looked useful

Order-5 tokenizer n-gram drafting accepted 810/8,192 target tokens and reached 9.53% to 9.77% ideal decode-call reduction at draft lengths 4-8. The unigram control accepted 845/8,192 target tokens and reached 10.13%, so the tokenizer-matched longer-context mechanism is not supported as a standalone improvement in this bounded test.

## Boundaries and scale limits

No production speculative decoder latency was implemented; results use ideal block-verifier call accounting and ignore draft overhead, cache slicing/copying, batched verification kernel behavior, and larger model/prompt distributions.

## Claim scope

On 128 WikiText-2 prompts and 8,192 greedy target tokens from CUDA KV-cached distilgpt2, tokenizer-ID n-gram draft proposals produced a small ideal verifier-call reduction, but max-order-5 n-gram backoff did not outperform an order-1 unigram control.

## Why it stopped

No-paper useful signal: direct KV-cached small-LM evidence showed only a small ideal call reduction, and the tokenizer-matched n-gram table underperformed the unigram control rather than validating the intended mechanism.

## Recommended next action

Stop this standalone n-gram drafting claim; only revisit with a direct latency implementation if a bounded follow-up first shows at least 25% ideal verifier-call reduction over unigram control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Domain-adaptive tokenizer n-gram drafting with direct verifier latency
- Success threshold: At least 25% ideal verifier-call reduction and a positive measured latency speedup over greedy KV decoding and unigram control on the same prompt suite.
- Stop condition: Stop if adaptive n-gram drafting remains below 25% ideal reduction or fails to beat unigram control after draft overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/tokenizer-matched-n-gram-drafting-against-a-real-kv-cached-80b97f12f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
