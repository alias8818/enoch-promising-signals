# Red-Team Ledger Replay for Local Agent Safety

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `red-team-ledger-replay-for-local-agent-safety-dec735b5b53d`
Run ID: `red-team-ledger-replay-for-local-agent-safety-dec735b5b53d-20260531T170500929985+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6fcd819485b5

## What looked useful

Ledger replay expressed temporal invariants that final-state-only inspection could not observe, catching 200000/200000 synthetic violations with 0/50000 benign false positives in this constructed proxy.

## Boundaries and scale limits

250000 deterministic synthetic traces and 1000000 events on one CPU process; no real local-agent traces, no real LLM/tool execution, no adaptive adversary, and no production false-positive measurement.

## Claim scope

Synthetic local-agent ledgers with history-dependent sensitive file reads, delayed exfiltration, approval-ordering violations, and prompt-injection-followed-by-action violations; comparison is against a final-state-only guard.

## Why it stopped

Synthetic/proxy-only evidence supports the mechanism but is not direct production or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should replay labeled real or semi-real local-agent traces against replay and stronger non-replay baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Realistic Local-Agent Red-Team Traces Against Stronger Baselines
- Success threshold: Ledger replay improves recall by at least 25 percentage points over the strongest non-replay baseline while keeping benign false-positive rate below 5% on the labeled trace set.
- Stop condition: Stop if replay recall is not materially higher than the strongest non-replay baseline, if false-positive rate exceeds 10%, or if labeled realistic traces cannot be assembled without private evidence.

## Evidence references

- Artifact root: `<local-path>/projects/red-team-ledger-replay-for-local-agent-safety-dec735b5b53d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
