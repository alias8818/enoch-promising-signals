# Agent Reliability via Evidence Ledger for Small Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-via-evidence-ledger-for-small-models-c97cbdddf51b`
Run ID: `agent-reliability-via-evidence-ledger-for-small-models-c97cbdddf51b-20260605T063411076199+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/a116fa268fd9

## What looked useful

The small model answered all synthetic location questions correctly but ignored requested JSON and citations in both baseline and ledger-prompt conditions. A deterministic ledger controller over the same evidence packets achieved 100% support citation and strict accuracy by extracting the verified matching evidence row, indicating that reliability gains came from an external evidence ledger/control layer rather than from prompting the small model to self-ledger.

## Boundaries and scale limits

Synthetic single-turn tasks only; evidence rows follow a regular template; no real tool use, long-horizon agent memory, open-domain retrieval, noisy documents, multi-model comparison, or human workload evaluation.

## Claim scope

On an 80-case synthetic evidence-grounded QA benchmark using google/flan-t5-small, prompt-only ledger instructions did not improve reliability, but an explicit evidence-ledger controller converted answer-only model outputs into fully supported answer+citation records without reducing answer accuracy.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports the controller mechanism but prompt-only ledgering failed and the benchmark is too templated for publication-grade claims.

## Recommended next action

Run a bounded direct agent benchmark with irregular evidence text and tool traces, comparing answer-only small-model agents against explicit ledger-controller agents on answer correctness, citation validity, and abstention behavior.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger controller on irregular small-agent tool traces
- Success threshold: Ledger-controller strict grounded-answer accuracy improves by >=10 percentage points over both baselines with <=2 percentage point answer-accuracy loss on at least 200 irregular cases.
- Stop condition: Stop if the controller cannot parse enough irregular evidence to cover 90% of cases, or if strict accuracy improves by less than 5 percentage points on the first 100 cases.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-evidence-ledger-for-small-models-c97cbdddf51b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
