# Held-Out Natural Malformed Tool-Call Router Replay

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `held-out-natural-malformed-tool-call-router-replay-dba2469a9e`
Run ID: `held-out-natural-malformed-tool-call-router-replay-dba2469a9e-20260526T220739682908+0000`

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

- Parent run decision: Real-Trace Validation of Tool-Call Validator Router: enoch://control-plane/projects/real-trace-validation-of-tool-call-validator-router-c48fccdb0d/runs/real-trace-validation-of-tool-call-validator-router-c48fccdb0d-20260526T152101262702+0000
- Parent run decision: Tool-Call Validator Router for Local Agents: enoch://control-plane/projects/tool-call-validator-router-for-local-agents-f47b621389b4/runs/tool-call-validator-router-for-local-agents-f47b621389b4-20260526T075411001654+0000

## What looked useful

Schema-guided replay improves executable recovery over no-schema repair (87.5% vs 81.25%) and strongly over strict JSON parsing (0%) and no-repair scoring (27.5%), with zero false accepts on the generated negative set.

## Boundaries and scale limits

The corpus is generated from natural-looking templates and perturbations, not real production malformed traces; no LLM-in-the-loop serving replay, human annotation, or downstream side-effect safety evaluation was performed.

## Claim scope

On a deterministic generated replay benchmark with 10,000 malformed tool-call positives and 1,000 negatives across five fixed seeds, a schema-guided replay router recovered the intended route for all malformed positives and executable arguments for 87.5% while producing zero false accepts.

## Why it stopped

No-paper closure because the Tier 2 local result is a useful generated-benchmark signal but not real-trace publication evidence.

## Recommended next action

Run one deepen follow-up on a small real malformed tool-call trace corpus with human-labeled intended route and arguments; stop paper consideration unless the schema-guided lift persists on real traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Malformed Tool-Call Router Replay
- Success threshold: Replay router executable accuracy is at least 5 percentage points above no-schema repair, route accuracy is at least 95%, and false accept rate is at most 1% on the real held-out trace set.
- Stop condition: Stop if the real-trace executable-recovery lift is under 2 percentage points, route accuracy falls below 90%, or false accepts exceed 2%.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-natural-malformed-tool-call-router-replay-dba2469a9e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
