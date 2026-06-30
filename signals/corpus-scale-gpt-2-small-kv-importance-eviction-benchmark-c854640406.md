# Corpus-scale GPT-2-small KV importance eviction benchmark

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `corpus-scale-gpt-2-small-kv-importance-eviction-benchmark-c854640406`
Run ID: `corpus-scale-gpt-2-small-kv-importance-eviction-benchmark-c854640406-20260612T214531566809+0000`

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

- Parent run decision: Sliding-Window KV Cache with Importance-Score Eviction on GPT-2-Small: enoch://control-plane/projects/sliding-window-kv-cache-with-importance-score-eviction-on-gpt-2-small-f3217d358e04/runs/sliding-window-kv-cache-with-importance-score-eviction-on-gpt-2-small-f3217d358e04-20260611T171002283023+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6f9a06c67866

## What looked useful

Naive cumulative and tail attention-received token importance underperformed recent-only by +1.053549 mean NLL and underperformed random by +0.227520 mean NLL for the tail variant; recent-only was much closer to full context.

## Boundaries and scale limits

Only 8 WikiText-2 test documents, one model, one context length, one budget, CPU-only execution, and prompt-subsequence compression rather than true in-place past_key_values eviction.

## Claim scope

Tier 1 GPT-2-small WikiText-2 test of attention-derived prefix-token eviction at 48 retained tokens from 128-token prefixes for 8-token continuations.

## Why it stopped

Controlled small direct GPT-2-small corpus test falsified the tested naive attention-importance eviction mechanism relative to recent-only; this is not a full validation of all possible KV importance methods.

## Recommended next action

Stop the paper path for naive attention-received KV importance eviction; only revisit with a true position-preserving KV-cache implementation and a predeclared margin over recent-only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Position-preserving GPT-2 KV-cache eviction vs recent-only
- Success threshold: Online position-preserving importance must reduce mean NLL by at least 5% versus recent-only and win on at least 60% of documents for both tested budgets.
- Stop condition: Stop as negative if position-preserving importance fails to beat recent-only on either mean NLL or document win rate for any tested budget.

## Evidence references

- Artifact root: `<local-path>/projects/corpus-scale-gpt-2-small-kv-importance-eviction-benchmark-c854640406`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
