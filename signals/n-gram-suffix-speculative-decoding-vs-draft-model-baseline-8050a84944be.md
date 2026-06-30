# N-gram Suffix Speculative Decoding vs Draft Model Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-speculative-decoding-vs-draft-model-baseline-8050a84944be`
Run ID: `n-gram-suffix-speculative-decoding-vs-draft-model-baseline-8050a84944be-20260619T220902031628+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7fe93baac7cb

## What looked useful

Suffix n-gram lookup is cheap and useful for repeated/copy-heavy traces, but the broad claim versus a competent draft-model baseline is unsupported: order-3 draft Markov had higher target-call reduction in all primary scenarios and seeds.

## Boundaries and scale limits

No neural draft model, real LLM target, tokenizer, GPU serving stack, batching, KV-cache behavior, or sampling-quality effects were tested. Evidence is mechanism-level and synthetic/proxy only.

## Claim scope

In a controlled deterministic token-trace proxy with 20k-token synthetic traces, max proposal length 8, five seeds, and online verification accounting, indexed suffix n-gram speculation did not beat an order-3 draft-like Markov baseline on target-call reduction, though it beat a weaker unigram draft on copy-heavy traces.

## Why it stopped

Proxy evidence rejects the broad comparison at this tier rather than providing full validation; a real-model serving benchmark would be required to overturn it.

## Recommended next action

Stop this run as a no-paper useful signal; only pursue a follow-up if it directly benchmarks suffix lookup against a real neural draft model in an LLM serving loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model serving benchmark for suffix n-gram speculation vs neural draft decoding
- Success threshold: Suffix n-gram must improve end-to-end tokens/s by at least 10% over the neural draft baseline on copy-heavy prompts without regressing non-copy prompts by more than 5%.
- Stop condition: Stop if suffix n-gram fails to beat the neural draft baseline in target-call reduction or end-to-end tokens/s on copy-heavy prompts after overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-speculative-decoding-vs-draft-model-baseline-8050a84944be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
