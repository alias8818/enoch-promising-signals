# Real Tiny-LLM Evidence-Ledger Tool-Use Evaluation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-tiny-llm-evidence-ledger-tool-use-evaluation-674a5c5e95`
Run ID: `real-tiny-llm-evidence-ledger-tool-use-evaluation-674a5c5e95-20260524T155210999317+0000`

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

- Parent run decision: Evidence-Ledger Constraint for Tiny Tool-Using Agents: enoch://control-plane/projects/evidence-ledger-constraint-for-tiny-tool-using-agents-4b5da8989cda/runs/evidence-ledger-constraint-for-tiny-tool-using-agents-4b5da8989cda-20260524T084003946062+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57c7e86ee078

## What looked useful

A real-model Tier 1 direct test supports the mechanism but also shows citation-only prompts can fail: Qwen2.5-1.5B fabricated evidence IDs and abstained until the ledger protocol explicitly required first-action tool use.

## Boundaries and scale limits

Only four tasks per model were evaluated; tasks were local calculator/private-table lookup questions; support labels were deterministic programmatic labels; prompts were adjusted after an observed citation-fabrication failure; no public benchmark, human audit, adversarial evidence, or confidence interval study was run.

## Claim scope

On a tiny four-task balanced local tool-use QA set, two real Qwen2.5 instruction models in the 0.5B-1.5B range met the ledger-retry threshold: unsupported final answers fell to zero with no exact-match loss and no abstention when ledger mode explicitly required a real tool call before final answer acceptance.

## Why it stopped

Stopped after satisfying the Tier 1 controlled small direct test on two real models; further CPU-only scale would exceed the local worker resource-efficiency envelope and is needed before any paper claim.

## Recommended next action

Run a pre-registered 50-100 example public tool-use QA evaluation on the same two models with the explicit first-tool-call ledger protocol, fixed prompts, matched budgets, bootstrap intervals, and independent support labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pre-registered Public Benchmark Confirmation of Evidence-Ledger Tool-Use Gating
- Success threshold: Both tested models show at least 50% unsupported-final reduction, ledger accuracy no more than 5 absolute percentage points below baseline, and ledger abstention no higher than 20%, with confidence intervals not contradicting the effect.
- Stop condition: Stop if either model fails the unsupported-answer reduction threshold, ledger abstention exceeds 20%, or exact-match accuracy drops by more than 5 absolute percentage points under fixed prompts.

## Evidence references

- Artifact root: `<local-path>/projects/real-tiny-llm-evidence-ledger-tool-use-evaluation-674a5c5e95`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
