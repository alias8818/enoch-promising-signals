# Independent Trace Corpus Test for Evidence Ledger Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `independent-trace-corpus-test-for-evidence-ledger-verifica-35fffc8b0a`
Run ID: `independent-trace-corpus-test-for-evidence-ledger-verifica-35fffc8b0a-20260531T223030288674+0000`

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

- Parent run decision: Falsifiable Evidence Ledger for Tool-Calling Agents: enoch://control-plane/projects/falsifiable-evidence-ledger-for-tool-calling-agents-c3266a94073e/runs/falsifiable-evidence-ledger-for-tool-calling-agents-c3266a94073e-20260531T113313505965+0000
- Parent run decision: Evidence Ledger Verification on Model-Generated Tool Traces: enoch://control-plane/projects/evidence-ledger-verification-on-model-generated-tool-trace-42876f124a/runs/evidence-ledger-verification-on-model-generated-tool-trace-42876f124a-20260531T145301427186+0000

## What looked useful

The medium synthetic benchmark supports the mechanism and shows that each ledger component has distinct value: artifact hashes catch artifact edits, anchored chains catch content/order/deletion edits, and cross-reference invariants catch internally re-chained evidence-reference attacks. A flat manifest baseline only catches artifact edits.

## Boundaries and scale limits

Synthetic corpus only; not validated on real externally produced trace corpora, production ledgers, uncontrolled adversaries, long-running workflows, or heterogeneous artifact stores.

## Claim scope

In a fixed-seed synthetic independent-trace corpus with two simulated producers and seven labeled tamper classes, a full evidence ledger using canonical record hashing, an anchored terminal ledger head, artifact hashes, and claim/evidence cross-reference invariants detects and localizes all tested corruptions with zero clean false positives, outperforming schema and flat-manifest baselines.

## Why it stopped

No-paper useful signal: Tier 2 synthetic evidence supports the mechanism but does not satisfy real-corpus publication readiness.

## Recommended next action

Run the same verifier and ablation suite on an externally sourced real trace corpus before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Independent Trace Corpus Evidence Ledger Verification
- Success threshold: Full ledger F1 >= 0.95, localization accuracy >= 0.90, clean false-positive rate <= 0.01, and at least 0.20 F1 improvement over the best real baseline.
- Stop condition: Stop if the full ledger F1 falls below 0.85, clean false-positive rate exceeds 0.05, or no suitable real independent trace corpus can be obtained without private/manual evidence.

## Evidence references

- Artifact root: `<local-path>/projects/independent-trace-corpus-test-for-evidence-ledger-verifica-35fffc8b0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
