# Tamper-Evident Agent Reasoning Ledger with Merkle Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tamper-evident-agent-reasoning-ledger-with-merkle-verification-9a1f0fe58683`
Run ID: `tamper-evident-agent-reasoning-ledger-with-merkle-verification-9a1f0fe58683-20260525T015641867381+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8993b96b9aa6

## What looked useful

The mechanism is practical at small local scale and gives logarithmic inclusion proofs, but coherent ledger rewrites remain self-consistent unless a trusted root is published outside the attacker's control.

## Boundaries and scale limits

Synthetic CPU-only traces up to 32768 entries; no real agent runtime, isolated logger, external signature/TSA/blockchain anchoring, multi-writer workload, redaction workflow, or auditor acceptance test.

## Claim scope

A dependency-free local Python prototype shows that hash-chained reasoning entries plus Merkle roots detect content edits, deletion, reordering, and invalid inclusion proofs on synthetic traces when verification uses a trusted prior root.

## Why it stopped

Local synthetic evidence supports the engineering mechanism but not a publication-grade or novel research claim; the decisive limitation is the need for external root anchoring.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should integrate an isolated logger with signed or timestamped Merkle-root publication and test adversarial omission/rewrite/fork attempts on real agent traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Externally Anchored Agent Trace Ledger Under Adversarial Rewrite Tests
- Success threshold: Detect 100% of injected omission, rewrite, deletion, reorder, truncation, and fork attacks that occur after a checkpoint, while adding less than 5% median runtime overhead on a representative tool-using agent benchmark.
- Stop condition: Stop if the logger cannot be isolated from agent-controlled code, roots cannot be retained outside the attacker's control, or overhead exceeds 20% median runtime after straightforward batching.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-agent-reasoning-ledger-with-merkle-verification-9a1f0fe58683`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
