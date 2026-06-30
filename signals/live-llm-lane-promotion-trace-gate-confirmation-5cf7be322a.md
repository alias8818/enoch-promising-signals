# Live LLM lane-promotion trace gate confirmation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-llm-lane-promotion-trace-gate-confirmation-5cf7be322a`
Run ID: `live-llm-lane-promotion-trace-gate-confirmation-5cf7be322a-20260613T104757496362+0000`

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

- Parent run decision: Evidence-ledger agent reliability for lane promotion decisions: enoch://control-plane/projects/evidence-ledger-agent-reliability-for-lane-promotion-decisions-32a2a3832c09/runs/evidence-ledger-agent-reliability-for-lane-promotion-decisions-32a2a3832c09-20260613T093751979460+0000
- Parent run decision: Evidence-ledger gate on LLM-generated lane-promotion traces: enoch://control-plane/projects/evidence-ledger-gate-on-llm-generated-lane-promotion-trace-fcdf51f7be/runs/evidence-ledger-gate-on-llm-generated-lane-promotion-trace-fcdf51f7be-20260613T095500220961+0000

## What looked useful

Trace gate F1 was 0.919 with 564 promotion cost units and 0 critical false negatives. Transcript keyword baseline F1 was 0.664 with 1116 cost units and 0 critical false negatives. Always-promote baseline F1 was 0.498 with 2000 cost units and 0 critical false negatives. The trace gate missed 100 noncritical accumulated-risk promotions, so the mechanism is promising but not paper-ready.

## Boundaries and scale limits

Evidence is synthetic and gate-decision-only. It does not validate production traces, actual live LLM adjudication quality, user-visible task outcomes, latency under serving load, or robustness to adversarial/misclassified traces.

## Claim scope

On a deterministic synthetic replay suite of 2000 structured agent traces over fixed seeds 11, 17, 23, 29, and 31, a structured trace gate improved lane-promotion F1 and reduced live-LLM promotion cost relative to transcript-keyword and always-promote baselines while preserving zero critical false negatives.

## Why it stopped

Tier 2 local confirmation produced moderate synthetic evidence for the gate mechanism, but not direct production or live-model evidence sufficient for publication.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should replay real controller traces with blinded labels and the same baselines before any paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded real-trace lane-promotion gate replay
- Success threshold: Trace gate has zero critical false negatives, F1 at least 0.10 above transcript-keyword baseline, and live-LLM promotion cost at least 35% lower than transcript-keyword baseline with recall no more than 0.05 absolute lower.
- Stop condition: Stop as unsupported if any critical false negatives occur or if cost savings require more than a 0.05 absolute recall loss versus transcript-keyword baseline.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-lane-promotion-trace-gate-confirmation-5cf7be322a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
