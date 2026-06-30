# Long-Context Cascade: Retrieval + Sliding Window vs Full Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `long-context-cascade-retrieval-sliding-window-vs-full-context-a2b9191376fd`
Run ID: `long-context-cascade-retrieval-sliding-window-vs-full-context-a2b9191376fd-20260621T230805510976+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/49b19478d320

## What looked useful

Retrieval-plus-window read 5.61% of full-context tokens in the main run but averaged 28.44% accuracy versus 100% for full-context scan. On 5,000-sentence documents, increasing top-k from 1 to 16 raised accuracy from 4.4% to 48.0% while increasing token fraction from 1.3% to 15.0%. Synonym/paraphrase queries were consistently worse than lexical queries.

## Boundaries and scale limits

No LLM inference, learned retriever, real corpus, GPU throughput, or full long-context serving validation was performed. The benchmark used generated sentence lists, lexical BM25-style window ranking, and exact extractive parsing.

## Claim scope

In a synthetic extractive sparse-evidence QA proxy, lexical retrieval plus fixed sliding windows reduced context read volume but did not preserve the full-context upper-bound accuracy.

## Why it stopped

Proxy early falsification: lexical retrieval plus sliding windows did not approach full-context accuracy under the tested budgets, so this run is not paper-positive.

## Recommended next action

Run a bounded deepen follow-up using semantic or query-expanded retrieval on the same benchmark, with success defined as at least 80% accuracy while reading no more than 20% of full-context tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic retrieval for long-context cascade window selection
- Success threshold: At least 80% overall accuracy and at least 70% synonym-query accuracy while reading no more than 20% of full-context tokens on 5,000-sentence documents.
- Stop condition: Stop if semantic/query-expanded retrieval remains below 60% overall accuracy at a 20% token budget or requires reading more than 20% of full context to exceed lexical top-k 16 accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-cascade-retrieval-sliding-window-vs-full-context-a2b9191376fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
