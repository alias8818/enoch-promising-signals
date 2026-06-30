# N-gram suffix tree speculative CPU decode

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `n-gram-suffix-tree-speculative-cpu-decode-5bd10b6781fd`
Run ID: `n-gram-suffix-tree-speculative-cpu-decode-5bd10b6781fd-20260604T193814914474+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/59bc0e094268

## What looked useful

Best GPT-2 BPE run used order 8, min_count 2, 1.8M train-token cap, and 374,904 contexts; block-8 mean accepted prefix was 0.4445, zero-accept rate 0.73835, full-block accept rate 0.0014, ideal speedup upper bound 1.4445x, and conservative 1.5x verification-cost speedup 0.963x. Regex-token runs saturated near 0.34 mean accepted tokens. Byte-token run reached 1.4937 mean accepted tokens but is not representative of LLM-token speculative decode.

## Boundaries and scale limits

No live LLM target model, no exact stochastic speculative sampling, no measured CPU transformer block-verification latency, one public corpus, and local CPU-only runs up to 1.8M BPE train tokens and 20k held-out sampled positions.

## Claim scope

On WikiText-2 token-stream proxy tests, longest-suffix n-gram drafting did not provide enough consecutive GPT-2 BPE-token acceptance for practical CPU speculative decoding under a modest block-verification overhead model; byte-level streams are much more predictable but are not representative of LLM token decoding.

## Why it stopped

Proxy early falsification: decision-relevant GPT-2 BPE token-stream tests missed the predefined acceptance threshold and remained below conservative breakeven after verification overhead; this is not a full live-serving validation.

## Recommended next action

Stop this line as a paper candidate; only revisit with a live small CPU LLM end-to-end speculative decoding benchmark if exact target-model acceptance and measured verification latency are required to challenge the proxy negative.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-cpu-decode-5bd10b6781fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
