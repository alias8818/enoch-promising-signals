# Agent reliability via evidence ledger for small LLM agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-via-evidence-ledger-for-small-llm-agents-d4411aee3ddc`
Run ID: `agent-reliability-via-evidence-ledger-for-small-llm-agents-d4411aee3ddc-20260605T133655326041+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/b70d1f1aa7de

## What looked useful

Main run unsupported claim rate fell from 0.2922 to 0.0360, supported answer rate rose from 0.5494 to 0.9376, and exact answer rate rose from 0.5775 to 0.9376. Cost was +0.5114 mean tool calls and +0.0529 abstention rate. Sensitivity sweeps showed unsupported-claim reductions from 0.1277 to 0.3655 absolute across tested noise regimes.

## Boundaries and scale limits

No real LLM, real tool environment, natural-language entailment, adversarial corpus, or long-horizon user workflow was evaluated. Results are limited to 100,000 main synthetic trials plus four 20,000-trial sensitivity settings on a CPU-only simulator.

## Claim scope

In a controlled synthetic proxy for small-agent failures, adding an evidence ledger with per-claim support checks, one strict retrieval retry, and abstention reduced unsupported final claims across retrieval-miss, distractor, stale-evidence, and composition-error regimes.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy-only and does not directly validate real small LLM agents.

## Recommended next action

Run a bounded direct small-LLM agent evaluation using the same ledger policy on natural-language tool QA tasks before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-LLM evaluation of evidence-ledger support checks
- Success threshold: Unsupported final-answer rate reduced by >=25% relative while exact/task success drops by <=5 percentage points and mean tool-call overhead remains <=2x baseline.
- Stop condition: Stop if unsupported final-answer reduction is <10% relative, exact/task success drops by >10 percentage points, or ledger overhead exceeds 3x baseline without compensating reliability gain.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-evidence-ledger-for-small-llm-agents-d4411aee3ddc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
