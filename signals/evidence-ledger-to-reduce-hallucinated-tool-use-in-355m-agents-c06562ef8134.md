# Evidence Ledger to Reduce Hallucinated Tool Use in 355M Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-to-reduce-hallucinated-tool-use-in-355m-agents-c06562ef8134`
Run ID: `evidence-ledger-to-reduce-hallucinated-tool-use-in-355m-agents-c06562ef8134-20260529T233213383736+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3f2524755b31

## What looked useful

Across five seeds of 180 examples each, the evidence-ledger condition reduced unsupported call rate from 0.680 to 0.227 versus baseline, while supported-call recall fell from 0.743 to 0.267. A rule-only control reduced unsupported calls only to 0.583, suggesting the ledger entries caused most of the shift.

## Boundaries and scale limits

Synthetic examples only; log-probability label scoring only; no real tools, no interactive trajectories, no fine-tuning, no instruction-tuned 355M agent, and no production traces. The result should not be generalized to real agent task success.

## Claim scope

On a synthetic CALL/NO_CALL tool-decision benchmark scored with GPT-2-medium (355M parameters), an explicit evidence-ledger prompt reduced unsupported tool-call preference relative to baseline and a rule-only control, but made the model substantially over-conservative.

## Why it stopped

Proxy/local 355M evidence supports a safety mechanism but shows a severe recall tradeoff and lacks direct interactive-agent validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should redesign the ledger format to preserve supported-call recall while retaining unsupported-call suppression on the same benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Recall-Preserving Evidence Ledger Format for 355M Tool Decisions
- Success threshold: Unsupported call rate at least 0.25 below baseline and supported-call recall no more than 0.10 below baseline across five seeds.
- Stop condition: Stop if all tested ledger variants either reduce supported-call recall by more than 0.20 or fail to reduce unsupported call rate by at least 0.15 versus baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-to-reduce-hallucinated-tool-use-in-355m-agents-c06562ef8134`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
