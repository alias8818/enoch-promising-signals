# Direct Local-LLM Evidence-Ledger QA Evaluation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `direct-local-llm-evidence-ledger-qa-evaluation-59bf5bc0f7`
Run ID: `direct-local-llm-evidence-ledger-qa-evaluation-59bf5bc0f7-20260609T003515269903+0000`

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

- Parent run decision: Evidence-Ledger for Small Local Agents: enoch://control-plane/projects/evidence-ledger-for-small-local-agents-3a409640f5d2/runs/evidence-ledger-for-small-local-agents-3a409640f5d2-20260608T221915772736+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8f715af5ee7e

## What looked useful

Evidence-ledger prompting alone was insufficient for small local-LLM QA: ledger answer correctness was 0/6, citation coverage and digest verification were 1/6, and decoy contamination was 3/6. The main failure mode is misgrounded citation, including citing source evidence while answering from a conflicting decoy.

## Boundaries and scale limits

Small Tier 1 local test only: six synthetic-but-direct QA items, one 0.5B local instruct model for the full run, one 1.5B first-item smoke check, deterministic decoding, no prompt search, no constrained decoding, no retrieval corpus, no human audit-time measurement, and no large/frontier model validation.

## Claim scope

On six controlled document-grounded QA tasks with adversarial decoy hints, a prompt-only evidence ledger did not improve cached Qwen2.5-0.5B-Instruct QA correctness or citation reliability over a plain context prompt; a one-item Qwen2.5-1.5B-Instruct smoke check reproduced misgrounded citation on the first item.

## Why it stopped

Controlled direct Tier 1 test failed the stated thresholds; this is not a full-scale validation, but it directly falsifies the prompt-only small-local-LLM ledger QA success criterion in the tested setting.

## Recommended next action

Stop this prompt-only QA line as no-paper evidence; the bounded next test should add an explicit verifier or constrained citation/JSON gate and measure whether it catches misgrounded citations on the same QA items.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-Gated Evidence-Ledger QA on Misgrounded Citations
- Success threshold: Verifier rejects at least 0.8 of misgrounded ledger answers, false-rejects no more than 0.2 of correct source-grounded answers, and final accepted answers have decoy contamination no greater than 0.1 on at least 12 controlled QA items.
- Stop condition: Stop if the verifier cannot distinguish cited-source support from decoy-derived answers on the original six failures, or if final accepted answer coverage falls below 0.5.

## Evidence references

- Artifact root: `<local-path>/projects/direct-local-llm-evidence-ledger-qa-evaluation-59bf5bc0f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
