# Live-LLM evidence-ledger reliability harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-llm-evidence-ledger-reliability-harness-7de012d4d0`
Run ID: `live-llm-evidence-ledger-reliability-harness-7de012d4d0-20260630T090822181912+0000`

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

- Parent run decision: Evidence-Ledger Agent Reliability Harness on GB10: enoch://control-plane/projects/evidence-ledger-agent-reliability-harness-on-gb10-2663c06beb40/runs/evidence-ledger-agent-reliability-harness-on-gb10-2663c06beb40-20260630T084812042004+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/745fc4966091

## What looked useful

Across 300 synthetic cases, the ledger validator detected 250/250 injected bad ledgers and accepted 50/50 clean ledgers; a text-only baseline detected 50/250 bad cases.

## Boundaries and scale limits

Synthetic corpus only; claim text equals evidence quote text; no live LLM provider, human labels, retrieval noise, paraphrase support, partial-support labels, or adversarial real-world citation cases were tested.

## Claim scope

In a deterministic synthetic QA/citation setting, an append-only evidence ledger with source hashes, exact quote spans, claim references, and hash-chained events mechanically detected unsupported claims, misquotes, wrong-document citations, stale source revisions, and post-hoc payload tampering while accepting clean ledgers.

## Why it stopped

Closed as no-paper useful signal because evidence is deterministic and synthetic, not direct live-LLM validation.

## Recommended next action

Run the same ledger contract against a small live/local LLM citation dataset with human-labeled support errors before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live/local LLM citation-ledger validation on labeled QA cases
- Success threshold: At least 80% detection of labeled support/citation failures, under 10% false rejection on labeled clean answers, and no undetected ledger tampering in a minimum 100-case evaluation.
- Stop condition: Stop if live/local model outputs cannot be made to emit usable ledger events, or if detection of labeled citation/support failures is below 60% after schema fixes.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-evidence-ledger-reliability-harness-7de012d4d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
