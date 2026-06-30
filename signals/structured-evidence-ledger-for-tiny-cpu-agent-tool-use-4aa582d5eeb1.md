# Structured evidence ledger for tiny CPU agent tool use

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `structured-evidence-ledger-for-tiny-cpu-agent-tool-use-4aa582d5eeb1`
Run ID: `structured-evidence-ledger-for-tiny-cpu-agent-tool-use-4aa582d5eeb1-20260522T120510116800+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c1981d2fd8ee

## What looked useful

Evidence ledgers reached 100% accuracy across all grid points versus 8.23% for raw tail truncation and 75.10% for same-entity retrieval, but exact-key transcript retrieval also reached 100% accuracy while using fewer visible bytes in this synthetic setup.

## Boundaries and scale limits

Tested only synthetic traces, deterministic regex extraction/answering, 1000 episodes per grid point, four context budgets up to 4096 characters, and one CPU process. No real small LLM, noisy extraction, production tool traces, or interactive planning loop was evaluated.

## Claim scope

On a synthetic deterministic CPU benchmark with regular entity.attribute=value tool observations, a structured evidence ledger preserves queried facts under tight context budgets better than raw transcript tail truncation and coarse same-entity retrieval, but not better than exact-key raw transcript retrieval.

## Why it stopped

Synthetic proxy supports the ledger mechanism only against weak/coarse memory baselines and is not a full validation against strong retrieval or real tiny-agent behavior.

## Recommended next action

Stop this run as no-paper useful signal; any next test should add noisy extraction and a real tiny local model while keeping exact-key transcript retrieval as a required baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy extraction ledger versus exact transcript retrieval for a real tiny CPU agent
- Success threshold: Ledger beats the strongest transcript retrieval baseline by at least 5 percentage points absolute accuracy at 1024-2048 character budgets, or matches accuracy while providing measurable provenance/audit benefits with no more than 25% latency overhead.
- Stop condition: Stop if exact or semantic transcript retrieval matches ledger accuracy and provenance utility within the budget, or if extraction errors erase the ledger advantage.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-for-tiny-cpu-agent-tool-use-4aa582d5eeb1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
