# Live native decision-ledger anchoring on labeled agent incident runs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-native-decision-ledger-anchoring-on-labeled-agent-inc-dac8db7510`
Run ID: `live-native-decision-ledger-anchoring-on-labeled-agent-inc-dac8db7510-20260529T095143350615+0000`

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

- Parent run decision: Hash-Chained Decision Ledger for Agent Reliability Drift Detection: enoch://control-plane/projects/hash-chained-decision-ledger-for-agent-reliability-drift-detection-f425985636ea/runs/hash-chained-decision-ledger-for-agent-reliability-drift-detection-f425985636ea-20260529T032721019597+0000
- Parent run decision: Anchored decision ledger replay on real agent incident traces: enoch://control-plane/projects/anchored-decision-ledger-replay-on-real-agent-incident-tra-676863184d/runs/anchored-decision-ledger-replay-on-real-agent-incident-tra-676863184d-20260529T071051130048+0000

## What looked useful

Ledger structure carries real signal above raw text and permutation controls, but the strongest evidence indicates much of the gain comes from ordinary telemetry and model/run identity rather than native ledger anchoring itself.

## Boundaries and scale limits

Single public trace corpus, MBPP subset only, labels derived by executing final answers against prompt asserts; not a live deployment, not cross-corpus, not pre-incident/online prediction, and no private operational incident labels.

## Claim scope

On 1,000 real MBPP agent traces from pagarsky/agent-trace, compact trace-native decision-ledger features can predict benchmark failure labels derived from prompt asserts better than raw trace text and shuffled controls, but they do not materially beat simple telemetry/model baselines.

## Why it stopped

Tier 2 validation produced a mixed result: anchored ledgers beat raw text and shuffled controls, but failed the stronger threshold of outperforming real telemetry baselines, so the idea is not paper-positive.

## Recommended next action

Stop this branch as no-paper evidence; run a bounded deepen follow-up that tests pre-error ledgers without model/run identity on a second labeled trace corpus and requires improvement over telemetry-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pre-error identity-free ledger prediction on a second labeled agent trace corpus
- Success threshold: Across at least 5 fixed grouped splits, identity-free pre-error ledger features improve over telemetry-only by at least +0.03 failure F1 and +0.03 ROC-AUC, with shuffled-ledger control near chance.
- Stop condition: Stop negative if ledger-prefix features fail to beat telemetry-only by both thresholds or if the effect disappears when model/run identity and final outcome markers are removed.

## Evidence references

- Artifact root: `<local-path>/projects/live-native-decision-ledger-anchoring-on-labeled-agent-inc-dac8db7510`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
