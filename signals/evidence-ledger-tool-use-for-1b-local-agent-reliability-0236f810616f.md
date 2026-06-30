# Evidence-ledger tool-use for 1B local agent reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-tool-use-for-1b-local-agent-reliability-0236f810616f`
Run ID: `evidence-ledger-tool-use-for-1b-local-agent-reliability-0236f810616f-20260523T034904869036+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8fdc9667bbfb

## What looked useful

Prompt-only ledger improved correctness from 43.3% to 63.3%, exact citation from 23.3% to 70.0%, and reduced unsupported answers from 76.7% to 36.7%, but failed all missing-evidence abstention cases. A deterministic gate that forced abstention when cited evidence did not contain the answer raised ledger-condition correctness to 83.3% and missing-evidence correctness to 100.0%, versus 43.3% total correctness for the same gate on baseline outputs.

## Boundaries and scale limits

Synthetic tasks only; one 1.5B local model; no real tool APIs, no long-horizon agent loop, no noisy retrieval corpus, no multi-model robustness, and support checking used simple cited-text containment rather than semantic entailment.

## Claim scope

On a 30-task synthetic evidence-grounding benchmark with Qwen/Qwen2.5-1.5B-Instruct, an explicit evidence-ledger prompt improved correctness and citation discipline over a baseline that mixed stale memory with tool observations; adding a deterministic support gate to the ledger condition produced the strongest reliability signal.

## Why it stopped

The result is a bounded synthetic proxy, not full validation of local-agent reliability; prompt-only ledger was mixed and the strongest effect requires a deterministic gate.

## Recommended next action

Stop this run as no-paper useful signal; next run should test a field-aware ledger gate on a larger realistic tool/retrieval benchmark across at least three 1B-class local models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Field-aware evidence-ledger gate on realistic local-agent tool traces
- Success threshold: Ledger plus field-aware gate improves total correctness by >=20 percentage points over the best prompt-only baseline, missing-evidence correctness is >=90%, and lookup correctness remains >=75% on at least 100 realistic tasks.
- Stop condition: Stop if field-aware gating cannot exceed prompt-only ledger by 10 percentage points, if lookup correctness falls below 65%, or if realistic traces show no reproducible unsupported-answer reduction.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-tool-use-for-1b-local-agent-reliability-0236f810616f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
