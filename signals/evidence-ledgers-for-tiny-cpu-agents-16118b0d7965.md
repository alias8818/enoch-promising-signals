# Evidence-Ledgers for Tiny CPU Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledgers-for-tiny-cpu-agents-16118b0d7965`
Run ID: `evidence-ledgers-for-tiny-cpu-agents-16118b0d7965-20260603T203053830049+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8eb4dc190ee9

## What looked useful

Evidence ledgers can preserve latest values and source citations far better than raw context when relevant facts are admitted to the ledger, but distractor filtering and efficient bounded eviction are necessary for viability on tiny CPU agents.

## Boundaries and scale limits

No real LLM/tiny-agent harness, no natural-language extraction errors, no adversarial ambiguity, and no production workload. The strongest positive result uses an oracle-style synthetic relevance filter; the fully budget-compliant unfiltered ledger only modestly improves accuracy.

## Claim scope

Synthetic CPU-only benchmark of latest-fact and source retention under a fixed character budget, comparing raw sliding context with structured evidence-ledger variants.

## Why it stopped

Synthetic proxy produced mixed evidence: mechanism supported with filtering, but unfiltered budget-compliant ledger only modestly beat raw context and naive ledger was CPU-expensive.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate a non-oracle relevance gate and natural-language extraction in a real tiny CPU agent harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle relevance gates for evidence ledgers in tiny CPU agents
- Success threshold: Gated ledger reaches at least 0.90 value and source accuracy, improves raw context by at least 0.40 absolute accuracy, and stays below 20x raw ingest latency under the same memory budget.
- Stop condition: Stop if the gated ledger improves raw context by less than 0.20 absolute accuracy or exceeds 50x raw ingest latency on two independent natural-language task sets.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledgers-for-tiny-cpu-agents-16118b0d7965`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
