# Evidence-ledger self-correction for 1B-parameter tool agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-self-correction-for-1b-parameter-tool-agents-0acee59954bb`
Run ID: `evidence-ledger-self-correction-for-1b-parameter-tool-agents-0acee59954bb-20260527T215201035983+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/df2fb53c6ff9

## What looked useful

Evidence ledger prompting improved confirmation accuracy from 66/100 to 74/100, with paired transitions of 9 ledger-only fixes versus 1 baseline-only fix and exact McNemar p=0.0215. The gain came from multi-tool aggregation; easy lookup/calculator cases were saturated and profile-field correction remained poor.

## Boundaries and scale limits

Synthetic prompt-only benchmark; 100-case confirmation plus 40-case pilot; no real external tool execution loop, no persistent ledger, no strict JSON/tool-call compliance validation, no additional model families, and no production 1B-agent traces.

## Claim scope

On a synthetic finalization benchmark with Qwen/Qwen2.5-1.5B-Instruct, an evidence-ledger prompt improved content-level correction from deterministic tool observations after a wrong prior, mainly on multi-tool aggregation cases.

## Why it stopped

No-paper useful signal: the result supports a narrow synthetic mechanism but is not direct or broad enough for the original 1B-parameter tool-agent claim.

## Recommended next action

Run a bounded follow-up on realistic multi-turn tool-agent traces with strict schema parsing and compare evidence ledger prompting against simpler re-read/cite-tool-output prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledgers on realistic multi-turn 1B tool-agent traces
- Success threshold: Evidence ledger beats both plain baseline and simpler re-read/cite-tool-output controls by at least 5 absolute accuracy points on content correction, with exact paired-test p<0.05 and no more than 2 absolute points loss in strict output validity on at least two 1B-class models.
- Stop condition: Stop as negative if gains disappear against the simpler prompt control, if output validity materially degrades, or if improvements remain confined to synthetic aggregation-style tasks.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-self-correction-for-1b-parameter-tool-agents-0acee59954bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
