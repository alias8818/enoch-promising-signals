# Suffix-Array Speculative Decoding from Training Corpus Residuals

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-from-training-corpus-residuals-b9c42d03a787`
Run ID: `suffix-array-speculative-decoding-from-training-corpus-residuals-b9c42d03a787-20260528T194641602435+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8cf1563055e9

## What looked useful

Exact suffix/prefix retrieval has a frequency-precision tradeoff: 8-byte contexts hit about 46-51% of held-out positions and estimate 33-44% verifier-call reduction, while 16-byte contexts drop to 1.5-6.1% hit rate and 2-12% estimated reduction, and 32-byte contexts are effectively absent.

## Boundaries and scale limits

No neural verifier, no BPE/model-token corpus, no measured inference latency, no suffix-array production implementation, and only two small natural-language corpora. Results should not be read as full speculative-decoding validation.

## Claim scope

Byte-level 90/10 held-out proxy on Tiny Shakespeare and Alice in Wonderland shows exact training-corpus context retrieval can reduce estimated verifier calls for very short contexts, but the effect collapses for longer exact contexts because hits become sparse.

## Why it stopped

Proxy useful-signal closure: the run tested the prerequisite retrieval/acceptance mechanism, not a full model-serving system, and the naive exact-context method is not paper-worthy as-is.

## Recommended next action

Run a bounded deepen test with GPT-2-tokenized text, approximate/backoff suffix retrieval, and a small real verifier against an n-gram/cache baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-Level Backoff Suffix Drafting with a Small Verifier
- Success threshold: At least 15% end-to-end decoding latency reduction versus one-token verifier decoding and at least 5% better latency than an n-gram/cache baseline on the same prompts without quality degradation.
- Stop condition: Stop if token-level context hits below 5% at useful context lengths or lookup overhead erases measured verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-from-training-corpus-residuals-b9c42d03a787`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
