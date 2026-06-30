# Tool-Use Evidence Ledger for Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tool-use-evidence-ledger-for-small-agents-9a80a6d8f940`
Run ID: `tool-use-evidence-ledger-for-small-agents-9a80a6d8f940-20260522T173447912241+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/79d3f7dbc52f

## What looked useful

Across 30 runs and 150,000 synthetic tasks, ledger_k3 improved mean accuracy over baseline_recency_k3 by +0.153 to +0.646 absolute depending on noise/order condition; ledger_full improved by +0.246 to +0.732 and achieved full conflict recall.

## Boundaries and scale limits

Evidence is synthetic/proxy only: no real LLM agent, natural-language transcript parsing, learned source reliability, external tools, or long-horizon trajectories were tested.

## Claim scope

In a controlled synthetic tool-use QA benchmark with known source reliability priors and noisy conflicting observations, a structured evidence ledger improves small-agent answer accuracy and order robustness versus bounded recency-memory baselines.

## Why it stopped

Closed as no-paper useful signal because the local evidence supports the ledger mechanism only in a synthetic proxy, not in real small LLM agents.

## Recommended next action

Run a bounded follow-up with an actual small instruction model maintaining the ledger over natural-language tool transcripts and order-perturbed evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM Evidence Ledger on Natural-Language Tool Traces
- Success threshold: Ledger condition improves accuracy by at least 10 absolute percentage points over the no-ledger baseline in adversarial-order traces while keeping ledger-format failures below 5%.
- Stop condition: Stop if the model cannot maintain the ledger format above 95% validity after two prompt variants, or if accuracy gain is under 5 points on two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/tool-use-evidence-ledger-for-small-agents-9a80a6d8f940`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
