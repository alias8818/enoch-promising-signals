# Evidence ledger for small local agent reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-small-local-agent-reliability-932687d4c148`
Run ID: `evidence-ledger-for-small-local-agent-reliability-932687d4c148-20260602T112809998416+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/257b1066766e

## What looked useful

Ledger validation achieved 1.0 bad-claim recall and 0.0 false rejection on integrity-only synthetic faults, but recall dropped to 0.799534 when fabricated-but-ledgered evidence was added as one of five fault modes.

## Boundaries and scale limits

100,000 synthetic tasks per main condition, 10 seeds per condition, CPU-only deterministic traces; no real LLM agents, real tool transcripts, human task labels, long-horizon autonomy, or external provenance capture were tested.

## Claim scope

A minimal evidence ledger detects synthetic post-observation claim integrity faults in small-agent traces, but does not detect fabricated evidence when the untrusted agent can append internally consistent records.

## Why it stopped

No-paper useful signal: synthetic evidence supports the integrity mechanism but falsifies the broader claim that an evidence ledger alone is sufficient for small local agent reliability.

## Recommended next action

Run a bounded real-trace follow-up with tool-signed or independently captured observations to test whether provenance controls close the fabricated-evidence gap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tool-signed evidence boundaries for small local agent ledgers
- Success threshold: At least 0.95 bad-claim recall, at most 0.02 good-claim false reject rate, and less than 10% runtime overhead on at least 200 real agent tasks.
- Stop condition: Stop if tool-signed or independently captured evidence still allows more than 0.10 bad-claim false accepts or causes more than 0.05 good-claim false rejects.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-local-agent-reliability-932687d4c148`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
