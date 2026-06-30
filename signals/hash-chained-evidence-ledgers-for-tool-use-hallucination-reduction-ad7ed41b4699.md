# Hash-Chained Evidence Ledgers for Tool-Use Hallucination Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-evidence-ledgers-for-tool-use-hallucination-reduction-ad7ed41b4699`
Run ID: `hash-chained-evidence-ledgers-for-tool-use-hallucination-reduction-ad7ed41b4699-20260527T234350997552+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ca1df01e51ec

## What looked useful

Hash references alone were not enough: they accepted 10000 of 14000 unsupported claims. Exact hash-chain plus field/value verification accepted 0 of 14000 unsupported claims with 8000 of 8000 supported claims accepted in 2000 trials.

## Boundaries and scale limits

Synthetic claims and structured observations only; no real LLM generations, realistic unstructured tool outputs, human grading, or production latency study. The result supports acceptance-time gating, not spontaneous generation-time hallucination reduction.

## Claim scope

In a deterministic synthetic tool-use verifier benchmark with structured observations, requiring final-answer claims to cite a valid hash-chain ledger entry and match the cited field/value rejected all injected unsupported claims while preserving all supported claims.

## Why it stopped

Closed as no-paper useful signal because this run directly tested synthetic verifier acceptance, not full real-agent hallucination reduction.

## Recommended next action

Run a bounded real-LLM follow-up where tool-using agents answer factual tasks under source-label-only versus enforced hash-ledger gating, then grade unsupported final-answer claims and abstention/completeness tradeoffs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LLM Hash-Ledger Gate for Tool-Use Final Answers
- Success threshold: At least 50% relative reduction in unsupported final-answer claims versus source-label baseline with supported-answer completeness dropping by no more than 10 percentage points on the same task set.
- Stop condition: Stop if the ledger gate reduces completeness by more than 20 percentage points, fails to reduce unsupported claims by at least 25%, or verifier false rejects dominate the error budget.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledgers-for-tool-use-hallucination-reduction-ad7ed41b4699`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
