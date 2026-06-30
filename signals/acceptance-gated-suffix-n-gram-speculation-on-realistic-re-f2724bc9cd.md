# Acceptance-gated suffix n-gram speculation on realistic repeated-span prompts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `acceptance-gated-suffix-n-gram-speculation-on-realistic-re-f2724bc9cd`
Run ID: `acceptance-gated-suffix-n-gram-speculation-on-realistic-re-f2724bc9cd-20260531T203851390851+0000`

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

- Parent run decision: N-Gram Suffix Draft for Speculative Decoding on Home GPUs: enoch://control-plane/projects/n-gram-suffix-draft-for-speculative-decoding-on-home-gpus-4d3278430b40/runs/n-gram-suffix-draft-for-speculative-decoding-on-home-gpus-4d3278430b40-20260531T123900901537+0000
- Parent run decision: KV-cache n-gram suffix speculative decoding on a 1B-3B home-GPU model: enoch://control-plane/projects/kv-cache-n-gram-suffix-speculative-decoding-on-a-1b-3b-hom-0e04e19360/runs/kv-cache-n-gram-suffix-speculative-decoding-on-a-1b-3b-hom-0e04e19360-20260531T162421190641+0000

## What looked useful

Acceptance gating improved draft precision and repeated-span specificity but reduced draft coverage enough that it underperformed ungated suffix lookup on ideal target-call speedup. This is useful no-paper evidence for treating the gate as a precision control rather than a standalone speedup win.

## Boundaries and scale limits

Bounded to GPT-2-small, synthetic-but-realistic operational repeated-span prompts, 48-token greedy continuations, and ideal target verification call accounting. It does not validate optimized batched KV-cache serving latency, larger models, instruction-tuned models, or private production traces.

## Claim scope

On 36 fixed-seed GPT-2-small repeated-span operational prompts, acceptance-gated suffix n-gram speculation preserved exact greedy output and reduced ideal target verification calls to 0.518 calls/token, a 1.97x ideal call reduction versus greedy. The effect was more specific to repeated prompts than controls, but the ungated suffix n-gram ablation had higher ideal speedup.

## Why it stopped

Tier 2 GPT-2-small evidence is mixed: gated speculation is exact and repeated-span-sensitive, but it fails to beat the ungated ablation on the primary ideal target-call speedup metric.

## Recommended next action

Stop this run as a no-paper useful signal; only continue if implementing a true batched KV-cache verifier to test whether higher acceptance precision converts into real latency or throughput wins.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched KV-cache suffix n-gram speculation latency test
- Success threshold: Acceptance-gated suffix n-gram must preserve 100% greedy-match equivalence and improve wall-clock tokens/sec by at least 20% versus ungated suffix n-gram on repeated-span prompts, without a statistically meaningful speedup on non-repeated controls.
- Stop condition: Stop if the batched implementation still trails ungated suffix lookup on repeated-span wall-clock throughput or if exact greedy-match preservation falls below 100%.

## Evidence references

- Artifact root: `<local-path>/projects/acceptance-gated-suffix-n-gram-speculation-on-realistic-re-f2724bc9cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
