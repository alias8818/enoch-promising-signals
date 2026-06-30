# Speculative Draft Cascade on CPU Only

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-draft-cascade-on-cpu-only-0483ec476ef4`
Run ID: `speculative-draft-cascade-on-cpu-only-0483ec476ef4-20260524T193748891159+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/776b47d08011

## What looked useful

Cascade preserved the target distribution within target-vs-target sampling noise and reduced target positions versus a strong single draft at gamma=8, but it did not beat the strongest single-draft baseline on the optimistic batched CPU cost proxy and was worse than target-only under sequential per-position CPU cost. Fewer target calls/positions alone is insufficient evidence for CPU speedup.

## Boundaries and scale limits

No real transformer models, learned draft models, tokenizer workloads, KV-cache behavior, or measured CPU batched-verification kernels were tested. Medium run was 20,000 tokens x 12 trials plus a gamma sweep over 2, 4, 8, 16.

## Claim scope

Dependency-free synthetic Markov LM simulation of target-only, single-draft, and two-stage speculative draft cascade decoding on a CPU worker. The claim is limited to algorithmic cost counters and explicit sequential/batched proxy cost models, not real transformer wall-clock speed.

## Why it stopped

Synthetic/proxy evidence is useful but not publication-grade, and the cascade failed to outperform the best single-draft baseline in the tested CPU cost models; this is not a full real-model validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next concrete test is a bounded real CPU transformer latency benchmark that measures target batch-cost curves and compares target-only, single-draft, and cascade decoding at equal output lengths.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Transformer Batch-Cost Test for Speculative Draft Cascades
- Success threshold: Cascade achieves at least 10% lower median latency/token than the best single-draft baseline while preserving exact speculative decoding semantics across at least three output lengths and two prompts/classes of prompts.
- Stop condition: Stop if measured target verification cost is approximately linear in proposed positions or if cascade latency is not better than the best single-draft baseline in two block-size settings.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-draft-cascade-on-cpu-only-0483ec476ef4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
