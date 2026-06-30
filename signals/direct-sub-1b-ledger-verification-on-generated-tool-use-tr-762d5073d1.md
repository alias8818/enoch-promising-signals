# Direct Sub-1B Ledger Verification on Generated Tool-Use Traces

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `direct-sub-1b-ledger-verification-on-generated-tool-use-tr-762d5073d1`
Run ID: `direct-sub-1b-ledger-verification-on-generated-tool-use-tr-762d5073d1-20260526T203611300738+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Ledger-Grounded Tool Call Verification for Sub-1B Agents: enoch://control-plane/projects/ledger-grounded-tool-call-verification-for-sub-1b-agents-996e467b7837/runs/ledger-grounded-tool-call-verification-for-sub-1b-agents-996e467b7837-20260525T071131635483+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/111b44975757

## What looked useful

The learned sub-1B verifier reached 53.24% test accuracy with 51.06% invalid false-accept rate, below the predeclared threshold and below the 77.13% best heuristic baseline. A deterministic replay oracle validated all generated labels and shows the task is executable, while heuristic total checks remained brittle on intermediate ledger perturbations.

## Boundaries and scale limits

Simulator-generated traces only; one tiny raw character Transformer architecture; 8 epochs; no real LLM/tool-agent traces; no grammar-aware tokenization or instruction-tuned sub-1B model; not a broad claim about all sub-1B verification approaches.

## Claim scope

Tier-1 controlled generated ledger/tool-use traces: a 363,073-parameter raw character Transformer verifier trained on 5,040 examples did not learn reliable ledger verification and did not outperform simple heuristic baselines on a 1,080-example held-out split.

## Why it stopped

Direct Tier-1 threshold was not met: the neural verifier accuracy was 0.5324, false-accept rate was 0.5106, and it underperformed the best heuristic baseline rather than beating it by at least 10 percentage points.

## Recommended next action

Stop this run as a no-paper useful negative signal; the next bounded action is to test a grammar-aware sub-1B verifier against the same perturbation families before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Grammar-Aware Sub-1B Ledger Verification on Generated Tool-Use Traces
- Success threshold: Held-out accuracy >= 0.90, invalid false-accept rate <= 0.10, and at least 10 percentage-point accuracy gain over the best non-oracle heuristic baseline on the same split.
- Stop condition: Stop if the grammar-aware verifier remains below 0.80 accuracy or above 0.20 false-accept rate after a calibrated run under 15 minutes, because the mechanism still lacks Tier-1 support.

## Evidence references

- Artifact root: `<local-path>/projects/direct-sub-1b-ledger-verification-on-generated-tool-use-tr-762d5073d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
