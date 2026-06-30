# Suffix-Tree Drafter for Local Speculative Decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-drafter-for-local-speculative-decoding-on-gb10-27e6d992dd34`
Run ID: `suffix-tree-drafter-for-local-speculative-decoding-on-gb10-27e6d992dd34-20260619T111806201968+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/06fb855ec8bb

## What looked useful

Suffix copying reached 8.8158x target-call speedup on repeated code-like templates versus 8.1213x for an online 4-gram control, but was slightly worse than the 4-gram control on Tiny Shakespeare and indistinguishable from baseline on random tokens.

## Boundaries and scale limits

CPU-only trace simulation with regex tokenization; no live LLM target, no GPU serving loop, no wall-clock model throughput, and no production tokenizer. Corpora were bounded to 30000 evaluated tokens per condition.

## Claim scope

Trace-level proxy evidence shows an online suffix-index drafter can reduce target-call count strongly on exact repeated/template-like token traces, but not on natural Tiny Shakespeare text or random high-entropy tokens.

## Why it stopped

Closed as a no-paper useful-signal proxy result: the mechanism is workload-sensitive and lacks direct model-serving evidence.

## Recommended next action

Run a direct local small-LLM speculative decoding integration that measures wall-clock tokens/s, target calls, exact acceptance, GPU utilization, and drafter overhead on repetitive code/log traces plus natural-text controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-LLM serving test for suffix-index speculative drafter
- Success threshold: At least 20% end-to-end tokens/s improvement over no-speculation and at least 10% over n-gram drafting on repetitive code/log workloads, with no material regression on natural-text controls beyond expected no-benefit behavior.
- Stop condition: Stop if suffix drafter overhead erases target-call savings or if repetitive workloads fail to exceed n-gram drafting by 10% end-to-end throughput.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-drafter-for-local-speculative-decoding-on-gb10-27e6d992dd34`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
