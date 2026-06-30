# Realistic Tool-Trace Evidence Ledger Evaluation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `realistic-tool-trace-evidence-ledger-evaluation-b460fb74ff`
Run ID: `realistic-tool-trace-evidence-ledger-evaluation-b460fb74ff-20260602T161846611772+0000`

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

- Parent run decision: Compressed Evidence Ledger for Tool-Use Agents: enoch://control-plane/projects/compressed-evidence-ledger-for-tool-use-agents-0f8d62b8f19e/runs/compressed-evidence-ledger-for-tool-use-agents-0f8d62b8f19e-20260602T112211185029+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/66e0858ba973

## What looked useful

Ledger verifier reached 1.000 macro-F1 and 0.000 false-positive rate on unsupported/contradicted claims; transcript-overlap baseline reached 0.283 macro-F1 and 0.318 false-positive rate on unsupported/contradicted claims. The predefined Tier 1 threshold was passed.

## Boundaries and scale limits

Small hand-authored fixture set; parser predicates are predefined; baseline is simple; no human audit study, model-generated ledger study, adversarial trace set, or production-scale held-out corpus was tested.

## Claim scope

A deterministic typed evidence ledger can verify supported, unsupported, and contradicted claims on a 10-case, 40-claim controlled fixture set of realistic shell/tool traces better than a transcript-overlap baseline.

## Why it stopped

Tier 1 mechanism support only; result is not paper-positive because it uses a small controlled hand-authored fixture rather than broad real traces or human/model ledger production.

## Recommended next action

Run a blinded deepen test on held-out real agent traces with model-written ledgers and a stronger retrieval or LLM audit baseline; stop paper pursuit unless the ledger maintains at least 0.85 macro-F1 and halves unsupported-claim false positives after ledger-construction cost is included.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded Held-Out Agent Trace Evidence Ledger Audit
- Success threshold: Ledger macro-F1 >= 0.85 and unsupported/contradicted false-positive rate reduced by >= 50% versus the stronger baseline, with median ledger construction plus audit time no more than 2x baseline audit time.
- Stop condition: Stop if macro-F1 falls below 0.75, false-positive reduction is below 25%, or ledger construction plus audit time exceeds 3x baseline audit time on the held-out trace set.

## Evidence references

- Artifact root: `<local-path>/projects/realistic-tool-trace-evidence-ledger-evaluation-b460fb74ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
