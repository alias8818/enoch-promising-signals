# Compressed episodic ledger for small-agent tool-use reliability on 10GB GPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-episodic-ledger-for-small-agent-tool-use-reliability-on-10gb-gpu-d510d14804c4`
Run ID: `compressed-episodic-ledger-for-small-agent-tool-use-reliability-on-10gb-gpu-d510d14804c4-20260602T150130667946+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e07d7bd80473

## What looked useful

At a 1024-token budget over 30 trials and 82,221 queries, compressed_ledger accuracy was 0.500 versus raw_window 0.142 and entity_summary 0.416. Budget sweep showed compressed_ledger accuracy rising from 0.178 at 256 tokens to 0.958 at 4096 tokens, consistently above raw_window.

## Boundaries and scale limits

No real LLM inference, natural-language extraction, online summarization, real tool APIs, adversarial updates, or long-horizon production traces were tested. Results are CPU-only synthetic simulations, not publication-grade deployment evidence.

## Claim scope

In synthetic exact-argument tool-use episodes with 96 entities, six attributes, and fixed token budgets, a compressed key-value episodic ledger improves recall reliability over a raw recency window at equal approximate token budget.

## Why it stopped

Evidence supports the memory mechanism only in a synthetic proxy; it is insufficient for a paper or real-agent reliability claim.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test the same ledger in a real small LLM agent loop with noisy extraction and actual tool-call scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-LLM tool-use test for compressed episodic ledger
- Success threshold: Compressed ledger improves exact tool-call success by at least 15 percentage points over raw recency and by at least 5 points over entity_summary at the same budget, without increasing wrong stale calls by more than 2 points.
- Stop condition: Stop if the ledger fails to beat entity_summary by 5 points on two independent seeds, or if extraction noise causes more than 10 percent wrong stale tool calls.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-episodic-ledger-for-small-agent-tool-use-reliability-on-10gb-gpu-d510d14804c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
