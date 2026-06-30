# N-Gram Speculative Decoding with Local Draft Buffer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-with-local-draft-buffer-2f11d33e8759`
Run ID: `n-gram-speculative-decoding-with-local-draft-buffer-2f11d33e8759-20260522T123511826930+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/60fbf69a39be

## What looked useful

The mechanism works when local repetition is high: synthetic repeated text reached 11.996 tokens per target call with gamma=12. Natural word-level corpora reached only 1.130-1.221 tokens per target call and had very low exact draft-token acceptance rates of 1.3-2.1%, indicating that broad LLM-serving gains are unlikely without a stronger draft policy or a highly repetitive domain.

## Boundaries and scale limits

No GPU LLM was served, no KV-cache or tokenizer integration was measured, and no wall-clock target-model speedup was benchmarked. Corpora were three Gutenberg books plus a synthetic repeated stream, with up to 40k evaluated tokens per natural corpus.

## Claim scope

CPU proxy over realized token streams: a rolling local n-gram copy buffer reduces target verification calls on repetitive streams and gives only modest 13-22% target-call reduction on natural word/punctuation Gutenberg text; character streams show larger proxy gains but are not directly comparable to subword LLM serving.

## Why it stopped

Proxy evidence supports the mechanism but not a publication-grade LLM serving claim; natural word-level acceptance is too low and full validation requires direct model-serving benchmarks.

## Recommended next action

Stop this run as no-paper useful evidence; the concrete next bounded test is an end-to-end small causal-LM benchmark that measures tokens/s and target forward calls against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-LM local n-gram draft buffer benchmark
- Success threshold: At least 1.25x wall-clock tokens/s over greedy decoding on a non-synthetic domain with unchanged output semantics and measured draft overhead below the saved target-model time.
- Stop condition: Stop if generic and code-like domains both remain below 1.10x wall-clock speedup or if CPU draft overhead exceeds target-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-with-local-draft-buffer-2f11d33e8759`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
