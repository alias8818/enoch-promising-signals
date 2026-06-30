# Suffix-Array Speculative Decoding Without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-without-draft-model-03f378610d0b`
Run ID: `suffix-array-speculative-decoding-without-draft-model-03f378610d0b-20260523T044044324765+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e56aeca11e8c

## What looked useful

Best upper-bound target pass reduction was 3.599x on repeated template/code word tokens, 1.272x on character-level Shakespeare, 1.021x on word-level Shakespeare, and 1.000x on random-vocabulary control. This supports a specialized repetition-cache proposer but not a general replacement for learned draft models.

## Boundaries and scale limits

No real transformer decoder was instrumented; target pass reduction is an upper bound from corpus replay, with <=30000 tokens per corpus and <=12000 evaluated tokens per corpus except the shorter template corpus.

## Claim scope

Teacher-forced exact-continuation proxy on bounded corpora shows suffix-index draft-free speculation can reduce verifier passes on repeated template/code-like streams, but provides negligible benefit on word-level natural text.

## Why it stopped

Proxy evidence is mixed: it supports the mechanism in high-repetition streams but early-falsifies the broad draft-model-free claim for ordinary word-level natural text; this is not full validation.

## Recommended next action

Run a bounded direct decoder follow-up on a small real autoregressive model and code/boilerplate prompt suite, comparing no speculation, learned draft speculation, and suffix-index-only speculation with wall-clock latency and quality checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Decoder Test for Suffix-Index Speculation on Repeated Code Prompts
- Success threshold: Median wall-clock generated-token throughput improves by at least 1.5x over no speculation on repeated code/boilerplate prompts, with no deterministic-output mismatch and with suffix-index overhead below 15% of total decode time.
- Stop condition: Stop if median speedup is below 1.2x, accepted tokens per block are below 0.5, or retrieval overhead erases verifier-pass savings.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-without-draft-model-03f378610d0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
