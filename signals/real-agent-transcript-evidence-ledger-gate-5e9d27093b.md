# Real Agent Transcript Evidence-Ledger Gate

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-transcript-evidence-ledger-gate-5e9d27093b`
Run ID: `real-agent-transcript-evidence-ledger-gate-5e9d27093b-20260527T083729626611+0000`

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

- Parent run decision: Evidence-Ledger Constrained Agent Tool Use: enoch://control-plane/projects/evidence-ledger-constrained-agent-tool-use-d38b7b5e7c9d/runs/evidence-ledger-constrained-agent-tool-use-d38b7b5e7c9d-20260524T234243007240+0000
- Parent run decision: LLM Agent Evidence-Ledger Gate Test: enoch://control-plane/projects/llm-agent-evidence-ledger-gate-test-aebc52e098/runs/llm-agent-evidence-ledger-gate-test-aebc52e098-20260524T235228082550+0000

## What looked useful

Full fixed-seed runs over 128 claims per run achieved ledger accuracy/precision/recall/rejection/F1 of 1.0 versus lexical baseline accuracy 0.5464 and unsupported rejection 0.3961. Channel ablations reduced recall as expected while keeping unsupported rejection at 1.0.

## Boundaries and scale limits

Single real transcript; unsupported claims are deterministic perturbations of real facts rather than human-authored hallucinations; exact structured fact matching does not test semantic paraphrase support or live-agent integration.

## Claim scope

On one real Codex agent transcript, a structured evidence-ledger gate over file, metadata, command, and agent-message facts rejected deterministic unsupported perturbation claims far better than a raw lexical transcript-overlap baseline while preserving supported claims when the relevant ledger channel was present.

## Why it stopped

No-paper useful signal: Tier 2-style fixed seeds, real baseline, direct target metrics, and ablations were completed locally, but the evidence remains single-transcript and partly perturbation-generated.

## Recommended next action

Run the same ledger-gate evaluation on at least 50 independent real agent transcripts with audited final-report claims and paraphrases before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Transcript Evidence-Ledger Gate With Audited Claims
- Success threshold: Ledger gate unsupported-claim rejection is at least 30 percentage points above lexical overlap and supported-claim recall is at least 0.90 on audited claims across the corpus.
- Stop condition: Stop if audited unsupported-claim rejection improves by less than 15 percentage points over baseline or supported-claim recall drops below 0.80 after adding the complete ledger channels.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-transcript-evidence-ledger-gate-5e9d27093b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
