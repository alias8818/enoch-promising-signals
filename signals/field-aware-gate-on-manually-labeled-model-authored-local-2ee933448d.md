# Field-aware gate on manually labeled model-authored local-agent claims

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `field-aware-gate-on-manually-labeled-model-authored-local-2ee933448d`
Run ID: `field-aware-gate-on-manually-labeled-model-authored-local-2ee933448d-20260523T081005439512+0000`

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

- Parent run decision: Field-aware evidence-ledger gate on realistic local-agent tool traces: enoch://control-plane/projects/field-aware-evidence-ledger-gate-on-realistic-local-agent-2760ab2637/runs/field-aware-evidence-ledger-gate-on-realistic-local-agent-2760ab2637-20260523T063234605972+0000
- Parent run decision: Evidence-ledger tool-use for 1B local agent reliability: enoch://control-plane/projects/evidence-ledger-tool-use-for-1b-local-agent-reliability-0236f810616f/runs/evidence-ledger-tool-use-for-1b-local-agent-reliability-0236f810616f-20260523T034904869036+0000

## What looked useful

Per-field thresholds reduced unsupported false accepts by 0.010 absolute but cost 0.075 supported recall and underperformed a shuffled-field threshold control on false accepts. Field as a classifier feature reduced false accepts by 0.010 with 0.005 recall loss and +0.010 safety utility, but the paired utility gain was not statistically persuasive.

## Boundaries and scale limits

Claims were generated from manually labeled templates with simulated confidence/evidence signals, not sampled from live production agent transcripts or independently human-labeled real logs. The run used five fixed split seeds and a small lexical classifier, so it is a bounded local confirmation/falsification rather than broad deployment evidence.

## Claim scope

On a 960-claim manually labeled local-agent-style benchmark with fixed train/validation/test seeds, per-field thresholding did not improve the safety/recall tradeoff over a global threshold baseline; field as a model feature gave only a small non-significant utility improvement.

## Why it stopped

Tier 2 bounded evidence did not support the threshold-heterogeneity mechanism strongly enough for a paper: the field-threshold method lost too much recall, and the field-feature variant was only a small unstable useful signal.

## Recommended next action

Stop this branch as no-paper evidence; if continuing, run one bounded real-log follow-up with independently labeled local-agent claims and a pre-registered false-accept reduction threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Field-aware claim gate on independently labeled real local-agent transcripts
- Success threshold: At least 25% relative reduction in unsupported false-accept rate versus the global threshold baseline, no more than 0.02 absolute supported-recall loss, positive safety-utility gain on at least 4 of 5 fixed seeds, and shuffled-field control below the real field-aware gate.
- Stop condition: Stop if real-log labels show less than 10% relative false-accept reduction, more than 0.02 supported-recall loss, or no advantage over shuffled-field controls after the pre-registered fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/field-aware-gate-on-manually-labeled-model-authored-local-2ee933448d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
