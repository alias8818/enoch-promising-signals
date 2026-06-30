# N-gram speculative decoding speedup on CPU-only inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-speedup-on-cpu-only-inference-b3965b17cda6`
Run ID: `n-gram-speculative-decoding-speedup-on-cpu-only-inference-b3965b17cda6-20260612T231916260858+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ee1613732b9e

## What looked useful

Copy-rich cases accepted 24/24 draft tokens, reduced target forwards from 25 to 4, and achieved 1.64x and 2.34x median wall speedups. The low-repeat control proposed no drafts and slowed to 0.92x. A tiny-GPT2 control accepted no drafts and stayed near 1.0x, showing the mechanism is acceptance-dependent rather than universally positive.

## Boundaries and scale limits

Synthetic prompts, 24 generated tokens per case, one CPU thread, one small public model for main metrics, no sampling, no batching, no quantized serving runtime, no real workload trace, and no larger CPU LLM validation.

## Claim scope

Bounded CPU-only greedy decoding test with distilgpt2 on two synthetic copy-rich prompts and one low-repeat control: prompt-lookup 3-gram speculative decoding reduced target forwards and improved wall time only when drafts were fully accepted.

## Why it stopped

Small local evidence is useful but mixed and not paper-ready; it supports the mechanism only in repeat-rich accepted-draft cases and shows overhead/no benefit when drafts are unavailable.

## Recommended next action

Run a bounded deepen follow-up on a small real copy/edit/RAG prompt corpus with a stronger CPU-suitable model or quantized runtime, and require speedup to correlate with measured draft acceptance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-workload CPU n-gram speculative decoding acceptance study
- Success threshold: Median wall speedup >= 1.3x on copy-heavy prompts, p25 speedup >= 1.0x, exact output match for every prompt, and low-repeat median speedup >= 0.98x with speculation disabled or bounded by an acceptance heuristic.
- Stop condition: Stop as negative if acceptance is below 30% on copy-heavy prompts or if low-repeat controls remain below 0.95x after adding a simple repeat-rate/acceptance gate.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-speedup-on-cpu-only-inference-b3965b17cda6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
