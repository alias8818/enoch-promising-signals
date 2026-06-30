# Static prefix draft table for zero-VRAM speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `static-prefix-draft-table-for-zero-vram-speculation-427a70a02721`
Run ID: `static-prefix-draft-table-for-zero-vram-speculation-427a70a02721-20260604T183632827576+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/75e50da5e1f9

## What looked useful

The mechanism exists but is narrow: compact static tables can draft repeated continuations, but useful reductions were modest and came from very short word prefixes or character-level repetition. High exact acceptance with longer prefixes collapsed in coverage, so it did not translate into large verifier-call reduction.

## Boundaries and scale limits

Evidence is corpus-oracle proxy evidence only, not acceptance under a real target LLM speculative decoding rule and not an end-to-end latency benchmark. Corpora were Tiny Shakespeare and Alice in Wonderland; no 7B-class model, GPU serving stack, or production tokenizer was tested.

## Claim scope

On two small public text corpora, static prefix-to-continuation tables trained on earlier tokens produced modest held-out exact-token draft acceptance with zero model VRAM: best proxy verifier-call reduction was about 10.9-15.5% for word/punctuation tokens and about 16.7% for character tokens.

## Why it stopped

Proxy-only early evaluation found only modest verifier-call reduction and no direct target-LLM decoding evidence, so the broad zero-VRAM speculation claim is not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should evaluate the same static-table proposal against a small real target-model decoding trace and include lookup overhead plus verifier batching latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Static prefix table acceptance against a small target LLM trace
- Success threshold: At least 10% median end-to-end tokens/sec improvement on a repetitive held-out domain with no quality regression and table storage under 10 MB.
- Stop condition: Stop if target-model acceptance yields under 5% verifier-call reduction or lookup plus verification overhead eliminates throughput gain on the small-model benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/static-prefix-draft-table-for-zero-vram-speculation-427a70a02721`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
