# Character n-gram draft model for CPU speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `character-n-gram-draft-model-for-cpu-speculative-decoding-da88ab9fa66a`
Run ID: `character-n-gram-draft-model-for-cpu-speculative-decoding-da88ab9fa66a-20260528T002421043908+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0b5705bd13e5

## What looked useful

Order-6/8 character n-grams reached 2.28 proxy chars per verifier call on Tiny Shakespeare and 2.56 on Alice at gamma=8, about 1.98x and 2.19x unigram baseline respectively, with sub-minute CPU runs and <=357 MB peak RSS. Full gamma=8 acceptance remained low at 1.34% and 2.75%, limiting direct speedup claims.

## Boundaries and scale limits

No real LLM verifier, no tokenizer-boundary integration, no distributional equivalence check, no end-to-end serving latency measurement, and only two small/medium English text corpora were tested.

## Claim scope

Bounded CPU proxy on two real text corpora: greedy character n-gram draft models improve exact-prefix continuation prediction over trivial baselines and run cheaply in pure Python.

## Why it stopped

Proxy evidence supports a cheap short-prefix mechanism but does not validate end-to-end speculative decoding; this is a no-paper useful signal rather than a publication-grade result.

## Recommended next action

Run a bounded deepen test that wires the n-gram draft through a real tokenizer and a small local causal LM verifier, measuring actual tokens/sec, verifier calls, acceptance, and output equivalence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-aware character n-gram draft with a small causal LM verifier
- Success threshold: At least 1.2x end-to-end tokens/sec improvement over baseline decoding on CPU with unchanged verifier-correct outputs and draft overhead below 10% of total time.
- Stop condition: Stop if tokenizer conversion rejects most character drafts, if accepted tokens per verifier call stay below 1.1, or if end-to-end throughput fails to exceed baseline by 5% after implementation-level overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/character-n-gram-draft-model-for-cpu-speculative-decoding-da88ab9fa66a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
