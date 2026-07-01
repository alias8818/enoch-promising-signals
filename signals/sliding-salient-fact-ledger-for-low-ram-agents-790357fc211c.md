# Sliding Salient-Fact Ledger for Low-RAM Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sliding-salient-fact-ledger-for-low-ram-agents-790357fc211c`
Run ID: `sliding-salient-fact-ledger-for-low-ram-agents-790357fc211c-20260524T205150219526+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d085e78b642

## What looked useful

Salient ledger exact-match accuracy was 0.3763 at 1024 bytes and 0.7023 at 2048 bytes versus sliding-window accuracy of 0.0025 and 0.0069. Important-fact accuracy reached 0.5608 at 1024 bytes and 0.9997 at 2048 bytes, while sliding windows remained below 0.008. Salience beat random fact eviction by 9.7 points at 1024 bytes and 14.2 points at 2048 bytes.

## Boundaries and scale limits

The run used 500 synthetic episodes, 600 turns, 40 queries per episode, and byte-budgeted memory representations only. It did not test real LLM extraction, natural conversations, agent planning, adversarial wording, multi-hop reasoning, or production RAM/token overhead.

## Claim scope

In a deterministic synthetic long-conversation memory task with perfect fact extraction, compact salient-fact ledgers preserve answerable facts far better than raw sliding transcript windows under 512-8192 byte budgets; salience-based eviction improves over random fact eviction most clearly at 1024-2048 bytes.

## Why it stopped

Synthetic perfect-extraction proxy supports the mechanism but is not direct/full validation and is insufficient for a paper-positive decision.

## Recommended next action

Stop this run as a no-paper useful signal; next run should evaluate the same ledger policy with a real LLM fact extractor on naturalistic conversations under token and RAM budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Extractor Salient Ledger under sequence-item budgets
- Success threshold: At 1024-2048 token-equivalent memory budgets, salient ledger improves held-out query accuracy by at least 10 percentage points over random fact eviction and at least 25 percentage points over sliding windows, with extractor-attributable errors reported separately.
- Stop condition: Stop if extractor noise reduces salient-ledger accuracy to within 5 percentage points of random fact eviction at both 1024 and 2048 token-equivalent budgets, or if sliding windows match ledger accuracy under the same budget.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-salient-fact-ledger-for-low-ram-agents-790357fc211c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
