# Small-LM End-to-End Retrieval Drafting Check

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `small-lm-end-to-end-retrieval-drafting-check-55c95f5f89`
Run ID: `small-lm-end-to-end-retrieval-drafting-check-55c95f5f89-20260522T094134444823+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: CPU Suffix-Array Speculative Decoding: enoch://control-plane/projects/cpu-suffix-array-speculative-decoding-b639b85b308d/runs/cpu-suffix-array-speculative-decoding-b639b85b308d-20260522T084540825817+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/97c0e59c9136

## What looked useful

Retrieval was effective but drafting was the bottleneck: distilgpt2 reached 20.8% retrieved-context exact accuracy and gpt2 reached 14.6%, both far below the 70% success threshold; oracle-context scores matched retrieved-context scores, showing evidence use/copying failure rather than retrieval failure.

## Boundaries and scale limits

The run tested synthetic short-answer facts and two base causal LMs, distilgpt2 and gpt2, on CPU. It did not test instruction-tuned small LMs, real corpora, larger models, fine-tuning, or production retrieval settings.

## Claim scope

On a 48-example synthetic closed-book factual QA benchmark, cached GPT-2-family base small LMs did not reliably draft exact answers from retrieved evidence, despite BM25 retrieval placing the answer in context for 97.9% of examples.

## Why it stopped

Controlled small direct test failed the stated threshold for GPT-2-class base small LMs: retrieval succeeded, but answer drafting from retrieved or oracle evidence remained under 21%.

## Recommended next action

Stop this run as a no-paper negative/useful-signal result; the only justified deepen test is a bounded instruction-tuned small-LM replication using the same direct threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Instruction-Tuned Small-LM Retrieval Drafting Replication
- Success threshold: Retrieved-context exact accuracy >= 70%, retrieved-context minus no-context exact accuracy >= 50 percentage points, and oracle-context exact accuracy >= 85% on at least 48 deterministic examples.
- Stop condition: Close negative if retrieval places the answer in context for >=95% of examples but retrieved-context or oracle-context exact accuracy remains below threshold.

## Evidence references

- Artifact root: `<local-path>/projects/small-lm-end-to-end-retrieval-drafting-check-55c95f5f89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
