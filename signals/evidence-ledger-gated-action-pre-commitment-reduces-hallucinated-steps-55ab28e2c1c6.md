# Evidence-Ledger-Gated Action: Pre-Commitment Reduces Hallucinated Steps

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gated-action-pre-commitment-reduces-hallucinated-steps-55ab28e2c1c6`
Run ID: `evidence-ledger-gated-action-pre-commitment-reduces-hallucinated-steps-55ab28e2c1c6-20260611T111701999760+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfc61bad5e15

## What looked useful

Across 10,000 paired episodes per variant, baseline and precommit-only both had 0.7159 unsupported-step episode rate and 1.6465 mean unsupported executed actions, while precommit-ledger-gate had 0.0 unsupported-step episode rate and 0.0 mean unsupported executed actions. A 9-cell sweep preserved the same qualitative result.

## Boundaries and scale limits

No real LLM generation, no natural-language evidence parsing, no real shell/API tools, and the verifier has direct access to symbolic action preconditions and ledger facts.

## Claim scope

In a controlled symbolic tool-state benchmark, enforceable evidence-ledger gating of pre-committed actions eliminated unsupported executed actions; pre-commitment without enforcement did not help.

## Why it stopped

No-paper proxy closure: the mechanism is supported in a symbolic harness, but this is not direct publication-grade evidence for real LLM agents.

## Recommended next action

Run a bounded real local LLM/tool-agent follow-up where the model writes natural-language pre-commitments and a separate verifier checks cited observations before action execution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Local LLM Pre-Commitment Evidence-Ledger Gate
- Success threshold: At least a 50% relative reduction in unsupported executed actions versus precommit-only without more than a 10 percentage point drop in task success on at least 100 paired real-model episodes.
- Stop condition: Stop if the verifier cannot reliably map cited observations to action preconditions, or if the gated variant does not reduce unsupported executed actions by at least 25% in an initial 40-episode smoke run.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gated-action-pre-commitment-reduces-hallucinated-steps-55ab28e2c1c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
