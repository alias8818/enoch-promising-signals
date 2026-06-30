# Evidence Ledger to Reduce Tool Misuse in 124M Local Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-to-reduce-tool-misuse-in-124m-local-agents-63687b9bc117`
Run ID: `evidence-ledger-to-reduce-tool-misuse-in-124m-local-agents-63687b9bc117-20260523T233003123859+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/84a15477df72

## What looked useful

Evidence ledger reduced blocked-case misuse from 88.3% to 46.7% but increased allowed-case over-refusal from 0.0% to 50.0%. It fixed unauthorized_write and unsafe_delete, partially reduced unsafe_email, and failed on missing_read_target and unneeded_web.

## Boundaries and scale limits

Single model, synthetic scenarios, fixed action-label scoring, no live tool execution, no human-authored agent traces, and exact GPT-Neo-125M control could not run because the local checkpoint cache was incomplete.

## Claim scope

On a 120-case synthetic fixed-candidate tool-action benchmark using a cached 135M-class local instruct model, an evidence-ledger prompt reduced unauthorized/unnecessary tool-choice rate on blocked cases but introduced substantial over-refusal on authorized cases.

## Why it stopped

No-paper useful signal: the local proxy result is mixed, not a full validation, and the ledger trades substantial misuse reduction for unacceptable over-refusal on valid tool cases.

## Recommended next action

Run a bounded deepen follow-up with a calibrated authorization verifier or thresholded policy layer to test whether over-refusal can be reduced while preserving the misuse reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated evidence-ledger gate for small local tool agents
- Success threshold: Compared with the baseline, reduce blocked-case misuse by at least 30 percentage points while keeping allowed-case over-refusal at or below 20%.
- Stop condition: Stop if the calibrated gate cannot keep over-refusal below 20% or if misuse reduction falls below 30 percentage points on the 120-case benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-to-reduce-tool-misuse-in-124m-local-agents-63687b9bc117`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
