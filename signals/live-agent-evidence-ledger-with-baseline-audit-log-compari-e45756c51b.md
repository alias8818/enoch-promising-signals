# Live Agent Evidence Ledger With Baseline Audit Log Comparison

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-agent-evidence-ledger-with-baseline-audit-log-compari-e45756c51b`
Run ID: `live-agent-evidence-ledger-with-baseline-audit-log-compari-e45756c51b-20260525T224551026043+0000`

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

- Parent run decision: Tamper-Evident Evidence Ledger for Small Tool-Using Agents: enoch://control-plane/projects/tamper-evident-evidence-ledger-for-small-tool-using-agents-f9477609b74b/runs/tamper-evident-evidence-ledger-for-small-tool-using-agents-f9477609b74b-20260525T214530501498+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e67dcf88cc54

## What looked useful

The evidence ledger reached 1.000 recall on 500 injected defects with 0.000 false positive rate on 100 clean episodes; the baseline audit log reached 0.000 recall and 0.000 false positive rate. Mean serialized storage overhead was 2.923x.

## Boundaries and scale limits

Synthetic deterministic episodes only; no real LLM agent traces, production audit logs, human auditor study, concurrent agents, distributed storage, adversarial actors, or long-horizon operational overhead were tested.

## Claim scope

In a controlled 600-episode synthetic direct test of agent-like file-read, command-result, mutation, and final-claim traces, an explicit evidence ledger detected injected claim-support, freshness, provenance, tamper, and missing-evidence defects that a plain chronological audit log did not detect.

## Why it stopped

Controlled Tier 1 evidence supports the mechanism but is not publication-grade and does not validate live production agent settings.

## Recommended next action

Run a bounded deepen follow-up on real live-agent traces with seeded evidence defects and a stronger post-hoc audit-log baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Trace Evidence Ledger Versus Strong Audit Baseline
- Success threshold: Evidence ledger recall exceeds strong audit-log recall by at least 0.25 across all seeded defects, ledger false positive rate is <= 0.05 on clean traces, and storage overhead is < 5x.
- Stop condition: Stop as negative if recall improvement is < 0.10, ledger false positive rate exceeds 0.10, or storage overhead reaches >= 10x on the real-trace corpus.

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-evidence-ledger-with-baseline-audit-log-compari-e45756c51b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
