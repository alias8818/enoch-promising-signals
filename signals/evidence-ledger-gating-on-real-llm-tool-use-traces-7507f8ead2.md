# Evidence-ledger gating on real LLM tool-use traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-gating-on-real-llm-tool-use-traces-7507f8ead2`
Run ID: `evidence-ledger-gating-on-real-llm-tool-use-traces-7507f8ead2-20260608T033512531471+0000`

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

- Parent run decision: Evidence-Ledger Agent Reliability Framework: enoch://control-plane/projects/evidence-ledger-agent-reliability-framework-78b6379aa010/runs/evidence-ledger-agent-reliability-framework-78b6379aa010-20260607T225428365244+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fec5ab3734c4

## What looked useful

On 762 controlled cited claims from 1,267 real command evidence items, the strict gate achieved F1 1.0 with 0 false positives and 0 false negatives; citation-exists and lexical baselines failed to block many counterfactual claims.

## Boundaries and scale limits

Claims were controlled and structured rather than extracted from messy natural final answers; no live agent-loop intervention, paraphrase entailment, adversarial output injection, or human-labeled natural claim audit was tested.

## Claim scope

Strict evidence-ledger gating over structured, cited exit-code and output-quote claims generated from 24 real Codex tool-use traces.

## Why it stopped

Tier 1 mechanism threshold passed on real traces, but this remains controlled structured-claim evidence rather than publication-grade validation of free-form agent final answers.

## Recommended next action

Run a bounded natural-final-answer audit: extract claims from real agent final messages, require evidence IDs or map them to ledger items, and measure human-checked support/block accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural final-answer evidence-ledger audit on real Codex traces
- Success threshold: Support F1 >= 0.90, unsupported false-accept rate <= 0.05, and at least 2x lower unsupported false-accept rate than the best baseline.
- Stop condition: Stop if claim extraction yields fewer than 100 auditable claims, if unsupported false-accept rate exceeds 0.10 after calibration, or if errors are dominated by ambiguous labels requiring private/human context unavailable to the worker.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gating-on-real-llm-tool-use-traces-7507f8ead2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
