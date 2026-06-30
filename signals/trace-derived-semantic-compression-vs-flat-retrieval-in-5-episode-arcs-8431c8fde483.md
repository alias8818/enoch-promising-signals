# Trace-Derived Semantic Compression vs Flat Retrieval in 5-Episode Arcs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-derived-semantic-compression-vs-flat-retrieval-in-5-episode-arcs-8431c8fde483`
Run ID: `trace-derived-semantic-compression-vs-flat-retrieval-in-5-episode-arcs-8431c8fde483-20260611T122438669750+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfc61bad5e15

## What looked useful

Trace-derived compression is budget-dependent: across five 200-arc seeds it loses to flat raw event retrieval at 45 words by about 0.097 accuracy, but wins at 70-220 words by about 0.070 to 0.200 accuracy because entity/object capsules preserve multi-hop state evidence.

## Boundaries and scale limits

No real corpus, no learned compressor, no LLM reader, no embedding retriever, and no adversarial or noisy extraction errors. The result tests a mechanism proxy rather than a production memory system.

## Claim scope

Synthetic 5-episode arcs with deterministic trace facts, BM25 retrieval within each arc, equal word budgets, trace-derived entity/object memory capsules, and deterministic answer scoring.

## Why it stopped

Synthetic-only bounded proxy produced mixed evidence: useful mechanism signal but not direct validation of trace-derived semantic compression in real 5-episode narrative arcs.

## Recommended next action

Stop this run as no-paper useful signal; next run should test learned or LLM compression against flat, embedding, and graph/multi-hop retrieval baselines on real or model-generated 5-episode traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Compression vs Multi-Hop Retrieval on Realistic 5-Episode Trace QA
- Success threshold: Compression beats the best non-compressed retrieval baseline by at least 5 accuracy points on multi-hop questions at two or more matched budgets, with no more than 2 points regression on single-fact questions at the tightest budget.
- Stop condition: Stop if compression fails to beat explicit multi-hop retrieval on multi-hop questions at matched budgets or if extraction errors erase the synthetic mechanism advantage.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-compression-vs-flat-retrieval-in-5-episode-arcs-8431c8fde483`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
