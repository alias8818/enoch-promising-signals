# Live LLM evidence-ledger diagnostic memory test on noisy unmarked shell traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-llm-evidence-ledger-diagnostic-memory-test-on-noisy-u-a2e95c8d0d`
Run ID: `live-llm-evidence-ledger-diagnostic-memory-test-on-noisy-u-a2e95c8d0d-20260610T184940995410+0000`

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

- Parent run decision: Live shell-agent evidence-ledger memory test on generated diagnostic traces: enoch://control-plane/projects/live-shell-agent-evidence-ledger-memory-test-on-generated-b345a29e0a/runs/live-shell-agent-evidence-ledger-memory-test-on-generated-b345a29e0a-20260610T111430179620+0000
- Parent run decision: Evidence-ledger vs flat-scratchpad shell agent: enoch://control-plane/projects/evidence-ledger-vs-flat-scratchpad-shell-agent-7a7f2f312eda/runs/evidence-ledger-vs-flat-scratchpad-shell-agent-7a7f2f312eda-20260610T060351799288+0000

## What looked useful

Evidence ledgering can materially help a small LLM diagnose noisy unmarked shell traces relative to raw traces, but much of the gain comes from compacting the signal lines: a lossy ledger with the wrong diagnosis row still scored 45.6% joint accuracy, only 7.8 points below the oracle ledger.

## Boundaries and scale limits

Single small cached LLM for the medium run; synthetic shell traces; oracle ledger rather than automatic extraction; no real incident traces, larger-model medium run, or robustness sweep across ledger formats.

## Claim scope

On 180 seeded synthetic noisy unmarked shell-trace diagnostic cases with google/flan-t5-small, an oracle evidence ledger improved joint diagnosis-and-evidence accuracy over the raw trace baseline by 40.0 percentage points, but did not meet the stricter Tier 2 threshold against the lossy-ledger ablation or the 60% absolute diagnosis-accuracy floor.

## Why it stopped

Tier 2 medium evidence produced a useful mechanism signal but failed the predeclared success threshold: oracle ledger joint accuracy was +40.0 points over raw, but only +7.8 points over lossy ablation and diagnosis accuracy was 53.3%, below the 60% floor.

## Recommended next action

Do not write a paper from this run; run a bounded deepen test with a stronger model, an automatically extracted ledger, and stricter no-diagnosis-row ablations on semi-real shell traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Automatic and no-label evidence ledgers for stronger-model shell-trace diagnosis
- Success threshold: Automatic ledger joint accuracy >= raw-trace joint accuracy + 0.10, >= every ablation by +0.10, diagnosis accuracy >= 0.60, and paired sign-test p < 0.01 versus raw and the strongest ablation.
- Stop condition: Stop if automatic or no-diagnosis ledgers fail to beat raw by 10 points or if a stronger model cannot exceed 60% diagnosis accuracy within the bounded case budget.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-evidence-ledger-diagnostic-memory-test-on-noisy-u-a2e95c8d0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
