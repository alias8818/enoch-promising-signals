# CPU-RAM N-Gram Lookup Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-ram-n-gram-lookup-speculative-decoding-7e4f2c2b2713`
Run ID: `cpu-ram-n-gram-lookup-speculative-decoding-7e4f2c2b2713-20260524T184217552168+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f9430ef38bfa

## What looked useful

RAM lookup is cheap at about 60-138 ns per Python dict lookup and tables fit easily in memory, but naive global n-gram acceptance is too low. Best exact-match proxy was only 0.120-0.166 accepted tokens per block, giving an unrealistically draft-free upper-bound speedup of 1.12x-1.17x; best multi-token drafts were similarly weak.

## Boundaries and scale limits

No target LLM verifier, no tokenizer-matched model sampling, no GPU serving path, no large web/code corpus, and no end-to-end latency measurement. Corpora were Tiny Shakespeare and Pride and Prejudice with regex tokenization.

## Claim scope

Bounded CPU-only proxy test of a naive RAM-resident n-gram continuation table on two small natural-language corpora. The measured claim is lookup cost, held-out exact-token/block acceptance, and idealized draft-free target-call speedup, not end-to-end LLM speculative decoding.

## Why it stopped

Bounded proxy early falsification: the draft lookup is fast, but held-out exact-match acceptance is too low for meaningful speculative decoding speedup, and this is not a full LLM serving validation.

## Recommended next action

Stop this naive global n-gram version as a no-paper useful signal; only continue with a bounded direct small-LM verifier test if the research goal is narrowed to prompt-local or domain-specific repetition.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Direct Verification of Prompt-Local N-Gram Drafting
- Success threshold: At least 1.25x end-to-end tokens/second over no-draft on a bounded repetitive-text or code/log workload after including CPU draft overhead, with no sampling correctness regression.
- Stop condition: Stop if direct model-backed speedup is below 1.10x or if acceptance remains below 0.25 mean accepted draft tokens per target verification on the bounded workload.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-ram-n-gram-lookup-speculative-decoding-7e4f2c2b2713`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
