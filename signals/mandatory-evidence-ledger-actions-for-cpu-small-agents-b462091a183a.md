# Mandatory evidence-ledger actions for CPU small agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `mandatory-evidence-ledger-actions-for-cpu-small-agents-b462091a183a`
Run ID: `mandatory-evidence-ledger-actions-for-cpu-small-agents-b462091a183a-20260619T180512138063+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e4e06b2a7886

## What looked useful

The verifier classified 6/6 synthetic ledgers correctly with 0 false accepts and 0 false rejects, catching missing required actions, dangling references, unsupported citations, hash mismatches, and absent support tokens.

## Boundaries and scale limits

Tested only on 6 deterministic synthetic ledgers with 1 positive control and 5 negative controls; no real agent transcripts, adversarial natural-language claims, or human-labeled semantic support corpus were evaluated.

## Claim scope

A dependency-free verifier can mechanically enforce mandatory evidence-ledger actions for structured CPU-small-agent handoff ledgers in a bounded synthetic corpus.

## Why it stopped

Synthetic/local mechanism evidence supports the scoped verifier contract but is not direct deployment evidence or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded work should evaluate the verifier on real CPU-agent transcripts with human-labeled claim support.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate mandatory evidence-ledger verifier on real CPU-agent transcripts
- Success threshold: At least 50 real task handoffs with verifier false accept rate below 5% on human-labeled unsupported claims and false reject rate below 10% on supported claims.
- Stop condition: Stop if real transcripts cannot be converted into the structured ledger schema or if false accepts exceed 20% after obvious schema-mapping fixes.

## Evidence references

- Artifact root: `<local-path>/projects/mandatory-evidence-ledger-actions-for-cpu-small-agents-b462091a183a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
