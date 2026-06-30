# Anchored evidence ledger verification across heterogeneous agent-tool traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchored-evidence-ledger-verification-across-heterogeneous-ad8ac1683b`
Run ID: `anchored-evidence-ledger-verification-across-heterogeneous-ad8ac1683b-20260607T115308365667+0000`

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

- Parent run decision: Evidence ledger verification on real or replayed agent-tool traces: enoch://control-plane/projects/evidence-ledger-verification-on-real-or-replayed-agent-too-f39664174c/runs/evidence-ledger-verification-on-real-or-replayed-agent-too-f39664174c-20260607T084909283285+0000
- Parent run decision: Evidence ledger infrastructure for agent reliability: enoch://control-plane/projects/evidence-ledger-infrastructure-for-agent-reliability-250ad63a40d2/runs/evidence-ledger-infrastructure-for-agent-reliability-250ad63a40d2-20260607T052838375790+0000

## What looked useful

Across 1,600 generated traces and 9,600 verifier trials, full anchoring achieved 1.0 recall, 1.0 precision, 1.0 localization accuracy, and 0.0 false-positive rate. Schema-only verification missed all attacks, whole-trace hashing could not localize and missed forged-ledger rewrites, and ablations failed on their intended mechanism-specific attack families.

## Boundaries and scale limits

Evidence is limited to synthetic traces and purpose-built parsers. No real production agent logs, third-party framework exports, adversarial parser edge cases, multi-party key management, or long-horizon operational replay were tested.

## Claim scope

In a fixed-seed synthetic testbed with four heterogeneous agent-tool trace formats, an anchored evidence ledger using canonical per-step hashes, predecessor-anchor binding, and HMAC-signed entries detected and localized seeded trace/ledger tampering better than schema-only and whole-trace-hash baselines.

## Why it stopped

Medium synthetic evidence supports the mechanism but is not publication-grade direct evidence on real-world traces.

## Recommended next action

Run the same seeded tampering protocol on real heterogeneous agent/tool traces exported from at least two existing frameworks before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace anchored evidence ledger verification with seeded tampering
- Success threshold: Full anchoring reaches recall >= 0.95, localization accuracy >= 0.90, false-positive rate <= 0.02, and outperforms both real baselines by at least 0.20 localization accuracy on attacked traces.
- Stop condition: Stop if real framework parser normalization causes false positives above 0.05 on clean traces or if full anchoring fails to exceed 0.85 recall on any major trace format after parser bugs are fixed.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-evidence-ledger-verification-across-heterogeneous-ad8ac1683b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
