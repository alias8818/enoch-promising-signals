# Evidence ledger around a real tiny local LLM agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-around-a-real-tiny-local-llm-agent-e157d0a6d1`
Run ID: `evidence-ledger-around-a-real-tiny-local-llm-agent-e157d0a6d1-20260528T235053460360+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence Ledger for Tiny CPU Agent: enoch://control-plane/projects/evidence-ledger-for-tiny-cpu-agent-07c941c695bb/runs/evidence-ledger-for-tiny-cpu-agent-07c941c695bb-20260528T172431118617+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8fda443b78db

## What looked useful

The evidence ledger did not improve answer correctness, but it converted unsupported generated text from silently accepted output into a detectable verifier failure while preserving tamper-evident evidence records.

## Boundaries and scale limits

The language model was a tiny local n-gram model rather than a pretrained transformer; tasks were structured local file lookups; unsupported text was induced by a controlled injection rate; no open-ended multi-step planning, adversarial retrieval, or larger document corpus was tested.

## Claim scope

In a 12-task controlled local file-QA setting, an append-only hash-chained evidence ledger around a tiny local token language-model agent produced verifier verdicts for all answers, supported correct claims, rejected one unsupported generated claim, and detected deliberate ledger tampering.

## Why it stopped

Tier 1 direct mechanism threshold passed, but evidence is too controlled and too small for paper readiness.

## Recommended next action

Run a bounded deepen test with a real pretrained tiny transformer or GGUF model on messy multi-step local document tasks, keeping the same ledger verifier and adding adversarial irrelevant-citation cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger verification with a pretrained tiny local transformer agent
- Success threshold: Ledger condition has verifier verdict coverage >= 0.90, unsupported accepted claim rate == 0, tamper edits detected, and no-ledger supported claim rate <= 0.10 on at least 30 tasks.
- Stop condition: Stop if the pretrained tiny local model cannot complete at least 30 tasks locally within the deployment budget, or if ledger unsupported accepted claim rate exceeds 0 on any verified unsupported claim class after parser fixes.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-around-a-real-tiny-local-llm-agent-e157d0a6d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
