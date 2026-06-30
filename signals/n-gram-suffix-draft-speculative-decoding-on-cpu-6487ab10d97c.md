# N-gram Suffix Draft Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-draft-speculative-decoding-on-cpu-6487ab10d97c`
Run ID: `n-gram-suffix-draft-speculative-decoding-on-cpu-6487ab10d97c-20260601T051650841171+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/cc18260a7c1e

## What looked useful

Dynamic suffix-copy drafting is cheap in Python, generally 5-13 microseconds per draft in best configurations. Byte traces reached 2.03-2.33 idealized tokens per verifier call, subword4 proxy traces reached 1.25-1.32, and word/punctuation traces averaged only 1.13 in best rows. The mechanism is real versus random-copy controls but highly tokenization-dependent.

## Boundaries and scale limits

No real transformer, real tokenizer, logits verification, KV-cache behavior, or end-to-end CPU decoding latency was tested. Results are 20k-token held-out trace proxies on small public texts and should not be read as a production LLM speedup claim.

## Claim scope

Trace-level CPU benchmark on three public-domain/public text corpora shows that a dynamic suffix n-gram drafter can cheaply produce accepted continuations, with strong byte-token acceptance, modest subword-proxy acceptance, and weak word-token acceptance.

## Why it stopped

Proxy trace evidence is mixed and insufficient for a CPU speculative decoding paper; byte-level results are promising, but subword/word-level results and lack of real verifier timing prevent a practical speedup claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate the dynamic suffix drafter with a real CPU model runtime and tokenizer and require measured wall-clock speedup, not proxy call reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer CPU verifier test for dynamic suffix n-gram drafting
- Success threshold: At least 1.15x end-to-end tokens/sec over greedy decoding on repetitive prompts, geometric mean speedup above 1.05x across all prompt classes, and no prompt class slower than 0.95x greedy.
- Stop condition: Stop if actual-token acceptance is below 0.25 accepted tokens per verifier call or measured throughput is below 1.05x greedy on the first two repetitive prompt classes.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-draft-speculative-decoding-on-cpu-6487ab10d97c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
