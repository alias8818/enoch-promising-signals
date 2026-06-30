# Held-out public fact-verification benchmark for evidence-ledger gating

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `held-out-public-fact-verification-benchmark-for-evidence-l-758247107a`
Run ID: `held-out-public-fact-verification-benchmark-for-evidence-l-758247107a-20260609T024012561704+0000`

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

- Parent run decision: Real-Agent Evidence Ledger on Public Fact Verification: enoch://control-plane/projects/real-agent-evidence-ledger-on-public-fact-verification-227d304520/runs/real-agent-evidence-ledger-on-public-fact-verification-227d304520-20260608T234035847372+0000
- Parent run decision: Evidence-Ledger Tool Agent: enoch://control-plane/projects/evidence-ledger-tool-agent-694a643b3495/runs/evidence-ledger-tool-agent-694a643b3495-20260608T200732045104+0000

## What looked useful

Evidence ledgers contain real claim-aligned signal: claim_plus_ledger_nb reached 0.5300 accuracy and 0.3436 macro-F1 versus claim_only_nb at 0.4476 accuracy and 0.2912 macro-F1, while shuffled_ledger_gated_nb fell to 0.4652 accuracy and 0.2638 macro-F1. The gate itself was mixed: ledger_gated_nb changed accuracy by -0.0032, macro-F1 by +0.0027, and NEE F1 by +0.0111 versus ungated ledger NB, with unstable gate rates and NEE precision across seeds.

## Boundaries and scale limits

This run used 3,068 public training claims and 500 held-out public dev claims, a lexical verifier, and provided QA evidence fields. It did not test neural verifiers, live retrieval, exact evidence-set scoring, additional public datasets, or human provenance audits.

## Claim scope

On the public AVeriTeC train/dev split with simple lexical Naive Bayes verifiers, claim-aligned QA evidence ledgers improve held-out fact-verification label metrics over claim-only and metadata baselines, and shuffled ledgers degrade performance. The calibrated evidence-ledger gate gives only a tiny macro-F1 and Not Enough Evidence F1 lift over ungated ledger NB while slightly reducing accuracy and showing unstable gate precision/recall across five fixed seeds.

## Why it stopped

Tier 2 held-out evidence supports ledger usefulness but not robust evidence-ledger gating; the gate improvement is too small and unstable for a paper-positive decision.

## Recommended next action

Stop this branch as no-paper useful signal; a bounded follow-up should test whether a stronger verifier plus selective-risk objective makes ledger gating stable rather than relying on this weak lexical gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Selective-risk evidence-ledger gating with a stronger verifier on AVeriTeC
- Success threshold: Across at least five fixed seeds, gated verifier improves selective risk by at least 5% relative and Not Enough Evidence F1 by at least 0.03 absolute versus ungated verifier, with accuracy no worse than 0.005 absolute below ungated and shuffled-ledger control losing at least 0.03 macro-F1.
- Stop condition: Stop as negative if the stronger verifier gate fails the NEE F1 or selective-risk threshold on AVeriTeC dev, or if gains disappear under fixed-seed repeats.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-public-fact-verification-benchmark-for-evidence-l-758247107a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
