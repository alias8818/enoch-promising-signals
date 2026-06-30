# Real-LLM evidence-ledger evaluation with distractor evidence

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-llm-evidence-ledger-evaluation-with-distractor-eviden-005fcb6383`
Run ID: `real-llm-evidence-ledger-evaluation-with-distractor-eviden-005fcb6383-20260621T062730339170+0000`

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

- Parent run decision: Evidence-ledger agent: verifiable claims vs ungrounded baseline: enoch://control-plane/projects/evidence-ledger-agent-verifiable-claims-vs-ungrounded-baseline-65d4d8305ff1/runs/evidence-ledger-agent-verifiable-claims-vs-ungrounded-baseline-65d4d8305ff1-20260621T055004787849+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/72aaddea9ab3

## What looked useful

The clarified ledger prompt reduced answer accuracy from 79.2% to 45.8%, identified the true support in only 33.3% of cases, and broke 10 baseline-correct answers while fixing only 2 baseline-wrong answers.

## Boundaries and scale limits

Single 0.5B instruction model; small paired local test; no larger models, real retrieval corpus, tool-enforced schema, or multi-prompt robustness sweep.

## Claim scope

On a 24-case fictional distractor-evidence QA task with Qwen/Qwen2.5-0.5B-Instruct and deterministic decoding, an explicit evidence-ledger prompt failed to improve answer accuracy and produced unreliable support labels.

## Why it stopped

Tier 1 direct small test falsified the stated success threshold for the tested real LLM; this is useful bounded negative evidence, not full validation.

## Recommended next action

Run the same harness on a stronger instruction model with tool-enforced JSON or constrained decoding before considering any broader evidence-ledger claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger distractor QA with stronger model and constrained schema
- Success threshold: Ledger condition improves answer accuracy by at least 15 percentage points over baseline, reaches at least 80% true support identification, and averages less than 0.25 false supporting distractors per case.
- Stop condition: Stop if the stronger/constrained run still fails to beat baseline accuracy or support identification remains below 60% after 100 held-out paired cases.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-evidence-ledger-evaluation-with-distractor-eviden-005fcb6383`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
