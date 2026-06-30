# Independent adjudication of evidence-ledger tool-error labels

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `independent-adjudication-of-evidence-ledger-tool-error-lab-0a60bec592`
Run ID: `independent-adjudication-of-evidence-ledger-tool-error-lab-0a60bec592-20260602T165009525417+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Replay evidence-ledger policy on real agent tool-error traces: enoch://control-plane/projects/replay-evidence-ledger-policy-on-real-agent-tool-error-tra-00ee1f9dc7/runs/replay-evidence-ledger-policy-on-real-agent-tool-error-tra-00ee1f9dc7-20260531T223028136502+0000
- Parent run decision: Blinded audit of evidence-ledger tool-error policy on frozen real traces: enoch://control-plane/projects/blinded-audit-of-evidence-ledger-tool-error-policy-on-froz-11c1dd20da/runs/blinded-audit-of-evidence-ledger-tool-error-policy-on-froz-11c1dd20da-20260601T045630766017+0000

## What looked useful

Independent adjudication over trace evidence reached 0.924808 accuracy and 0.914033 macro-F1 in the nominal regime versus ledger-only 0.774050/0.767257 and error-code-only 0.848592/0.831860; it corrected about 0.90 of ledger mislabels with very low false positives but retained about 0.21 false negatives.

## Boundaries and scale limits

No real production or public evidence-ledger traces were available in this workspace; the generator and adjudicator use hand-specified scenario semantics and noise processes. The result supports the adjudication mechanism but does not establish external validity across real tool stacks, domains, or human expert labels.

## Claim scope

In a controlled synthetic evidence-ledger benchmark with fixed latent tool-call causes, noisy ledger labels, five corruption regimes, and 2.5M generated traces, an independent rule-based trace adjudicator improves tool-error label accuracy and macro-F1 over ledger-only, execution-failure-only, and error-code-only baselines.

## Why it stopped

The mechanism was supported in a bounded controlled benchmark, but the evidence is synthetic/proxied rather than real ledger evidence, so it is not paper-positive.

## Recommended next action

Stop as no-paper useful signal; next concrete test is a bounded real-trace adjudication study using public or instrumented agent/tool-call logs with independent human or expert-derived labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace validation of independent evidence-ledger tool-error adjudication
- Success threshold: Trace adjudication beats both ledger-only and error-code-only baselines by >=0.05 macro-F1, correction rate is >=0.50 on ledger mislabels, and false-positive rate is <=0.05 across at least two tool domains.
- Stop condition: Stop negative if real-trace macro-F1 lift is <0.02 over the best baseline, if false-positive rate exceeds 0.10, or if available traces lack enough evidence to adjudicate causality.

## Evidence references

- Artifact root: `<local-path>/projects/independent-adjudication-of-evidence-ledger-tool-error-lab-0a60bec592`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
