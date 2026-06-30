# External summary+retrieval memory vs full-transcript long-horizon agent

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `external-summary-retrieval-memory-vs-full-transcript-long-horizon-agent-2f15c0e1caab`
Run ID: `external-summary-retrieval-memory-vs-full-transcript-long-horizon-agent-2f15c0e1caab-20260610T144115571385+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/021ea2559543

## What looked useful

Default medium run: summary80_retrieve8 reached 0.824 mean evidence-exposure accuracy at 870.6 mean context tokens; full_window_1800tok reached 0.246 at 1795.8 tokens; full_unbounded reached 1.000 at 8579.6 tokens. Low-memory summary30_retrieve3 still beat transcript window overall but latest-value accuracy dropped to 0.568.

## Boundaries and scale limits

Synthetic benchmark only; no real LLM answerer, no learned/generated summarizer, no semantic embedding index, no noisy paraphrase workload, and no real agent traces. Medium runs covered 12 seeds, 1600 events per seed, and 300 queries per seed.

## Claim scope

On deterministic synthetic long-horizon transcripts with exact entity/attribute queries, a recency-summary plus lexical retrieval memory exposed required evidence much more accurately than a same-budget recency transcript window while using fewer context tokens; it did not beat unbounded full transcript accuracy.

## Why it stopped

No-paper closure: the result is a bounded synthetic useful signal, not a full validation of long-horizon agents or real LLM behavior.

## Recommended next action

Run a bounded direct LLM follow-up using generated natural-language summaries plus BM25/vector retrieval and paraphrased held-out queries; stop treating the current synthetic memory-oracle result as paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM QA test for summary+retrieval memory on paraphrased long-horizon transcripts
- Success threshold: Summary+retrieval accuracy >= 85% of unbounded transcript accuracy, <= 25% of unbounded mean context tokens, and >= 20 percentage points above same-budget transcript window across at least 1000 held-out queries.
- Stop condition: Stop if summary+retrieval fails to beat the same-budget transcript window by 10 percentage points on a 200-query pilot or if generated-summary drift causes unrecoverable evidence loss in more than 25% of latest-value queries.

## Evidence references

- Artifact root: `<local-path>/projects/external-summary-retrieval-memory-vs-full-transcript-long-horizon-agent-2f15c0e1caab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
