# Evidence-Ledger Agent: Falsifiable Claim Tracking for Tool-Use Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-falsifiable-claim-tracking-for-tool-use-tasks-8e3597d11559`
Run ID: `evidence-ledger-agent-falsifiable-claim-tracking-for-tool-use-tasks-8e3597d11559-20260611T073401884814+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2d662c61c743

## What looked useful

Evidence-ledger validation achieved 1.0 unsupported-claim recall and 1.0 precision on the structured synthetic benchmark; citation-only validation achieved 0.3345907381614986 mean unsupported-claim recall because it missed wrong values behind valid citations.

## Boundaries and scale limits

The run used 20,000 synthetic claims across five seeds and did not test live LLM generation, natural-language claim extraction, multi-hop support, adversarial paraphrases, or human-labeled real tool-use traces.

## Claim scope

In a deterministic synthetic tool-use benchmark with structured observations, structured atomic final claims, and explicit citations, an evidence ledger that checks cited entity, field, and value detects unsupported claims that citation-only validation misses.

## Why it stopped

Proxy synthetic evidence supports the core ledger-checking mechanism but is not a full validation of open-ended evidence-ledger agents.

## Recommended next action

Run a bounded real-LLM follow-up with natural-language tool-use transcripts, automatic claim extraction, and human or trusted-parser labels; stop this run as useful no-paper evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LLM Evidence Ledger on Labeled Tool-Use Transcripts
- Success threshold: At least 0.80 unsupported-claim recall with no more than 0.10 false-positive rate on supported claims, and at least a 2x recall improvement over citation-only validation on 200 or more labeled natural-language claims.
- Stop condition: Stop if claim extraction or evidence matching cannot exceed citation-only unsupported-claim recall by 10 percentage points, or if supported-claim false-positive rate exceeds 0.20 after basic prompt/parser tuning.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-falsifiable-claim-tracking-for-tool-use-tasks-8e3597d11559`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
