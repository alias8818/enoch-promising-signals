# Anchor-Verified Speculative Memory Recall

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-verified-speculative-memory-recall-8ebd0341214c`
Run ID: `anchor-verified-speculative-memory-recall-8ebd0341214c-20260628T234643719360+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/aa15f41a92c5

## What looked useful

Anchor verification is a useful safety/control layer: wrong-anchor false accepts were 0.0 across all runs versus 1.0 for unverified speculative winners. The tested SimHash proposal is not viable as a speedup baseline: calibrated speedup was only 0.053x to 0.100x versus dense full scan, with moderate-noise recall only 0.55 to 0.745.

## Boundaries and scale limits

Tested only synthetic random embeddings up to 200000 memories, 1024 dimensions, 100 calibrated queries, CPU NumPy implementation, and a simple SimHash/Hamming shortlist. No real LLM memory, real embedding corpus, production ANN index, or GPU-optimized retrieval was evaluated.

## Claim scope

In a synthetic vector-memory benchmark with unique 64-bit anchors, exact anchor verification eliminated wrong-anchor accepts for a compressed SimHash speculative recall path, but that proposal path was slower than dense full scan and recall was noise-sensitive.

## Why it stopped

Synthetic local evidence supports the anchor gate but falsifies this simple speculative recall path as a practical speedup; this is a bounded mechanism signal, not full validation.

## Recommended next action

Stop this implementation as no-paper evidence; the bounded next test is to replace SimHash proposal with a production ANN or learned index and rerun the same anchor-positive and wrong-anchor protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: ANN-Backed Anchor-Verified Speculative Recall
- Success threshold: At least 0.95 positive anchor-verified recall@1, wrong-anchor false accept rate at or below 1e-6 or zero observed over at least 100000 wrong-anchor probes, and at least 2x latency improvement versus dense full scan on a real embedding workload.
- Stop condition: Stop if ANN-backed recall cannot exceed 0.90 at 1x dense-scan latency or if anchor verification introduces measurable false accepts on wrong-anchor probes.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-verified-speculative-memory-recall-8ebd0341214c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
