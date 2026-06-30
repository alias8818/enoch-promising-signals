# Suffix-Tree Speculative Decoding vs N-gram on Local LLM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-vs-n-gram-on-local-llm-18878cdf8a5a`
Run ID: `suffix-tree-speculative-decoding-vs-n-gram-on-local-llm-18878cdf8a5a-20260630T042040571388+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/258725c218cc

## What looked useful

Suffix-copy has lower Python draft overhead and higher acceptance than n-gram on GPT-2-small, but target-call reduction is only slightly better there and model-dependent; n-gram is better on distilgpt2. The harness is useful for a bounded next-stage verification test, but the current result should not be treated as paper-positive.

## Boundaries and scale limits

Only 8 hand-written prompts per medium run, 2,048 generated tokens per model/K condition, deterministic greedy decoding, simulated verification from saved token streams, no end-to-end KV-cache speculative serving path, no larger instruction-tuned model, no diverse corpus benchmark.

## Claim scope

On saved greedy target streams from local distilgpt2 and GPT-2-small, a suffix-copy drafter is competitive with but not consistently better than a dynamic n-gram backoff drafter. It modestly beats n-gram on GPT-2-small at K=4/8/16, but loses clearly on distilgpt2 at the same K values.

## Why it stopped

Mixed bounded evidence from local greedy-stream replay: suffix-copy is not consistently superior to n-gram, and the serving-critical end-to-end verification path was only proxied.

## Recommended next action

Stop this run as no-paper useful evidence; next, implement actual batched speculative verification with target logits/KV-cache reuse and evaluate suffix-copy versus n-gram on a broader prompt corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end suffix-copy speculative decoding with batched target verification
- Success threshold: Suffix-copy achieves at least 5% relative target-call reduction or latency improvement over n-gram on both tested models, with equal greedy outputs and lower or comparable draft overhead.
- Stop condition: Stop if suffix-copy fails to beat n-gram on GPT-2-small by at least 2% relative target-call reduction or if batched verification overhead erases the replay-level advantage.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-vs-n-gram-on-local-llm-18878cdf8a5a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
