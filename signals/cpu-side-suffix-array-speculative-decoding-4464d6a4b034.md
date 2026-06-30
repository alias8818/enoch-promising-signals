# CPU-Side Suffix Array Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-side-suffix-array-speculative-decoding-4464d6a4b034`
Run ID: `cpu-side-suffix-array-speculative-decoding-4464d6a4b034-20260529T005321056833+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f12390d6958e

## What looked useful

Exact-copy retrieval can be a strong draft source for repeated spans, but static prompt suffix-array drafting is near-neutral on ordinary real text and is computationally dominated by a simpler hash n-gram control in this setup.

## Boundaries and scale limits

No live LLM, no GPU overlap, no batching, no dynamic suffix-array updates, no LLM tokenizer, and no production latency path were tested. Main real-text runs used 45k prompt tokens and 8k continuation tokens per corpus.

## Claim scope

Bounded CPU-only proxy over regex-tokenized public text: static prompt-index exact-copy speculative drafts reduce target-call count on highly repetitive synthetic text, but provide only 1.0019x to 1.0221x speedup proxy on two real-text corpora, and suffix arrays do not improve proposal quality over a same-policy hash n-gram baseline.

## Why it stopped

Early bounded proxy falsification for the suffix-array-specific claim: real-text speedup was at most 1.0221x in sensitivity testing and hash n-gram matched quality with much lower CPU overhead; this is not a full production validation.

## Recommended next action

Stop this suffix-array-specific path unless a follow-up can test real LLM tokenizer/greedy traces and demonstrate at least 1.10x end-to-end speedup over a hash n-gram retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-token trace validation of retrieval speculative drafts
- Success threshold: At least 1.10x end-to-end latency or target-call improvement over no speculation on a non-synthetic workload, while also beating the hash n-gram retrieval baseline after CPU overhead.
- Stop condition: Stop if non-synthetic LLM traces remain below 1.05x speedup or suffix arrays fail to beat hash n-gram retrieval on latency-adjusted metrics.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-side-suffix-array-speculative-decoding-4464d6a4b034`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
