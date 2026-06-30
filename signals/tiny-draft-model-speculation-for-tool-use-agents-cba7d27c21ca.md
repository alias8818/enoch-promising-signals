# Tiny Draft Model Speculation for Tool-Use Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-draft-model-speculation-for-tool-use-agents-cba7d27c21ca`
Run ID: `tiny-draft-model-speculation-for-tool-use-agents-cba7d27c21ca-20260524T181457149025+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d085e78b642

## What looked useful

Tool-call formatting is a material variable for speculative decoding. Pretty structured tool calls reached 0.9215 weighted acceptance versus 0.8887 for prose, but compact JSON was 0.8884 and statistically indistinguishable from prose; estimated useful speculation windows were short, about k=2 to k=4.

## Boundaries and scale limits

Synthetic continuations only; non-instruction-tuned GPT-2-family models; teacher-forced acceptance metric rather than an implemented speculative decoder; no real tool-use traces, task success, or production latency validation.

## Claim scope

Bounded proxy result: on synthetic tool-call-shaped continuations with GPT-2 as verifier and DistilGPT-2 as draft, pretty-printed tool JSON improves token-level speculative acceptance versus prose, while compact JSON does not.

## Why it stopped

Closed as no-paper useful signal because this proxy supports a mechanism and design knob but does not validate end-to-end tool-agent latency or correctness.

## Recommended next action

Run a bounded deepen follow-up using a real speculative decoder on real or benchmarked instruction-model tool-call traces, with k=2 and k=4 windows and pretty-vs-compact formatting as an explicit ablation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Speculative Decoding on Instruction Tool-Call Traces
- Success threshold: At least 1.15x median end-to-end decoding speedup at unchanged tool-call validity and task success, with a confidence interval excluding no speedup for k=2 or k=4.
- Stop condition: Stop if compact and pretty tool-call formats both fail to exceed 1.05x end-to-end speedup or if tool-call validity drops by more than 0.5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-draft-model-speculation-for-tool-use-agents-cba7d27c21ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
