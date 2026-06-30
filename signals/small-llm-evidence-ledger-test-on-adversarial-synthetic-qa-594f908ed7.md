# Small-LLM evidence ledger test on adversarial synthetic QA

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `small-llm-evidence-ledger-test-on-adversarial-synthetic-qa-594f908ed7`
Run ID: `small-llm-evidence-ledger-test-on-adversarial-synthetic-qa-594f908ed7-20260529T112431208042+0000`

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

- Parent run decision: Evidence ledger reduces tiny agent hallucination: enoch://control-plane/projects/evidence-ledger-reduces-tiny-agent-hallucination-31a93f6888b7/runs/evidence-ledger-reduces-tiny-agent-hallucination-31a93f6888b7-20260529T080133385441+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/eddb43fb175d

## What looked useful

The ledger condition scored 18.75% exact-answer accuracy versus 31.25% for baseline, with -12.5 percentage point delta and only 6.25% valid support citations, missing the +8 point and 70% support-validity Tier 1 threshold.

## Boundaries and scale limits

Synthetic deterministic dataset; one primary 0.5B instruction model; one ledger prompt formulation; CPU-only bounded run; not a natural-QA or broad model-family validation.

## Claim scope

In a 32-example controlled adversarial synthetic QA test with Qwen/Qwen2.5-0.5B-Instruct, a free-form evidence-ledger prompt did not improve exact-answer accuracy over an answer-only baseline and failed to produce valid support citations.

## Why it stopped

Controlled small direct test missed the stated threshold: ledger prompting reduced answer accuracy and rarely cited the correct supporting sentence.

## Recommended next action

Stop this run as an early direct falsification of the tested ledger-prompt mechanism; only pursue a bounded deepen follow-up if testing constrained ledger formatting or decoding, not a scale-only rerun.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained evidence-ledger decoding for small-model adversarial QA
- Success threshold: Constrained ledger condition improves exact-answer accuracy by at least 8 percentage points over baseline and achieves at least 70% valid support citations.
- Stop condition: Stop if constrained ledger support validity remains below 50% or answer accuracy fails to exceed baseline on the first 100-example controlled run.

## Evidence references

- Artifact root: `<local-path>/projects/small-llm-evidence-ledger-test-on-adversarial-synthetic-qa-594f908ed7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
