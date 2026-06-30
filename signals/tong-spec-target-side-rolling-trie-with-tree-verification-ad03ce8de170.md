# TONG-spec target-side rolling trie with tree verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tong-spec-target-side-rolling-trie-with-tree-verification-ad03ce8de170`
Run ID: `tong-spec-target-side-rolling-trie-with-tree-verification-ad03ce8de170-20260619T042800763334+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6dad8e1c9970

## What looked useful

Rolling trie verification matched rebuilt reference roots on all non-corrupted checks, detected all injected corruptions in smoke and medium probes, and showed 11.66x-14.8x end-to-end advantage over rebuild verification when checks were frequent, shrinking to 1.33x when checks were sparse.

## Boundaries and scale limits

Synthetic workloads only; no real TONG implementation, decoder trace, model-serving path, compiled data structure, concurrency, or large-scale throughput validation was tested. The first larger Python profile was interrupted after roughly 10 minutes, so performance claims are limited to the reduced 6000-op/window-512 CPU profile.

## Claim scope

In a bounded synthetic target-token workload, an incremental rolling trie with Merkle-style root verification maintained equivalence with a rebuilt reference trie and detected injected state divergence while making frequent verification much cheaper than rebuild-on-verify.

## Why it stopped

No-paper closure: this run produced useful synthetic mechanism evidence, but it did not directly validate TONG-spec behavior or real decoder integration.

## Recommended next action

Run a bounded direct follow-up using real target-side speculative decoding traces and an optimized implementation before considering any paper or production claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-backed target-side rolling trie verification
- Success threshold: Zero unexpected root divergences, 100% detection of injected tree-state corruptions, and at least 3x end-to-end verification overhead reduction versus rebuild-on-verify on frequent-verification real traces without more than 2x memory overhead.
- Stop condition: Stop as negative if real traces show unexpected root divergence, missed injected corruptions, or less than 1.5x end-to-end overhead reduction in the frequent-verification regime after implementation-level optimization.

## Evidence references

- Artifact root: `<local-path>/projects/tong-spec-target-side-rolling-trie-with-tree-verification-ad03ce8de170`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
