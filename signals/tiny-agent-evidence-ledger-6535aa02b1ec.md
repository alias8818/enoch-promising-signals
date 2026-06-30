# Tiny Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-6535aa02b1ec`
Run ID: `tiny-agent-evidence-ledger-6535aa02b1ec-20260605T033943945711+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/28b2f05902ed

## What looked useful

The prototype detected 4/4 injected tamper cases in smoke, 10000-record, and 100000-record runs. At 100000 records, ledger append averaged 15.298 microseconds per record, verification averaged 8.887 microseconds per record, and size overhead was 261 bytes per record versus plain JSONL.

## Boundaries and scale limits

Tested only with synthetic events up to 100000 records on one local file. No live LLM/tool-agent traces, human audit outcomes, external anchoring, digital signatures, trusted timestamps, concurrent writers, crash-recovery tests, or adversaries able to rewrite the full ledger suffix were evaluated.

## Claim scope

A local append-only SHA-256 hash-chained JSONL ledger can make synthetic tiny-agent evidence records tamper-evident for payload edits, deletion, reordering, and single-record rehashing while adding about 15 microseconds append latency and 261 bytes per 512-byte record on this host.

## Why it stopped

No-paper useful signal: the mechanism worked under synthetic local tests, but this is not direct live-agent, human-audit, or adversarial-storage evidence.

## Recommended next action

Run a bounded live-agent integration test with real tool transcripts and reviewer audit metrics before considering any paper or broader provenance claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Tiny-Agent Evidence Ledger Audit Test
- Success threshold: Ledger-backed review improves unsupported-claim detection accuracy by at least 15 percentage points or reduces review time by at least 20 percent without reducing accuracy, while append overhead remains below 1 millisecond per event and all seeded tamper cases are detected.
- Stop condition: Stop if live-agent instrumentation cannot capture complete evidence records, if ledger overhead exceeds 1 millisecond per event on small tasks, or if reviewer metrics show no accuracy or time benefit versus plain transcripts.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-6535aa02b1ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
