# Evidence-ledger agent reliability for 1B-parameter local models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-reliability-for-1b-parameter-local-models-15604fbb956c`
Run ID: `evidence-ledger-agent-reliability-for-1b-parameter-local-models-15604fbb956c-20260531T132833555712+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/eeb1ceb17c75

## What looked useful

Raw evidence-ledger prompting is not sufficient as a standalone reliability intervention for 1B-class local models: Qwen grounded success rose only from 0% to 6.7% while exact answers fell from 85.0% to 61.7%; Llama baseline failed JSON parsing, while ledger reached 40.0% exact answers and 13.3% grounded success.

## Boundaries and scale limits

Tested only 60 Qwen2.5-1.5B-Instruct cases and 30 Llama-3.2-1B-Instruct cases on synthetic short-context evidence packets. No real agent traces, long-context retrieval, constrained decoding, validator retries, human grading, or broad model sweep were tested.

## Claim scope

On synthetic multi-hop line-cited QA for two cached 1B-class local instruction models, raw evidence-ledger prompting improved parse/citation structure in some cases but did not deliver reliable grounded answering and reduced Qwen exact-answer accuracy.

## Why it stopped

Moderate synthetic evidence gives a useful mixed/negative result for raw evidence-ledger prompting, but it is not publication-grade and does not validate reliable 1B-class local agents.

## Recommended next action

Stop this prompt-only run; next bounded test should add deterministic JSON constraints plus citation-validator retry and require improved grounded success without answer-accuracy regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validator-retry evidence ledgers for 1B-class local QA
- Success threshold: Ledger-plus-validator reaches at least 60% grounded success on both models and does not reduce exact-answer accuracy by more than 5 percentage points versus the stronger direct baseline.
- Stop condition: Stop if grounded success remains below 30% on either model or if retry latency exceeds 3x raw ledger latency without meeting the accuracy threshold.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-for-1b-parameter-local-models-15604fbb956c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
