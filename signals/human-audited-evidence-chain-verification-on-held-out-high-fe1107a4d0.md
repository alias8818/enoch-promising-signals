# Human-audited evidence-chain verification on held-out high-risk local-agent traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `human-audited-evidence-chain-verification-on-held-out-high-fe1107a4d0`
Run ID: `human-audited-evidence-chain-verification-on-held-out-high-fe1107a4d0-20260529T232653463482+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evaluate verified safety evidence chains on real small local-agent traces: enoch://control-plane/projects/evaluate-verified-safety-evidence-chains-on-real-small-loc-464e68602b/runs/evaluate-verified-safety-evidence-chains-on-real-small-loc-464e68602b-20260529T093043430782+0000
- Parent run decision: Evaluate evidence-chain safety verification on independent local-agent trace corpus: enoch://control-plane/projects/evaluate-evidence-chain-safety-verification-on-independent-5f7be646f5/runs/evaluate-evidence-chain-safety-verification-on-independent-5f7be646f5-20260529T160945217287+0000

## What looked useful

The structured verifier achieved 1.0000 held-out accuracy and 1.0000 unsupported-claim rejection with 0 false accepts on deterministic trace labels, versus 0.3694 accuracy and 0.7371 unsupported rejection for a calibrated raw trace-text lexical baseline. Ablations degraded in the expected channels.

## Boundaries and scale limits

Labels are deterministic audits from command and exit-status fields rather than independent human-audited annotations; claims are templated and the verifier shares the explicit evidence taxonomy with the label generator.

## Claim scope

Structured evidence-chain verification over deterministic command/event evidence was evaluated on 8,981 held-out high-risk local-agent command events from 776 unrelated local Enoch projects, producing 38,263 trace-grounded claims.

## Why it stopped

Bounded full local validation supports the mechanism at scale, but it did not satisfy the human-audited evidence requirement needed for publication-grade closure.

## Recommended next action

Stop as no-paper useful signal; the next concrete validation is an independent blinded human audit of a stratified held-out sample of at least 500 high-risk claims from the saved dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded human audit of held-out high-risk evidence-chain labels
- Success threshold: Structured verifier false-accept rate below 1% on high-risk unsupported claims, balanced accuracy at least 20 percentage points above both baselines, and no unexamined false accept in destructive/network/permission claim families.
- Stop condition: Stop if human labels show false-accept rate at or above 1% for high-risk unsupported claims, if inter-annotator agreement is too low to define a reliable gold set, or if the structured verifier fails to beat both baselines by 20 balanced-accuracy points.

## Evidence references

- Artifact root: `<local-path>/projects/human-audited-evidence-chain-verification-on-held-out-high-fe1107a4d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
