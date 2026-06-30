# Prompt Suffix-Array Speculative Decode

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-suffix-array-speculative-decode-e344b53e3096`
Run ID: `prompt-suffix-array-speculative-decode-e344b53e3096-20260608T012742596960+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7efcb0693f7e

## What looked useful

Suffix-array prompt lookup can be a viable model-free draft source for prompt-local copying, but it is brittle outside exact repetition. Longer drafts improve proxy call reduction on repetitive prompts while lowering accepted/proposed ratio.

## Boundaries and scale limits

Short synthetic prompts, GPT-2 only, greedy exact-token acceptance, no batched verifier implementation, no measured serving latency, no sampling acceptance, no long-context traces, and no comparison to production prompt-lookup or neural draft baselines.

## Claim scope

On four short GPT-2 greedy-generation prompts, a prompt-token suffix-array drafter reduces proxy target verification calls only when generation repeats prompt-local text; the best tested aggregate setting reached a 2.54x mean upper-bound call reduction, while the nonrepeating prose control showed no useful reduction.

## Why it stopped

No-paper closure: the result is a short synthetic proxy signal, not direct serving evidence or broad validation.

## Recommended next action

Run a bounded deepen follow-up with a real batched verifier and measured end-to-end latency on 50-100 long prompt-copy traces, comparing against no-draft and n-gram/prompt-lookup baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched verifier latency test for prompt suffix-array drafting
- Success threshold: At least 20% median end-to-end latency reduction on copy-heavy traces with less than 5% regression on non-copy controls.
- Stop condition: Stop if suffix-array query plus verification overhead erases proxy call savings or if acceptance falls below 10% on copy-heavy traces.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-suffix-array-speculative-decode-e344b53e3096`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
