# Bounded Anchor Compression for CPU Long-Context Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-anchor-compression-for-cpu-long-context-retrieval-2ac202238e72`
Run ID: `bounded-anchor-compression-for-cpu-long-context-retrieval-2ac202238e72-20260607T144749706360+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7a69b6f68e37

## What looked useful

With 2 anchors per block and salience >=1.5, salience-anchor retrieval reached 1.0 recall@1 with 4.1-5.9x lower measured online query latency and 32x fewer scanned tokens than full scan; at salience 1.0 recall fell to 0.85, exposing anchor coverage as the limiting mechanism.

## Boundaries and scale limits

Synthetic embeddings only; no real LLM hidden states, natural corpora, ANN baseline, or production serving cache model. Main run used 120 queries per salience setting and one fixed candidate budget.

## Claim scope

Synthetic CPU vector retrieval over 32,768-token contexts shows bounded salience anchors can preserve recall and reduce online scan cost when relevant tokens are captured by the anchor heuristic.

## Why it stopped

Bounded synthetic evidence supports the mechanism conditionally but is not direct/full validation and exposes a low-salience recall failure.

## Recommended next action

Stop this run as no-paper useful signal; next run should test learned or query-aware anchor selection on real-document embeddings with the same full-scan and chunk baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Embedding Bounded Anchor Retrieval
- Success threshold: On held-out real-document queries, learned/calibrated bounded anchors achieve >=0.95 recall@1 or >=0.98 recall@5 with >=16x scanned-token reduction and statistically stable p95 latency improvement over full scan.
- Stop condition: Stop if anchor coverage remains below 0.95 at <=16 anchors per block or if p95 CPU latency is not at least 2x better than full scan after index reuse is accounted for.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-anchor-compression-for-cpu-long-context-retrieval-2ac202238e72`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
