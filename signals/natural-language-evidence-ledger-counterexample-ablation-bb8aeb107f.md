# Natural-language evidence-ledger counterexample ablation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-evidence-ledger-counterexample-ablation-bb8aeb107f`
Run ID: `natural-language-evidence-ledger-counterexample-ablation-bb8aeb107f-20260630T061138105892+0000`

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

- Parent run decision: Evidence-ledger tool agent with falsifiable claim counterexamples: enoch://control-plane/projects/evidence-ledger-tool-agent-with-falsifiable-claim-counterexamples-8745bdb565a7/runs/evidence-ledger-tool-agent-with-falsifiable-claim-counterexamples-8745bdb565a7-20260629T152552710860+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/237047725527

## What looked useful

Across 5,400 synthetic cases and 64,800 case-policy-budget rows, the full counterexample-priority ledger reached 1.0000 accuracy and 1.0000 counterexample recall at budget 2, while counterexample ablation reached 0.1111 accuracy and 0.0000 counterexample recall. FIFO context showed position-sensitive degradation, with early and middle counterexamples lost at budget 2.

## Boundaries and scale limits

Synthetic templated evidence only; deterministic parser and decision rule; no real LLM, human-written evidence, noisy retrieval, adversarial paraphrase, or long-horizon agent setting was tested.

## Claim scope

In a deterministic synthetic universal-claim task, a natural-language evidence ledger that preserves explicit counterexamples maintains perfect falsification accuracy under small retained-ledger budgets, while deleting counterexample entries causes systematic false acceptance of false universal claims.

## Why it stopped

Closed as a no-paper useful signal: the bounded synthetic mechanism is supported, but evidence is proxy-only and not sufficient for publication-grade claims about LLM agents or real research ledgers.

## Recommended next action

Run a bounded LLM prompt-level replication with paraphrased evidence streams, comparing full-ledger prompts against counterexample-ablated prompts using blinded final-answer scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM prompt-level counterexample ledger ablation on paraphrased universal claims
- Success threshold: Full-ledger prompting improves counterexample recall by at least 20 percentage points over counterexample-ablation prompting overall and in early/middle counterexample position slices.
- Stop condition: Stop if full-ledger prompting fails to improve counterexample recall by 10 percentage points over counterexample ablation in a 200-case pilot, or if local model outputs cannot be scored consistently.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-evidence-ledger-counterexample-ablation-bb8aeb107f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
