# Structured Evidence Ledger for 1B Local Tool Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-for-1b-local-tool-agents-8c3ab57aa984`
Run ID: `structured-evidence-ledger-for-1b-local-tool-agents-8c3ab57aa984-20260523T153104780259+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d616f470598f

## What looked useful

On 12,000 synthetic claim/evidence events and 2,000 random queries, the ledger JSONL was 18.3% of transcript size and returned 100% correct evidence rows at about 161 bytes/query. Transcript tails at 8KB, 16KB, 32KB, and 65KB achieved 0.05%, 0.05%, 0.4%, and 0.65% accuracy respectively; full transcript scan reached 100% only with 10.6MB of context/searchable text.

## Boundaries and scale limits

No 1B model inference, no live tool-use policy, no real user/tool traces, and no downstream task-success measurement. The evidence is a proxy for context pressure and audit retrieval, not a full local-agent validation.

## Claim scope

Synthetic deterministic benchmark of claim-to-evidence recall for context-limited tool-agent traces: a structured ledger with claim-id lookup preserved evidence recall under 8KB-65KB prompt budgets, while raw transcript tails lost nearly all older evidence.

## Why it stopped

Proxy evidence supports the ledger retrieval mechanism but does not directly validate 1B local model behavior, live tool use, or downstream task success.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded direct follow-up with an actual local approximately 1B tool agent on realistic multi-step tasks before making a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Ledger-Backed Recall Test for a Local 1B Tool Agent
- Success threshold: Ledger-backed agent improves citation correctness by at least 20 percentage points over both baselines without reducing final task success or increasing median end-to-end latency by more than 25%.
- Stop condition: Stop if ledger retrieval fails to beat both baselines on citation correctness, or if integration overhead reduces final task success by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-for-1b-local-tool-agents-8c3ab57aa984`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
