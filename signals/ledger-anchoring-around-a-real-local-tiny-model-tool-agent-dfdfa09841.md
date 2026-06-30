# Ledger anchoring around a real local tiny model/tool-agent loop

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `ledger-anchoring-around-a-real-local-tiny-model-tool-agent-dfdfa09841`
Run ID: `ledger-anchoring-around-a-real-local-tiny-model-tool-agent-dfdfa09841-20260530T015353451499+0000`

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

- Parent run decision: Ledger anchoring in a local tiny language-agent harness: enoch://control-plane/projects/ledger-anchoring-in-a-local-tiny-language-agent-harness-642f59c44a/runs/ledger-anchoring-in-a-local-tiny-language-agent-harness-642f59c44a-20260529T213541938038+0000
- Parent run decision: Evidence-ledger anchoring for tiny CPU-bound agents: enoch://control-plane/projects/evidence-ledger-anchoring-for-tiny-cpu-bound-agents-3a3368291be6/runs/evidence-ledger-anchoring-for-tiny-cpu-bound-agents-3a3368291be6-20260529T101321005606+0000

## What looked useful

The task environment was solvable by a deterministic oracle at 30/30, but the tiny LM selected zero apply_transaction actions in 120 fixed-seed episodes, yielding 0/30 success for baseline, ledger_anchor, and both ablations. Ledger anchoring cannot help when the model policy never invokes the state-mutating tool.

## Boundaries and scale limits

Evidence is limited to one very small non-instruction causal LM as the medium fixed-seed run. A pythia-14m smoke check was also negative but too slow for a CPU-only medium run. The result does not rule out instruction-tuned 0.5B-1.5B local models, finetuned tool policies, or GPU-hosted runs.

## Claim scope

For a real local sshleifer/tiny-gpt2 causal-LM tool-agent that scores constrained ledger actions by conditional likelihood, ledger anchoring did not improve deterministic ledger reconciliation success over a no-ledger baseline across 5 fixed seeds, 30 tasks, and two ablations.

## Why it stopped

Direct fixed-seed test failed the preregistered support threshold: ledger success rate was 0.00, delta versus baseline was 0.00, and action diagnostics showed no transaction-application actions.

## Recommended next action

Stop this run as no-paper negative evidence; the next bounded test should use an instruction-tuned local model and require nonzero tool-mutation competence before measuring ledger anchoring benefits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ledger anchoring with an instruction-tuned local tool policy
- Success threshold: Ledger anchoring must reach at least 70% final-ledger success and improve by at least 10 percentage points over no-ledger baseline, with ablations reducing or eliminating the gain.
- Stop condition: Stop as negative if the instruction-tuned model selects apply_transaction in fewer than 50% of tasks or ledger anchoring fails to improve final success by at least 10 percentage points over baseline.

## Evidence references

- Artifact root: `<local-path>/projects/ledger-anchoring-around-a-real-local-tiny-model-tool-agent-dfdfa09841`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
